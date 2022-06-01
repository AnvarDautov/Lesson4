# Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого
# файла по возрастанию.

max_val = 100
quantity = 10
data = open(path, 'w')
 for i in range(quantity):
     data.write(f'{str(randint(0, max_val))},')
 data.close()

 with open(path, 'r') as fr:
     list_int = fr.readline().split(',')
     list_int.pop()
     list_int.sort(key=(int))
 print(list_int)