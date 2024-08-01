# Task 1 - Age Assignments Based on the Riddle

Anton: int = 21
Beth: int = Anton + 6
Chen: int = Beth + 20
Drew: int = Chen + Anton
Ethan: int = Chen

print('Task 1 - Age Assignments Based on the Riddle\n')
print(f"Anton is {Anton}")
print(f"Beth is {Beth}")
print(f"Chen is {Chen}")
print(f"Drew is {Drew}")
print(f"Ethan is {Ethan}")
print('------------------------------------------------------------\n\n')

# Task 2 - Formatted String Interpolation

name: str = "Alice"
age: int = 30
city: str = "New York"

print('Task 2 - Formatted String Interpolation\n')
print(f"{name} is {age} years old and lives in {city}")
print('------------------------------------------------------------\n\n')

# Task 3 - String Manipulation

s: str = "hEllo WoRlD"
print(f'Task 3 - String Manipulation - {s}\n')
print(f"Capitalize - {s.capitalize()}")
print(f"Uppercase - {s.upper()}")
print(f"Lowercase - {s.lower()}")

print('------------------------------------------------------------\n\n')

# Task 4 - Substring Search

s: str = "the quick brown fox jumps over the lazy dog"

print(f'Task 4 - Substring Search - {s}\n')
print(f"index of 'fox' is {s.index('fox')}")
print(f"'the' appears {s.count('the')} times")

print('------------------------------------------------------------\n\n')

# Task 5 - String Replacement

s: str = "I love programming in Python"

print(f'Task 5 - String Replacement - {s}\n')
print(f"{s.replace('Python', 'Java')}")

print('------------------------------------------------------------\n\n')

# Task 6 - String Splitting and Joining

s: str = "apple,banana,cherry,dates"

print(f'Task 6 - String Splitting and Joining - {s}\n')
split: list[str] = s.split(',')
print(split)
print(' '.join(split))

print('------------------------------------------------------------\n\n')

# Task 7 - String Stripping and Justifying

s: str = "   Python is fun!   "
print(f'Task 7 - String Stripping and Justifying - {s}\n')
print(s.strip())
print(s.strip().ljust(20, '*'))
print(s.strip().rjust(20, '*'))

print('------------------------------------------------------------\n\n')

# Task 8 - Convert an integer to its binary representation

num: int = 45

print(f'Task 8 - Convert an integer to its binary representation\n')
print(f"Binary representation: {bin(num)}")

print('------------------------------------------------------------\n\n')

# Task 9 - Calculate Powers of Numbers.

base: int = 3
exponent: int = 4

power_result = base ** exponent


print(f'Task 9 - Calculate Powers of Numbers\n')
print("Power result:", power_result)

print('------------------------------------------------------------\n\n')

# Task 10 - Round floating-point numbers

value: float = 12.34567

print(f'Task 10 - Round floating-point numbers\n')

print("Rounded to nearest integer:", round(value))
print("Rounded to two decimal places:", round(value, 2))

print('------------------------------------------------------------\n\n')
