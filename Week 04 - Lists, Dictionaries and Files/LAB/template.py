"""
RECORD CHECK  -  my version
===========================

Name  : ALVIN
Lane  : IT      
Date  :


"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.


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



# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = [
    {"label": "R-001", "value": 87.0, "limit": 100.0},
    {"label": "R-002", "value": 120.0, "limit": 100.0},
    {"label": "R-003", "value": 45.0, "limit": 100.0}
]


# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

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


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
