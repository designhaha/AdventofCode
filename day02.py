import re

passwords = []
valid_passwords = 0

with open("data.txt") as file:
    for line in file:
        passwords.append(line.replace("\n", ""))

# for password in passwords:
#     check = re.match(r"(?P<num1>\d+)-(?P<num2>\d+) (?P<contains>\w): (?P<password>\w+)", password)
#     amount = re.findall(rf"{check.group('contains')}", check.group('password'))
#     if (len(amount) >= int(check.group('num1'))) and (len(amount) <= int(check.group('num2'))):
#         valid_passwords += 1
#         print(password)
#         print("valid")
#     else:
#         print(password)
#         print("invalid")

for password in passwords:
    check = re.match(r"(?P<num1>\d+)-(?P<num2>\d+) (?P<contains>\w): (?P<password>\w+)", password)
    password_str = check.group('password')
    letter = check.group('contains')
    char1 = password_str[int(check.group('num1'))-1]
    char2 = password_str[int(check.group('num2'))-1]

    if (char1 == letter or char2 == letter) and (char1 != char2):
        valid_passwords +=1
        print(f"{letter}: {password_str} {char1} {char2}")

print(len(passwords))

print(valid_passwords)
