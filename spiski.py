# Работа со списками

spisok_1 = ['biba', 'boba', 'bobus']
print(spisok_1)
print(spisok_1[0].title())
print(spisok_1[1].upper())
print(spisok_1[2].lower())
print(spisok_1[-1].upper())
print(f"Один из элементов в списке {spisok_1[2].title()}")
spisok_1[0] = 'aboba'
print(spisok_1)
spisok_1.append('habib')
print(spisok_1)
spisok_1.insert(0, 'rabota')
print(spisok_1)
del spisok_1[0]
print(spisok_1)
popped_spisok_1 = spisok_1.pop()
print(spisok_1)
print(f"Удалённый элемент из списка: {popped_spisok_1}")
random_pop = spisok_1.pop(1)
print(f"Элемент {random_pop} под номером один удалён из списка")
print(spisok_1)
spisok_1.remove('aboba')
print(spisok_1)
list_element = 'bobus'
spisok_1.remove(list_element)
print(spisok_1)
spisok_2 = ['1111', '1111', '1111', '11']
print(spisok_2)
spisok_2.remove('1111')
print(spisok_2)
spisok_3 = ['Svyat', 'Darina', 'Nikita', 'Ivan']
print(spisok_3)
spisok_3.sort()
print(spisok_3)
spisok_3.sort(reverse=True)
print(spisok_3)
spisok_4 = ['1', '2', '3', '7', '4', '5']
print(spisok_4)
print('sorted')
print(sorted(spisok_4))
print(spisok_4)
len(spisok_4)
print(len(spisok_4))

