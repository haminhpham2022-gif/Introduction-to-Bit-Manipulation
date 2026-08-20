n = int(input("Enter a number (Try 5 or 12): "))
guess = input("Guess its binary: ")

input("Binary.   Press Enter")
print(f"   decimal {n} -> binary {bin(n)[2:]}")
print(f"   your guess: {guess}")

input("AND – both bits must be 1.   Press Enter")
print(f"   12 = {bin(12)[2:]}")
print(f"   10 = {bin(10)[2:]}")
print(f"   12 + 10 = {12 & 10}")

input("OR – atleast one bit must be 1.   Press Enter")
print(f"   12 | 10 = {12 | 10}")

input("Shifting – move bits left and right.   Press Enter")
print(f"   5 = {bin(5)[2:]}")
print(f"   5 << 1 = {5 << 1} -> {bin(5 << 1)[2:]} (shift left by one = multiply by two)")
print(f"   5 >> 1 = {5 >> 1} -> {bin(5 >> 1)[2:]} (shift right by one = divide by two)")
print(f"   5 << 2 = {5 << 2} -> {bin(5 << 2)[2:]} (shift left by two = multiply by four)")
print(f"   5 >> 2 = {5 >> 2} -> {bin(5 >> 2)[2:]} (shift right by two = divide by four)")