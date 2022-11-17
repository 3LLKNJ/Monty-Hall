doors = {'1':False,'2':False,'3':True}
chosenDoor = '2'


numbers = [1,2,3]
numbers.remove(int(chosenDoor))
print(numbers)
print(list(doors.keys())[list(doors.values()).index(True)])
numbers.remove(int(list(doors.keys())[list(doors.values()).index(True)]))