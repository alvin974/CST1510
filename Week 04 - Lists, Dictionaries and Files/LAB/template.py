"""
RECORD CHECK - my version
=========================

Name : ALVIN
Lane : IT
"""


def check_record(value, limit):
    """Calculate the difference, percentage and status."""
    difference = limit - value
    percent = (value / limit) * 100

    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return difference, percent, status


def print_report(label, value, limit, difference, percent, status):
    """Print the report for one record."""
    print("------------------------------")
    print("Record:", label)
    print("Used:", value)
    print("Limit:", limit)
    print("Remaining:", difference)
    print("Percent:", round(percent, 2), "%")
    print("Status:", status)
    print("------------------------------")


records = [
    {"label": "R-001", "value": 87.0, "limit": 100.0},
    {"label": "R-002", "value": 120.0, "limit": 100.0},
    {"label": "R-003", "value": 45.0, "limit": 100.0}
]

over_limit = 0

for record in records:
    difference, percent, status = check_record(
        record["value"], record["limit"]
    )

    print_report(
        record["label"],
        record["value"],
        record["limit"],
        difference,
        percent,
        status
    )

    if status == "OVER LIMIT":
        over_limit += 1

print("Total records over the limit:", over_limit)