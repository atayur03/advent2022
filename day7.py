print("start")
print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

commands = contents

dirs = {"/home": 0}
path = "/home"

# Process every command
for command in commands:
    # Commands that start with $
    if command[0] == "$":
        # Do nothing
        if command[2:4] == "ls":
            pass
        # Manage changing the path
        elif command[2:4] == "cd":
            # # Go back to the root
            if command[5:6] == "/":
                path = "/home"
            # Go back in the path
            elif command[5:7] == "..":
                path = path[0:path.rfind("/")]
            # Change the path
            else:
                dir_name = command[5:]
                path = path + "/" + dir_name
                dirs.update({path: 0})
    # Do nothing when listing directories available
    elif command[0:3] == "dir":
        pass

    else:
        size = int(command[:command.find(" ")])
        dir = path
        for i in range(path.count("/")):
            dirs[dir] += size
            dir = dir[:dir.rfind("/")]


total = 0

limit = 30000000 - (70000000 - dirs["/home"])
valid_dirs = []


for dir in dirs:

    if dirs[dir] < 100000:
        total = total + dirs[dir]

    if limit <= dirs[dir]:
        valid_dirs.append(dirs[dir])

smallest = min(valid_dirs)

print("Answer to part 1: ", total)
print("Answer to part 2: ", smallest)
