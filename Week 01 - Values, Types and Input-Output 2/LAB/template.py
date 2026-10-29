
"""
RECORD CHECK - my version
=========================

Name  : ALVIN ANKUNDA
Lane  : IT
Date  :

Run it: python template.py
"""

label = input("Enter label: ")
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

difference = first - second
percent = (first / second) * 100

print()
print("=" * 34)
print(f" RECORD CHECK - {label}")
print("=" * 34)
print(f"First      : {first:>+10.2f}")
print(f"Second     : {second:>+10.2f}")
print(f"Difference : {difference:>+10.2f}")
print(f"Percent    : {percent:>10.2f} %")
print("=" * 34)
