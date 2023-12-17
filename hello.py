f1 = open('pro.txt', 'r')
body = f1.readlines()
f1.close()

print(body)
f3 = open('pro.txt', 'w')
for line in body:
    if "java" in line:
        body = line.replace("java", "python")
        f3.write(body)
        print(body)

    else:
        body = line
        f3.write(body)
        print(body)
f3.close()
# body = body.replac`z`
# f1 = open('pro.txt', 'w')
# f1.write(body)
# f1.close()
