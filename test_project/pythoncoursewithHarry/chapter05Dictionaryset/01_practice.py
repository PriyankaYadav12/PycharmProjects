dict = {
    "bottle": "plastic",
    "steel": "Dishes",
    "glass": "Mirror",
    "wire": "aluminium"
}
# for x, y in dict.items():
# print(x, ":=", y)

key = input("enter the key\n")
if(dict.get(key)== None):
    print("value not found")
else:
    print("the value corresponding to your key is:", dict.get(key))