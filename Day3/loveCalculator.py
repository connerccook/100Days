print("Welcome to the Love Calculator")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

name1_count = 0
name2_count = 0
combined_name = name1 + name2

name1_count += combined_name.count('l')
name1_count += combined_name.count('o')
name1_count += combined_name.count('v')
name1_count += combined_name.count('e')
name2_count += combined_name.count('t')
name2_count += combined_name.count('r')
name2_count += combined_name.count('u')
name2_count += combined_name.count('e')

love_count = name1_count * 10 + name2_count

print(f"You are {love_count}% compatible")
