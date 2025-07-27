# Step 1: Define the binary inputs
A = 0b1 # A = 1
B = 0b0 # B = 0
C = 0b1 # C = 1

# Step 2: Perform logic gate operations as described

# First AND gate: A AND B
AND1 = A & B # 1 & 0 = 0

# Second AND gate: B AND C
AND2 = B & C # 0 & 1 = 0

# First OR gate: OR of both AND outputs
OR1 = AND1 | AND2 # 0 | 0 = 0

# NOT gate: Negate C (invert bits and mask to 1 bit)
NOT_C = ~C & 0b1 # ~1 = -2 → masked = 0

# Third AND gate: A AND NOT C
AND3 = A & NOT_C # 1 & 0 = 0

# Final OR gate: Combine last AND with previous OR
Q = AND3 | OR1 # 0 | 0 = 0

# Step 3: Display the result
print(f"The output Q is: {Q}")





light = input("Enter 1 to turn ON the light, 0 to turn it off:")

if light == "1":
    print("💡💡Light is on.")
elif light == "0":
    print("🌑 Light is off.")
else:
    print("Only 1 or 0 is allowed!")



number = int(input("Enter a number: "))

# Bitwise And with 1 checks the last bit
if number & 1:
    print(f"{number} is odd! 😲")
else:
    print(f"{number} is even!")




number = int(input("Enter a number: "))

# Convert number to binary
binary = bin(number)[2:]

# Count 0s and 1s
zeros = binary.count("0")
ones = binary.count("1")

# Show results
print(f"\nBinary of {number} is: {binary}")
print(f"Number of 1s: {ones}")
print(f"Number of 0s: {zeros}")
