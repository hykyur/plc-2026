import re

regex = r"^(?!.*011)[0-1]*$"

sample = [
    "",
    "0",
    "1",
    "00",
    "01",
    "10",
    "11",
    "000",
    "101",
    "111",
    "1001",
    "011",
    "0011",
    "0110",
    "1011",
    "00110",
    "01101"
]

for s in sample:
    if re.fullmatch(regex, s):
        print(f"Accepted: {s!r}")
    else:
        print(f"Rejected: {s!r}")