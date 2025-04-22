# Subscripting
print("Hello"[0])

# String
print("123" + "345")

# Integer = Whole number
print(123 + 345)

# Large Intergers
print(123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)

# TypeError Exception
try:
    print(len(123))
except TypeError:
    print("Exception: O tipo informado é inválido")

# Type of data
print(type("Hello"))
print(type(123))
print(type(123_456_789))
print(type(3.14159))
print(type(True))

# Convert data types
print(int("123"))
print(int("123_456_789"))
print(float("3.14159"))
print(int(True))
try:
    print(float("hello"))
except ValueError:
    print("Exception: Valor informado não é válido para conversão")
