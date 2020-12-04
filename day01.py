import re

num_array = []
sum_array = []
num1 = 0
num2 = 0
num3 = 0
multiply = 0

with open("data.txt") as file:
    for line in file:
        num_array.append(int(line))

# for i in num_array:
#     for x in num_array:
#         if (num_array.index(i) != num_array.index(x)):
#             sum_array.append(i+x)
#             if (i+x == 2020):
#                 num1 = i
#                 num2 = x

for x in num_array:
    for y in num_array:
        for z in num_array:
            if (num_array.index(x) != num_array.index(y)) and (num_array.index(x) != num_array.index(z)):
                if (x+y+z == 2020):
                    num1 = x
                    num2 = y
                    num3 = z

print(f"{num1} + {num2} + {num3}= 2020")
print(f"num1 mulitply by num2 and num3 = {num1*num2*num3}")


