## sort()
## list의 재구성된 동일 값 반환
numbers = [4, 6, 2, 7, 1]
numbers.sort()
print(numbers)

## sorted()
## list의 새 목록을 반환
names = ["Carlos", "Ray", "Alex", "Kelly"]
print(names)
print(sorted(names))
print(names)

## 정렬 Key
print(sorted(names, key=len))