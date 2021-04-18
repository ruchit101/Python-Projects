# import json
# a ={"name":"harry","salary":9000,"language":"Python"}
# # conversion to JSON done by dumps() function
# b = json.dumps(a)
# print(b) # printing the output



import json

data = '{"var1":"harry", "var2":56,"var3":false}'
print(data) #string
print(type(data))

parsed = json.loads(data) # converts string/json object into Python dictionary
print(parsed)
print(type(parsed))

#Task 1 - json.load? Ans: Json.load() kisi bhi file object #
# ko as an argument leta hai jabki json.loads kisi bhi string ko as an argument leta hai..


data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}

print(type(data2))
jscomp = json.dumps(data2)  # Convert Python Dictionary into JS compatible object
# and dump will convert file object and into JS compatible object
print(jscomp)
print(type(jscomp))

# Task 2 = what is sort_keys parameter in dumps
