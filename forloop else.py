khana=["roti","dal","chawal"]

a=input("Search Food: ")
for i in khana:
    if i==a.lower():
        print(f" {a} found")
        break
else:
    print("Not found!")