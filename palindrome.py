import string

inp_str = input("Enter original string: ")
new_str = inp_str.lower()
bad_char = string.whitespace + string.punctuation

for char in new_str:
    if char in bad_char:
        new_str = new_str.replace(char, " ")

if new_str == new_str[::-1]:
    print(f"String {inp_str} is a palindrome")
else:
    print(f"String {inp_str} is not a palindrome")
