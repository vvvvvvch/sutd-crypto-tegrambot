import random

students = {"Иванов", "Петров", "Смирнов", "Сидоров", "Васильев", "Кузнецов", "Попов", "Федоров", "Лебедев", "Семенов"}
languages = {"Русский", "Английский", "Французский", "Немецкий", "Китайский"}

lang_stud = {}

for st in students:
    kolvo = random.randint(1,3)
    lang_stud[st] = random.sample(list(languages), kolvo)

unique_lang = set()
for i in lang_stud:
    unique_lang = unique_lang.union(set(lang_stud[i]))

# print(lang_stud)
print("Множество различных языков, которые знают студенты: ", sorted(unique_lang), f" ({len(unique_lang)})")

china = [i for i in lang_stud if "Китайский" in lang_stud[i]]
print("Студенты, знающие китайский: ", china)

