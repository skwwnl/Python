T = int(input())

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


for _ in range(T):
    i = list(map(int, input().split(" ")))
    if leap_year(i[0]) == True and i[1] == 3:
        print(f"{i[0]} 2 29")
    elif i[1] == 1:
        print(f"{i[0]-1} 12 31")
    else:
        print(f"{i[0]} {i[1]-1} {days[i[1]-2]}")
