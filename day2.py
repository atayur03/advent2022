print("start")
print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

total_score = 0
for el in contents:
    opp = el[0:1]
    me = el[2:3]
    if me == "X":
        total_score = total_score + 0
        if opp == "A":
            total_score = total_score + 3
        elif opp == "B":
            total_score = total_score + 1
        elif opp == "C":
            total_score = total_score + 2
    elif me == "Y":
        total_score = total_score + 3
        if opp == "A":
            total_score = total_score + 1
        elif opp == "B":
            total_score = total_score + 2
        elif opp == "C":
            total_score = total_score + 3
    elif me == "Z":
        total_score = total_score + 6
        if opp == "A":
            total_score = total_score + 2
        elif opp == "B":
            total_score = total_score + 3
        elif opp == "C":
            total_score = total_score + 1
    else:
        total_score / 0
print(total_score)
