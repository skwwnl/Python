target = int(input()) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total_even = 0
for even in range(2,target + 1, 2):
    print(even)
    total_even += even

print(total_even)