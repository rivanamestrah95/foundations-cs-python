import json


def Tuples(tuple1, tuple2):
  sums = ()
  for i in range(len(tuple1)):
    sums += (tuple1[i] + tuple2[i], )
  return (sums)


def dictFile(dict, fname):
  with open(fname, 'w') as file:  #indent=4
    json_str = json.dumps(dict, separators=(',', ':'))
    file.write(json_str)


#i dont now how can we input a tuple
while (True):
  print("1. Sum Tuples")
  print("2. Export JSON")
  print("3. Import JSON")
  print("4. Exit")
  print("- - - - - - - - - - - - - - -")
  choice = input("enter a choice: ")
  if choice == "1":
    re = Tuples((3, 2, 3, 5), (5, 7, 1, 1))
    print(re)
  elif choice == "2":
    my_dict = {"name": "Rivana", "age": 25, "city": "Lebanon"}
   dictFile(my_dict, "myfile1.json")

  else:
    break
