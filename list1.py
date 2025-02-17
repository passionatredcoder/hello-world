phrase = "Don't panic!"
plist1 = list(phrase)
print(phrase)
print(plist1)
#find length of list
print(len(plist1))
#to copy objects of existing list to another one
plist2 = plist1.copy()


#to add an object to existing list
plist2.append(1)
plist2.remove('D')
new_list = []
for num in range(4):
    new_list.append(plist2.pop(5))

new_list.insert(2, "Himanshu")

plist2.extend(new_list)
print(plist2)

