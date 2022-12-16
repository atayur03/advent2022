def get_priority(p):
    asci = ord(p)
    if asci >= 65 and asci <= 90:
        return (asci - 38)
    elif asci >= 97 and asci <= 122:
        return asci - 96
    else:
        return 0


def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


print("start")
print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

i = int(0)
total = 0
while i < len(contents):
    fstlst = contents[i]
    sndlst = contents[i+1]
    trdlst = contents[i+2]
    inter = intersection(fstlst, sndlst)
    inter1 = intersection(inter, trdlst)
    total = total + get_priority(inter1[0])
    i = i + 3

print(total)
