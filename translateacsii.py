str_a = input("Enter a string: ")
newstr = ''
for i in str_a:
    if i.isalpha():
        s = chr(ord(i) - 2)
        newstr += s
    else:
        newstr += i
print(newstr)
