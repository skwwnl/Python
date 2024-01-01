line1 = ["1", "2", "3"]
line2 = ["4", "5", "6"]
line3 = ["7", "8", "9"]

map = [line1, line2, line3]
position = input()

letter = position[0].lower()
abc  = ["a", "b", "c"]
letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[number_index][letter_index] = "X"


print(f"{line1}\n{line2}\n{line3}")