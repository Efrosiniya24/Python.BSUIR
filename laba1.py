import random

def main():
    while True:
        task = input("Введите номер задания: ")
        if task == "1":
            task1()
        elif task == "2":
          task2()
        elif task == "3":
            task3()
        elif task == "4":
            task4()
        elif task == "6":
            task6()
        elif task == "5":
            task5() 
        else:
            print("Неверный ввод")
        i = input("Продолжить? \n 1)Да 2)Нет\n")
        if i != "2" : break
    


def task1():
    numberRandom = random.randint(1,20)
    counter = 1

    print("Угадайте число)\n")
    while True:
        number = int(input("Введите число: "))
        if number > numberRandom :
           print("Ваше число больше загаданного")
        elif number < numberRandom :
            print ("Ваше число меньше загаданного")
        else :
           print("Вы угадали с", counter, "попытки")
           break
        counter +=1


def task2():
    odd = 0
    even = 0
    line = input("Введите строку: ").split(' ')
    for i in range(len(line)):
        if len(line[i]) % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Количество слов с нечетной длиной:", odd, "\nКоличество слов с четной длиной:", even)

def task3():
    first = 0
    indexFirst = 0 
    last = 0
    indexLast = 0
    t = True
    u = True
    repetition = []
    line = input("Введите через пробел элементы списка: ").split(' ')
    print("Элементы, встречающиеся только один раз: ", end='')

    for i in range (len(line)):
        if line.count(line[i]) == 1:
            u = False
            print(line[i], " ",end='')
        if line[i] == "0" and t == True:
            first = int(line[i])
            indexFirst = i
            t = False
        if line[i] == '0' and t == False:
            last = int(line[i])
            indexLast = i

    if u == True: print("Таких элементов нет")

    if t == True:
        print("Нулевых элементов нет")
    elif indexFirst == indexLast:
        print("\nТолько один нулевой элемент")
    else:
        sum = 0
        for i in  range(indexFirst, indexLast):
           sum+=int(line[i])
        print("\nСумма элементов между первым и последним нулевыми элементами равна: ", sum)

def task4():
    dictionary = {}
    while True:
        q = int(input("Введите количество цифр: "))
        if q<0:
            print("Введите положительное число")
        else:
            break
    array = []

    for i in range(q):
        array.append(random.randint(0,9))
    print("Полученная строка", array)

    for num in array:
        dictionary[num] = array.count(num)

    print(dictionary)
    
def task6():    
    line = tuple(input("Введите через пробел элементы кортежа: ").split(' '))
    print("Количество нулевых элементов: ", line.count("0"))

def task5():
    dictionary ={'Маффин' : [["мука", "сахар", "соль","масло", "какао", "яйца", "разрыхдитель", "шоколад", "сахарная пудра"], 2.4, 78],
                 'Торт Наполеон' : [["мука", "сахар", "соль","масло", "молоко", "яйца", "вода"], 4, 947],
                 'Шоколадный фондан' : [["мука", "сахар","масло", "шоколад", "яйца", "какао"], 3.65, 56],
                 'Павлова' : [["Сахарная пудра", "яичные белки", "кукурузный крахмал","лимонный сок", "сливки", "ягоды"], 4.7, 110],
                 'Зефир' : [["Агар-агар", "сахар", "Ванилин","яблоки", "вода"], 1.7, 77]}

    while True:
        operation = int(input(("\nМеню: \n 1) Просмотр описания\n 2)  Просмотр цены\n 3) Просмотр количества\n 4) Всю информацию\n 5) Покупка\n 6) До свидания\n")))
        if operation == 1:
           for d in dictionary:
                print(d, ": ","\n       Состав: ", (dictionary[d][0]))
        elif operation ==2:
            for d in dictionary:
                print(d, (dictionary[d][1]), " руб\n")
        elif operation ==3:
              for d in dictionary:
                print(d, (dictionary[d][2]), " грамм\n")
        elif operation ==4:
             for d in dictionary:
                print(d, ": ","\n       Состав: ", (dictionary[d][0]), "\n       Стоимость: ", (dictionary[d][1]), " руб", "\n       Количество: : ", (dictionary[d][2]), " грамм\n")
        elif operation == 5:
            cost = 0
            p =0
            while True:
                dessert = input("\nВыберите десерт:  ")
                q = int(input("\nВведите количество:  "))
                cost+= float(dictionary[dessert][1]) *q
                print(cost)
                p+=1
                i = int(input("Продолжить? \n 1)Да 2)Нет\n"))
                if i == 2 : 
                    print("Стоимость покупки: ", cost)
                    print("Количество оставшихся товаров в кондитерской: ", (len(dictionary)-p))
                    break
        elif operation == 6:
            print("До свидания")
            break

main()  