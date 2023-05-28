import json

k = int(input("Введите количество товаров для добавления: "))

products = {"products":[]}
for i in range(k):
    name = input("Название: ")
    price = int(input("Цена: "))
    weight = int(input("Вес: "))
    available = bool(input("В наличии 0/1: "))
    products["products"].append({"name":name,"price":price,"weight":weight,"available":available})

with open("1.json","r") as file:
    data = json.load(file)

data["products"].extend(products["products"])

for i in data["products"]:
    print("Название: ", i["name"])
    print("Цена: ", i["price"])
    print("Вес: ", i["weight"])
    print("В наличии" if i["available"] else "Нет в наличии!","\n")



with open("1.json","w") as file:
    json.dump(data, file, indent=4,ensure_ascii=False)