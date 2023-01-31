import random

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
number = "01234567890"
symbols = "!~`@#$%^&*_"

Use = lower_case + upper_case + number + symbols
length = 10

password = "".join(random.sample(Use, length))

print("Your password is:" + password)
