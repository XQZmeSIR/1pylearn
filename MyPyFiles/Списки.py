motorcycles.append('dicati') # Addind elements TO THE END OF THE list.
# Метод append() упрощает динамическое построение списков. Например, вы можете начать с пустого списка и добавлять в него элементы серией команд append().
# Often usedF

print(motocycle)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

# Вставка элементов в список
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(2, 'bmw') # Метод insert() позволяет добавить новый элемент в произвольную позицию списка.
print(motorcycles)

moto = []
moto.append("honda")
moto.append("bmv")
print(moto)

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')  # Adding an element to the list


print(motorcycles)

moto = ['honda', 'ihfwe', 'ehw']

del moto[1]   # del allows you to delete particular elemen in the list
print(moto)   # after del data are no longer available


moto = ['honda', 'yamaha', 'suzuki']
print(moto)
poped_moto = moto.pop()   # it allows u to delete the last item in the list
print(moto)     # but u can save the item instead of deleting
print(poped_moto)


moto = ['honda', 'yamaha', 'suzuki']

last_owened = moto.pop()
print(f'Last owened moto is {last_owened.title()}.')   # пример с Ф строкой


last_owened = moto.pop(0)    # pop method can be used for deleting
print(f'Last owened moto is {last_owened.title()}.')  # a particular item in the list

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('honda')   # .remove позволяет удалить определ значение в списке
print(motorcycles)

print()
print()

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)

print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")


print()

#  ##Exercise 3.4

guests1 = ['Alex', 'Ivan']
guests2 = ['Paul', 'Charles']

invite1 = guests1.pop(0)
invite2 = guests1.pop(0)
invite3 = guests2.pop(0)
invite4 = guests2.pop(0)

print(f"Welcome, {invite1}!")
print(f"Welcome, {invite2}!")
print(f"Welcome, {invite3}!")
print(f"Welcome, {invite4}!")

## вроде все


###Exersize 3.5

print("Unfortunatly,", invite1, "will not be able to attend our meeting")

del guests1[1]

guests1.append("Maxim")

invite1 = guests1.pop(0)
invite2 = guests1.pop(0)
invite3 = guests2.pop(0)
invite4 = guests2.pop(0)


print(f"Welcome, {invite1}!")
print(f"Welcome, {invite2}!")
print(f"Welcome, {invite3}!")
print(f"Welcome, {invite4}!")

print(print)
