import random
#随机值的浮点值0---1
random.random()
#随机整数[1, 4]
print(random.randint(1, 4))
#随机[1, 4)
print(random.randrange(1, 4))
#随机
print(random.choice("hello"))
print(random.choice([1, 3, 4]))
#随机取3位
print(random.sample("hello", 3))
#随机
print(random.uniform(1, 3))
#洗牌
l = [1, 2, 3, 4, 5]
random.shuffle(l)
print(l)


checkcode = ""

for i in range(4):
    current = random.randint(0, 1)
    char = ""
    if current:
        char = random.randint(0, 9)

    else:
        char_num = random.randint(65, 90)
        char = chr(char_num)

    checkcode += str(char)


print(checkcode)


