shopping_list = []

while True:
    item = input("Add an item (type 'done' to finish): ")

    if item.lower() == "done":
        break

    shopping_list.append(item)

print("\nYour shopping list:")
for i in shopping_list:
    print("-", i)