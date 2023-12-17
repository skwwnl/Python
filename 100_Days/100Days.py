size = input()
ex_pep = input()
ex_che = input()
bill = 0

def pep(size, a):
    if size == "S":
        return a + 2
    else:
        return a + 3

def cheese(b):
    return b + 1


# main code
if size == "S":
    bill += 15
    if ex_pep == "Y":
        bill = pep(size, bill)
    if ex_che == "Y":
        bill = cheese(bill)
    print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
if size == "M":
    bill += 20
    if ex_pep == "Y":
        bill = pep(size, bill)
    if ex_che == "Y":
        bill = cheese(bill)
    print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")
if size == "L":
    bill += 25
    if ex_pep == "Y":
        bill = pep(size, bill)
    if ex_che == "Y":
        bill = cheese(bill)
    print(f"Thank you for choosing Python Pizza Deliveries!\nYour final bill is: ${bill}")