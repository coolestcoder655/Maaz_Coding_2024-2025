# file = open("demo.txt", "a")

# file.write("\nhi")
# file.close()

# with open("demo.txt", "r+") as file:
#     data = file.read()

# print(data)

# with open("demo.txt", "w") as file:
#     file.write("Hello.")


with open("practice.txt", "w") as file:
    file.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")

def wordReplacing(toFind, toReplace, fileName):
    
    return None

with open("practice.txt", "r") as file:
        data = file.read()

data = data.replace("Java", "Python")
write = open("practice.txt", "w")
write.write(data)
write.close()


"""
with open("practice.txt", "r") as file:
    data = file.read()
    exists = data.find("learning")
    if exists == -1:
        print("learning is not in the file")
    else:
        print("learning is in the file")

with open("practice.txt") as file:
    print(file.read())
"""