
"""
RECORD CHECK - my version
=========================

Name : ALVIN ANKUNDA
Lane : IT

Run it: python template.py
"""


def status_of(percent):
    """Return the status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and percentage."""
    difference = limit - value
    percent = (value / limit) * 100
    return difference, percent


label = input("Hostname: ")
value = float(input("GB used: "))
limit = float(input("GB total: "))

difference, percent = check(value, limit)
status = status_of(percent)

print()
print("=" * 34)
print(f"  RECORD CHECK - {label}")
print("=" * 34)

print(f"  Used       : {value:>10.2f}")
print(f"  Total      : {limit:>10.2f}")
print(f"  Free       : {difference:>10.2f}")
print(f"  Percent    : {percent:>10.2f} %")
print(f"  Status     : {status}")

print("=" * 34)
