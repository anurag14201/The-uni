def Largest_Smallest_digit(n):
    largest_digit = 0
    smallest_digit = 9
    while (n):
        digit = n % 10
        # largest digit
        largest_digit = max(digit, largest_digit)
        # smallest digit
        smallest_digit = min(digit, smallest_digit)
        n = n // 10
    return largest_digit, smallest_digit


n = 9999990
print("Original Number:", n)
result = Largest_Smallest_digit(n)
print("Largest Digit of the said number:", result[0])
