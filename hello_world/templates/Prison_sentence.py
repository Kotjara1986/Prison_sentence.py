
print("ВЕЧЕР В ХАТУ УВАЖАЕМЫЙ АРЕСТАНТ!")
print("Я УМНАЯ ПРОГРАММА, КОТОРАЯ МОЖЕТ СКОНВЕРТИРОВАТЬ ТВОЙ СРОК КАК ТЫ ХОЧЕШЬ!")
my_sentence = int(input("Введи пожалуйста количество лет: "))
my_sentence2 = int(input("Введите количество месяцев: "))
print("Выбери единицу конвертации:")
print("1.секунды", "2.минуты", "3.часы", "4.дни", "5.недели", "6.месяца", sep="\n")
menu_number = int(input("Введите номер меню: "))

def seconds(*args):
    global my_sentence
    global my_sentence2
    result = (my_sentence * 365) * 24 * 60 * 60
    result2 = (my_sentence2 * 30) * 24 * 60 * 60
    return result + result2

def minutes(*args):
    global my_sentence
    global my_sentence2
    result = (my_sentence * 365) * 24 * 60
    result2 = (my_sentence2 * 30) * 24 * 60
    return result + result2

def hours(*args):
    global my_sentence
    global my_sentence2
    result = (my_sentence * 365) * 24 
    result2 = (my_sentence2 * 30) * 24 
    return result + result2

def days(*args):
    global my_sentence
    global my_sentence2
    result = (my_sentence * 365)
    result2 = (my_sentence2 * 30)
    return result + result2

def weeks(*args):
    global my_sentence
    global my_sentence2
    result = (my_sentence * 365) // 7
    result2 = (my_sentence2 * 30) // 7
    return result + result2

def month(*args):
    global my_sentence
    global my_sentence2
    result = (my_sentence * 365) // 30
    result2 = my_sentence2
    return result + result2

if menu_number == 1:
    output = seconds()
    print("Ваш срок в секундах состовляет", output, "с")
elif menu_number == 2:
    output2 = minutes()
    print("Ваш срок в минутах состовляет", output2, "мин")
elif menu_number == 3:
    output3 = hours()
    print("Ваш срок в часах состовляет", output3, "ч")
elif menu_number == 4:
    output4 = days()
    print("Ваш срок в днях состовляет", output4, "д")
elif menu_number == 5:
    output5 = weeks()
    print("Ваш срок в неделях состовляет", output5, "нед")
else:
    output6 = month()
    print("Ваш срок в месяцах состовляет", output6, "мес")
