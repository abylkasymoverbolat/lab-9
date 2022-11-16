[15:31, 16.11.2022] Abylkasymov: import random
names = ['Маша', 'Петя', 'Вася']
code_names = ['Шпунтик', 'Винтик', 'Фунтик']
for i in range(len(names)):
names[i] = random.choice(code_names)
print(names
[15:43, 16.11.2022] Abylkasymov: import random
names = ['Маша', 'Петя', 'Вася']
secret_names = map(lambda x: random.choice(['Шпунтик', 'Винтик', 
'Фунтик']), names)
print(list(secret_names))







Пример: list1 = [10, 11, 12, 13, 14] list2 = [20, 30, 42] print("List1 before Concatenation:\n" + str(list1)) for x in list2 : list1.append(x) print ("Concatenated list i.e. list1 after concatenation:\n" + str(list1))





def func(a, b): #функ создать етемз
    return a + b
a = map(func, [2, 4, 5], [1,2,3])#map аркылы элемент доступ беру
print(tuple(a)) #кортеж аркылы
