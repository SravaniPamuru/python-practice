group=[1,2,3,4]
search= int(input("enter the element in search:"))
for element in group:
    if search==element:
        print("element found in group")
        break
    else:
        print("element not found")
