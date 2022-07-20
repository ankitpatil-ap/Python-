name = "tony stark"

print(name.upper())
#TONY STARK
print(name)
#tony stark    ie it does not change the original string just print the layout which we offer

print(name.find('a'))
#7
print(name.replace("tony stark", "IronMan"))
#IronMan
print(name.replace("stark", "shark"))
#tony shark
print("t" in name)
#True