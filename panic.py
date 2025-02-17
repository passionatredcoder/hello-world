phrase  ="Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist2 = plist.copy()

for num in range(4):
    plist2.pop()

plist2.insert(4,plist2.pop(5))
plist2.insert(6, plist2.pop(7))
plist2.remove('D')
plist2.remove("'")
print(plist2)

new_phrase = ''.join(plist2)
print(new_phrase)