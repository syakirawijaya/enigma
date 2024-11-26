import random
from datetime import date

randomnum = random.randint(00000,99999)
keylist = {}

keylist["A"] = randomnum[0,2]
keylist["B"] = randomnum[1,3]
keylist["C"] = randomnum[2,4]
keylist["D"] = randomnum[3,]

date = date.today
offset = date.strftime("%d%m%Y")
