phrase = "Don't panic!" 
plist = list(phrase) 
print(phrase)  
print(plist) 

new_plist = plist[1:8:1]
new_plist.remove("'")
new_plist.insert(2, new_plist.pop(3))
new_plist.extend([new_plist.pop(), new_plist.pop()])

new_phrase = ''.join(new_plist)
print(new_plist) 
print(new_phrase)