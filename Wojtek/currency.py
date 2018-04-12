from urllib import request as rq
import json

cred = 100
data = 0

x = rq.urlopen("http://api.fixer.io/latest")
curr = json.load(x)
print('actual for: ', curr['date'])

for i in curr['rates']:
    value = cred * curr['rates'][i]
    print("you can buy %.2f" % value, i)
