
def T6_1():
    dict = {
        "Algeria" : "Algiers",
        "Albania" : "Tirana ",
        "Andorra" : "Andorra la Vella",
        "Angola" : "Luanda",
        "Antigua and Barbuda" : "Saint John's",
        "Argentina" : "Buenos Aires",
        "Armenia" : "Yerevan",
        "Australia" : "Canberra",
        "Austria" : "Vienna",
        "Azerbaijan" : "Baku",
    }

    for key, value in dict.items():
        print(key, value)

    cnt = input("Country is ")
    print(f"Capital is {dict[cnt]}")

    sortedDict = dict(sorted(dict.items(), key=lambda x: x[0].lower()) )

    print(sortedDict)

def T6_2():
    alp = {
        "авеинорст" : 1,
        "дклмпу" : 2,
        "бгёья" : 3,
        "йы" : 4,
        "жзхцч" : 5,
        "шэю" : 8,
        "фщъ" : 10
    }
    sum = 0
    word = input()

    for i in word:
        for key, value in alp.items():
            if i in key:
                sum += value
    
    print(sum)

def T6_3():
    # stud = {"Mikel", "Tomas", "Joel", "Nikel", "Hellen", "Richard", "Pam", "Jim", "Ray"}
    stud = {"Mikel", "Tomas", "Jo"}
    studBase = {'name' : {'cLang' : 1, 'langs' : []}}
    languages = set()
    setOfChineseAgents = set()
    for i in stud:
        cLang = int(input(f"How many languages does {i} know? "))
        studBase[i] = {}
        studBase[i]['cLang'] = cLang
        studBase[i]['langs'] = []
        for x in range(cLang):
            lang = input(f"{i} knows ").lower()
            studBase[i]['langs'].append(lang)
            if lang not in languages:
                languages.add(lang)
            if lang == "chinese":
                setOfChineseAgents.add(i)
        print(f"{i} knows {studBase[i]['cLang']} langs and it {sorted(studBase[i]['langs'])}")
    print(f'{len(setOfChineseAgents)} student know chinese and it {setOfChineseAgents}')
    print(f"all languages that students know {sorted(languages)}")
T6_3()
