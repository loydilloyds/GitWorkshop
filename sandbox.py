def isPalindrome(num : str) -> bool :
    n = len(num)
    for i in range(0, n // 2):
        if num[i] != num[n - i - 1]:
            return False

    return True

x = 585
numBase2 = bin(x)[2:] 

sum = 0
for i in range(1, 1000000):
    if isPalindrome(str(i)) and isPalindrome(bin(i)[2:]):
        sum = sum + i

print(sum)
