import json

with open("1.json","r") as file:
    data = json.load(file)

for i in data["products"]:
    print("Название: ", i["name"])
    print("Цена: ", i["price"])
    print("Вес: ", i["weight"])
    print("В наличии" if i["available"] else "Нет в наличии!","\n")
