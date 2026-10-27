
"""
RECORD CHECK - my version
=========================

Name  : ALVIN ANKUNDA
Lane  : IT

Run it: python template.py
"""

hostname = input("Hostname: ")
used_gb = float(input("GB used: "))
total_gb = float(input("GB total: "))

difference = total_gb - used_gb
percent = (used_gb / total_gb) * 100
free_percent = (difference / total_gb) * 100

print("=" * 34)
print(f"  RECORD CHECK - {hostname}")
print("=" * 34)
print(f"Used      : {used_gb:>10.2f}")
print(f"Total     : {total_gb:>10.2f}")
print(f"Free      : {difference:>+10.2f}")
print(f"Percent   : {percent:>10.2f} %")
print(f"Free %    : {free_percent:>10.2f} %")
print("=" * 34)
