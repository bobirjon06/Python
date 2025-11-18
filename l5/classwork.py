# # #1
# # n = int(input())
# #
# # dictionary = {}
# # for i in range(0, n):
# #     name = input("Ism: ")
# #     age = int(input("Age: "))
# #     dictionary[name] = age
# # print(dictionary)
#
# #2
#
# lugat = {
#     "car": "moshina",
#     "rabbit": "quyon",
#     "student": "talaba"
# }
# a = input("Inglizcha so'z kiriting: ")
# print(lugat.get(a, "not found"))

lugat = {
    "car": "moshina",
    "rabbit": "quyon",
    "student": "talaba"
}

tanlov = int(input("""
Tanlang:
    1. en -> uz
    2. uz -> en
""")
)
if tanlov == 1:
    en = input("Inglizcha so'z kiriting:")
    print(lugat.get(en, "Bunday so'z bazada yo'q"))
elif tanlov == 2:
    uz = input("O'zbekcha so'z kiriting:")
    for k, v in lugat.items():
        if uz ==v:
            print(k)
            break
    else:
        print("not found")
