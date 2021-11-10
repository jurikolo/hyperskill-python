# Gather user input
print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
beans = int(input())
print("Write how many cups of coffee you will need:")
cups_required = int(input())

# Process
water_cups = water // 200
milk_cups = milk // 50
beans_cups = beans // 15
max_cups = min(water_cups, milk_cups, beans_cups)
if max_cups == cups_required:
    print("Yes, I can make that amount of coffee")
elif max_cups > cups_required:
    print("Yes, I can make that amount of coffee (and even", max_cups - cups_required, "more than that)")
else:
    print("No, I can make only", max_cups, "cups of coffee")

# print(cups_required * 200, "ml of water")
# print(cups_required * 50, "ml of milk")
# print(cups_required * 15, "g of coffee beans")