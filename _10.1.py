PetsName = input('Имя питомца:')
PetsType = input('Вид:')
PetsAge = int(input('Возраст:'))
OwName = input('Владелец:')
pets = {PetsName:{"Вид питомца": PetsType, "Возраст питомца": PetsAge, "Имя владельца": OwName}}

if PetsAge % 10 == 1:
    print('Это', pets[PetsName]["Вид питомца"],'по кличке', '"' + PetsName + '"' + '.', 'Возраст питомца:', PetsAge, 'год' + '.', 'Имя владельца:', OwName, end = '.')
elif PetsAge % 10 > 1 and PetsAge % 10 < 5:
    print('Это', pets[PetsName]["Вид питомца"],'по кличке', '"' + PetsName + '"' + '.', 'Возраст питомца:', PetsAge, 'года' + '.', 'Имя владельца:', OwName, end = '.')
else:
    print('Это', pets[PetsName]["Вид питомца"],'по кличке', '"' + PetsName + '"' + '.', 'Возраст питомца:', PetsAge, 'лет' + '.', 'Имя владельца:', OwName, end = '.')