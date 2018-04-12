from urllib.request import urlopen
import json

def print_all_values(data):
    #zamienia string w słownik
    the_json = json.loads(data)
    print("Wszystkie waluty")
    print(the_json["rates"])

def calculate(data):
    EUR = 100
    the_json = json.loads(data)
    for k in (the_json["rates"]):
        print(EUR/the_json["rates"][k], [k])


url_data = 'http://api.fixer.io/latest'
web_url = urlopen(url_data)
print(web_url.getcode())
if web_url.getcode() == 200:
    data = web_url.read()
print_all_values(data)
calculate(data)
