import re

with open("04-passport.txt", "r") as file:
    read = file.read().replace("\n", " ")
    read2 = read.replace("  ", "\n")

with open("04-passport_clean.txt", "w") as file_clean:
    file_clean.write(read2)

passports = []
passport = {}
lines = 0
valid = 0
valid_values = 0
check_keys = {"byr", "iyr", "eyr" ,"hgt", "hcl", "ecl", "pid"}
valid_passports = []
valid_passports_values = []

def byr(v):
    x = re.search("^[\d]{4}$", v)

    if x:
        if(int(v) >= 1920) and (int(v) <= 2002):
            return True
        else:
            return False
    else:
        return False

def iyr(v):
    x = re.search("^[\d]{4}$", v)

    if x:
        if (int(v) >= 2010) and (int(v) <= 2020):
            return True
        else:
            return False
    else:
        return False

def eyr(v):
    x = re.search("^[\d]{4}$", v)

    if x:
        if (int(v) >= 2020) and (int(v) <= 2030):
            return True
        else:
            return False
    else:
        return False

def hgt(v):
    x = re.search("^\d+(cm|in)$", v)

    if x:
        num = re.sub("\D", "", v)
        unit = re.sub("\d", "", v)
        if (unit == "cm") and (int(num) >= 150 and int(num) <= 193):
            return True
        elif (unit == "in") and (int(num) >= 59 and int(num) <= 76):
            return True
        else:
            return False
    else:
        return False

def hcl(v):
    x = re.search("^#[0-9a-f]{6}$", v)
    if x:
        return True
    else:
        return False

def ecl(v):
    x = re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", v)
    if x:
        return True
    else:
        return False

def pid(v):
    x = re.search("^\d{9}$", v)
    if x:
        return True
    else:
        return False

def validate(p):
    byr_check = False
    iyr_check = False
    eyr_check = False
    hgt_check = False
    hcl_check = False
    ecl_check = False
    pid_check = False

    for field, value in p.items():
        if (field == "byr"):
            if (byr(value)):
                byr_check=True
        elif (field == "iyr"):
            if (iyr(value)):
                iyr_check=True
        elif (field == "eyr"):
            if (eyr(value)):
                eyr_check=True
        elif (field == "hgt"):
            if (hgt(value)):
                hgt_check=True
        elif (field == "hcl"):
            if (hcl(value)):
                hcl_check=True
        elif (field == "ecl"):
            if (ecl(value)):
                ecl_check=True
        elif (field == "pid"):
            if (pid(value)):
                pid_check=True
    if byr_check and iyr_check and eyr_check and hgt_check and hcl_check and ecl_check and pid_check:
        return True
    else:
        return False

with open("04-passport_clean.txt") as file:
    for line in file:
        lines += 1
        passport_str = line.replace(" ", "\n")
        for item in passport_str.splitlines():
            key, value = item.strip().split(":")
            passport[key] = value
        passports.append(passport.copy())
        passport = {}

for i in passports:
    if all(key in i for key in check_keys):
        valid +=1
        valid_passports.append(i)

for i in valid_passports:
    if validate(i):
        valid_passports_values.append(i)
        valid_values +=1

# for i in valid_passports_values:
#     print(i)

print(lines)
print(valid)
print(valid_values)

