number = int(input())
num = number
rev = 0
while num > 0:
    rem = num%10
    rev = rev*10 + rem
    num //= 10

print("Reverse of ", number, " : ", rev, " num value : ", num)