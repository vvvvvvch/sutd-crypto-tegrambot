d = {}

with open("en-ru.txt","r") as file:
    for line in file:
        en_w = line.split("-")[0].strip()
        ru_ws = line.split("-")[1].strip().split(',')
        for i in ru_ws:
            i = i.strip()
            if i in d.keys():
                d[i] = d[i] + ", " + en_w
            else:
                d[i] = en_w

with open("ru-en.txt", "w") as file:
    for i in sorted(d.keys()):
        file.writelines(f"{i} - {d[i]}\n")

