def inventory_analyzer():
    print("Welcome to Inventory List Analyzer!\n")
    items = []

    while True:
        item_name = input("Enter item name: ").strip().title()
        item_category = input("Enter category: ").strip().lower()
        quantity = int(input("Enter quantity: "))

        items.append({
            'name': item_name,
            'category': item_category,
            'quantity': quantity
        })

        cont = input("Do you want to add more items? (y/n): ").lower()
        if cont != 'y':
            break

    print("\n========== INVENTORY SUMMARY ==========")

    total_items = len(items)
    item_names = [item['name'] for item in items]
    print(f"\nTotal Different Items: {total_items}")
    print(f"Explanation: You entered {total_items} different items: {', '.join(item_names)}.")

    total_quantity = sum(item['quantity'] for item in items)
    quantities = " + ".join(str(item['quantity']) for item in items)
    print(f"\nTotal Quantity in Stock: {total_quantity}")
    print(f"Explanation: Sum of all quantities: {quantities} = {total_quantity}")

    average = total_quantity / total_items
    print(f"\nAverage Quantity per Item: {average:.2f}")
    print(f"Explanation: Average = {total_quantity} total / {total_items} items")

    most_stocked = max(items, key=lambda x: x['quantity'])
    least_stocked = min(items, key=lambda x: x['quantity'])

    print(f"\nMost Stocked Item: {most_stocked['name']} ({most_stocked['quantity']} units)")
    print(f"Explanation: {most_stocked['name']} has the highest quantity.")

    print(f"\nLeast Stocked Item: {least_stocked['name']} ({least_stocked['quantity']} units)")
    print(f"Explanation: {least_stocked['name']} has the lowest quantity.")

    categories = {item['category'] for item in items}
    print(f"\nUnique Categories in Inventory: {categories}")
    print("Explanation: Categories are taken from user input and duplicates are removed.")

    sorted_items = sorted(items, key=lambda x: x['quantity'], reverse=True)
    print("\nItems Sorted by Quantity (High to Low):")
    for idx, item in enumerate(sorted_items, 1):
        print(f"{idx}. {item['name']} - {item['quantity']} units")
    print("Explanation: Items are shown from highest to lowest quantity.")

    sorted_categories = sorted(categories)
    print("\nCategories in Alphabetical Order:")
    for idx, cat in enumerate(sorted_categories, 1):
        print(f"{idx}. {cat}")
    print("Explanation: Categories sorted alphabetically for clean display.")

    print("\n========== END OF REPORT ==========")


inventory_analyzer()

'''
Welcome to Inventory List Analyzer!

Enter item name: pen
Enter category: stationary
Enter quantity: 50
Do you want to add more items? (y/n): y
Enter item name: pencil
Enter category: stationary
Enter quantity: 50
Do you want to add more items? (y/n): y
Enter item name: notebook
Enter category: stationary
Enter quantity: 50
Do you want to add more items? (y/n): n

========== INVENTORY SUMMARY ==========

Total Different Items: 3
Explanation: You entered 3 different items: Pen, Pencil, Notebook.

Total Quantity in Stock: 150
Explanation: Sum of all quantities: 50 + 50 + 50 = 150

Average Quantity per Item: 50.00
Explanation: Average = 150 total / 3 items

Most Stocked Item: Pen (50 units)
Explanation: Pen has the highest quantity.

Least Stocked Item: Pen (50 units)
Explanation: Pen has the lowest quantity.

Unique Categories in Inventory: {'stationary'}
Explanation: Categories are taken from user input and duplicates are removed.

Items Sorted by Quantity (High to Low):
1. Pen - 50 units
2. Pencil - 50 units
3. Notebook - 50 units
Explanation: Items are shown from highest to lowest quantity.

Categories in Alphabetical Order:
1. stationary
Explanation: Categories sorted alphabetically for clean display.

========== END OF REPORT ==========
'''
