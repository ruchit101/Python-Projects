import pickle
import requests

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

# When we use requests module
# 1. Get URL to pull request
# 2. Get response contains the server's response to the HTTP request and that will return response object
# and we can check the status of the response using status_code(200: Ok,404:Error,etc.)
# 3. response.text returns the content of the response, in unicode. We get the exact content
# 4. Then use the usual python like readlines and all.

respons = requests.get(url)
respons_text = respons.text
print(respons_text)
data = respons_text.splitlines()
# print(data[0:2])

red = [[i] for i in data]
print("_________________________")
print(red[0:2])

# pickling the python object
fileobj = open('irisData.pkl', 'wb')
pickle.dump(red, fileobj)
fileobj.close()

# Reading Of Pickle file
fileobj = open('irisData.pkl', 'rb')
data = pickle.load(fileobj)
print(data)
