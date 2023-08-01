import datetime


# Read and import tickets from the text file into the Special List
def read_tickets_from_file(file_name):
  special_list = []
  try:
    with open(file_name, 'r') as file:
      for line in file:
        ticket_info = line.strip().split(', ')
        special_list.append(ticket_info)
  except FileNotFoundError:
    print("Error: Ticket file not found.")
  return special_list


# login form for the user and the admin, if the user has username admin so this is the admin, he has 5 attempts to enter his right password, if the user is a normal user so the password should be space or empty  password


def login():
  print("Welcome to the Corrupted Ticketing System!")

  admin_attempts = 5
  while admin_attempts > 0:
    username = input("Enter your username: ")
    if username.lower() == "admin":
      password = input("Enter your password: ")
      if password == "admin123123":
        print("Admin Login Successful")
        return "admin"
      else:
        admin_attempts -= 1
        print("Incorrect Username and/or Password, {} attempts left!!!!!!!!!!".
              format(admin_attempts))

    else:
      # Ask for password for normal users
      password = input("Enter your password: ")
      # If the password is empty (blank or spaces only)
      if not password.strip():
        print("Normal User Login Successful")
        return username  # Return the username instead of "user"
      else:
        print("Incorrect Password for normal user. Try again.")

  print("Max login attempts reached .... Access denied")
  return None


# Implementation the menu options for the admin and normal user
def admin_menu(special_list):
  while True:
    print("\n\n****Admin Menu Options:****  ")
    print("1. Display Statistics")
    print("2. Book a Ticket")
    print("3. Display all Tickets")
    print("4. Change Ticket’s Priority")
    print("5. Disable Ticket")
    print("6. Run Events")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
      display_statistics(special_list)
    elif choice == "2":
      book_ticket(special_list)
    elif choice == "3":
      display_all_tickets(special_list)
    elif choice == "4":
      change_ticket_priority(special_list)
    elif choice == "5":
      disable_ticket(special_list)
    elif choice == "6":
      special_list = display_and_remove_today_events(special_list)
    elif choice == "7":
      print("Exit The Admin Menu.")
      break
    else:
      print("Invalid choice, please lets try again.")


#Option 1 ----> Display Statistics
def display_statistics(special_list):

  #empty dictionary event_counter to store the occurrence count for each event ID.
  event_counter = {}
  #extract the event ID from the ticket and add it to the event_counts dictionary, if the event ID is already present in the dictionary, the counter is incremented by 1 else a new id is added with a count of 1.

  for ticket in special_list:
    event_id = ticket[1]  #extract the event ID from the ticket
    #update the occurrence count for the event ID,if event_id key is not present in the event_counter dictionary, the get() method will return 0.
    event_counter[event_id] = event_counter.get(event_id, 0) + 1

  #Check if there are any tickets in the system
  #if the dictionary is not empty
  # it finds the ID of event with the highest number of tickets in the

  # reference to get the max value of a dictionary :: https://datagy.io/python-get-dictionary-key-with-max-value/
  if event_counter:
    max_event_id = max(event_counter, key=event_counter.get)

    print(
      "Event ID with the highest number of tickets: {}".format(max_event_id))
  else:  #if the dictionary is empty
    print("No tickets in the system.")


#Option 2 ----> for user menu  : Book a Ticket
#allow the admin to book a new ticket for an event by specifying the username, event ID, date of the event and priority (the ticket ID auto-incremented, The text file includes several tickets in the following format: tick101, ev003, fred, 20230802, 0


def book_ticket(special_list):
  now_date = datetime.datetime.now()
  today = now_date.strftime("%Y%m%d")
  ticket_id = "tick" + str(len(special_list) + 101)
  event_id = input("Enter Event ID: ")
  username = input("Enter Username: ")
  date_str = input("Enter Date of the Event (like yyyymmdd): ")
  priority = input("Enter Priority (0-9): ")

  new_ticket = [ticket_id, event_id, username, date_str, priority]
  special_list.append(new_ticket)

  if date_str >= today:
    print("Ticket booked successfully!")
  else:
    print("Ticket UNBOOKED!, the time of the ticket is passed. ")


#Option 3 ---->  Display all Tickets


def sort_tickets(ticket):
  return (ticket[3], ticket[1])


def display_all_tickets(special_list):
  now_date = datetime.datetime.now()
  today = now_date.strftime("%Y%m%d")

  upcoming_tickets = [
    ticket for ticket in special_list
    if len(ticket) >= 5 and ticket[3] >= today
  ]
  sorted_tickets = sorted(upcoming_tickets, key=sort_tickets)

  if sorted_tickets:
    print("Upcoming Tickets:")
    for ticket in sorted_tickets:
      print(
        "Ticket ID: {}, Event ID: {}, Username: {}, Date: {}, Priority: {}".
        format(ticket[0], ticket[1], ticket[2], ticket[3], ticket[4]))
  else:
    print("No upcoming tickets in the system.")


# Option 4 ----> Change Ticket’s Priority
def change_ticket_priority(special_list):
  ticket_id = input("Enter Ticket ID: ")
  priority = input("Enter new Priority (0-9): ")

  for ticket in special_list:
    if ticket[0] == ticket_id:
      ticket[4] = priority
      print("Congratulations: Priority updated successfully!")
      break
  else:
    print("Ticket not found.")


#Option 5 ----> Disable Ticket
def disable_ticket(special_list):
  ticket_id = input("Enter Ticket ID to disable: ")

  for ticket in special_list:
    if ticket[0] == ticket_id:
      special_list.remove(ticket)
      print("Ticket disabled successfully!")
      break
  else:
    print("Ticket not found.")


#Option 6 ----> Run Events


def get_priority(ticket):
  return ticket[4]


def display_and_remove_today_events(special_list):
  today = datetime.datetime.now().strftime("%Y%m%d")
  today_events = [ticket for ticket in special_list if ticket[3] == today]
  if today_events:
    today_events.sort(key=get_priority, reverse=True)
    for ticket in today_events:
      print("Running Event ID: {}, Priority: {}".format(ticket[1], ticket[4]))
    special_list = [
      ticket for ticket in special_list if ticket not in today_events
    ]
    return special_list
  else:
    print("No events to run today.")
    return special_list


def user_menu(special_list, username):
  while True:
    print("\n\n****User Menu Options:****  ")
    print("1. Book a Ticket")
    print("2. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
      book_ticket_for_user(
        special_list, username)  # Pass the username to book_ticket_for_user
    elif choice == "2":
      print("Normal User logout successful.")
      break
    else:
      print("Invalid choice, please try again.")


def book_ticket_for_user(special_list, username):
  now_date = datetime.datetime.now()
  today = now_date.strftime("%Y%m%d")
  ticket_id = "tick" + str(len(special_list) + 101)
  event_id = input("Enter Event ID: ")
  date_str = input("Enter Date of the Event (like yyyymmdd): ")
  priority = "0"  # Default priority is set to 0

  new_ticket = [ticket_id, event_id, username, date_str, priority]
  special_list.append(new_ticket)

  if date_str >= today:
    print("Ticket booked successfully!")
  else:
    print("Ticket UNBOOKED!, the time of the ticket is passed.")


def main():
  file_name = "ticketFile.txt"
  special_list = read_tickets_from_file(file_name)

  user_type = login()
  if user_type == "admin":
    admin_menu(special_list)
  else:
    user_menu(special_list, user_type)  # Pass the username instead of "user"

  # Use a flag variable to determine if data should be saved to file
  save_to_file = True
  if user_type == "7":
    save_to_file = False

  if save_to_file:
    with open(file_name, 'w') as file:
      for ticket in special_list:
        file.write(", ".join(ticket) + "\n")


if __name__ == "__main__":
  main()
