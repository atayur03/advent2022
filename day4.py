print("start")
print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

count = 0
for row in contents:
    assignments = row.split(",")
    elf1 = assignments[0].split("-")
    elf2 = assignments[1].split("-")
    if int(elf1[0]) <= int(elf2[1]) and int(elf1[1]) >= int(elf2[0]):
        count = count+1
print(count)
