import random
print("Hello reader")
name = input("What is you name? ")
print("Hello " + name)

names = ["mahadi","qwer","dfghgfds","dfgh"]
worker = ["fisherman", "labour","wood cutter"]
marketname = ["sdsds","sdsds","gfgfg","hfgdfgsd"]

randomname = random.choice(names)
randomworker = random.choice(worker)
randommarketname = random.choice(marketname)



story = "once upon a time there lived a man called " + randomname + " . He was a" + randomworker+" . Je every day to the marrket known as"+ randommarketname + "."

print(story)