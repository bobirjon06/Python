f = open("students.txt")
lst = list()
count = 0
while True:
    {print("""
    --- Talabalar Ro'yxati Dasturi ---
    1. Talaba qo‘shish
    2. Talabalarni ko‘rish
    3. Talaba ma’lumotini yangilash
    4. Talabani o‘chirish
    5. Chiqish
    Tanlang:
    """)}
    choice = int(input())
    # print(choice)
    # count = 0
    match choice:
        case 1:
            f = open("students.txt", "a")
            name = input("Ism: ")
            age = int(input("Yosh: "))
            kurs = input("Kurs: ")
            temp = [count, name, age, kurs]
            lst.append(temp)
            f.write(str(lst[count][0]) + ": " + str(lst[count][1]) + " | " + str(lst[count][2]) + "| " + str(lst[count][3]) + "\n")
            f.close()
            count += 1
        case 2:
            f = open("students.txt", "r")
            txt = f.read()
            print(txt)
            f.close()
        case 3:
            f = open("students.txt", "w")
            a = int(input("Yangilanadigan talaba IDsi: "))
            name = input("Ism: ")
            age = int(input("Yosh: "))
            kurs = input("Kurs: ")
            lst[a][1] = name
            lst[a][2] = age
            lst[a][3] = kurs
            for i in range(len(lst)):
                f.write(str(lst[i][0]) + ": " + str(lst[i][1]) + " | " + str(lst[i][2]) + "| " + str(lst[i][3]) + "\n")
            f.close()
        case 4:
            f = open("students.txt", "w")
            a = int(input("O'chirish uchun ID kiriting: "))
            for i in lst:
                if i[0] == a:
                    lst.remove(i)
            for i in range(len(lst)):
                f.write(str(lst[i][0]) + ": " + str(lst[i][1]) + " | " + str(lst[i][2]) + "| " + str(lst[i][3]) + "\n")
            f.close()
        case 5:
            break