name1 = input("Enter the First name: ")
name1_formatted = name1.strip().capitalize()
name2 = input("Enter the second name: ")
name2_formatted = name2.strip().capitalize()
name3 = input("Enter the third name: ")
name3_formatted = name3.strip().capitalize()
print(f"The three names are: {name1_formatted}, {name2_formatted} & {name3_formatted}")

x = input("Give me a number to multiply by 10: ")
print(x * 10)

x = input("Give me a number to multiply by 10: ")
print(int(x) * 10)

x = input("Give me a number to multiply by 10: ").replace(",", "").replace(".", "")
print(int(x) * 10)