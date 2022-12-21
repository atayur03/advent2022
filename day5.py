print("start")
print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)


def move(lst, st, en):
    el = lst[st-1].pop()
    lst[en-1].append(el)
    return lst


def move1(lst, st, en, num):
    st_len = len(lst[st-1])
    els = lst[st-1][-num:]
    lst[en-1] = lst[en-1]+els
    lst[st-1] = lst[st-1][:-num]
    return lst


init_lst = [
    ["N", "R", "G", "P"],
    ["J", "T", "B", "L", "F", "G", "D", "C"],
    ["M", "S", "V"],
    ["L", "S", "R", "C", "Z", "P"],
    ["P", "S", "L", "V", "C", "W", "D", "Q"],
    ["C", "T", "N", "W", "D", "M", "S"],
    ["H", "D", "G", "W", "P"],
    ["Z", "L", "P", "H", "S", "C", "M", "V"],
    ["R", "P", "F", "L", "W", "G", "Z"]
]

lst = init_lst
for row in contents:
    parsed = row.split(" ")
    lst = move1(lst, int(parsed[3]), int(parsed[5]), int(parsed[1]))


print(lst)
for el in lst:
    print(el.pop())
