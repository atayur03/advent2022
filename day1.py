print("start")
print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

max_cals = 0
snd_cals = 0
trd_cals = 0
count = 0
for el in contents:
    if el != "":
        count = count + int(el)
    else:
        if count > max_cals:
            trd_cals = snd_cals
            snd_cals = max_cals
            max_cals = count
        elif count > snd_cals:
            trd_cals = snd_cals
            snd_cals = count
        elif count > trd_cals:
            trd_cals = count
        count = 0
print(max_cals + snd_cals+trd_cals)
