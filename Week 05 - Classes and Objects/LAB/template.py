"""
RECORD CHECK - my version
=========================

Name : ALVIN
Lane : IT
Date : 24 October 2026

Run it: python template.py
"""

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

    def percent(self):
        return (self.value / self.limit) * 100

    def status(self):
        percentage = self.percent()

        if percentage >= 100:
            return "OVER LIMIT"
        elif percentage >= 90:
            return "WARNING"
        else:
            return "OK"

    def is_over(self):
        return self.value > self.limit

    def summary(self):
        return f"{self.label}: {self.value}/{self.limit}"


records = [
    Record("Server-A", 87.0, 100.0),
    Record("Server-B", 120.0, 100.0),
    Record("Server-C", 95.0, 100.0)
]

for record in records:
    print(record.summary())
    print(record.percent())
    print(record.status())
    print(record.is_over())