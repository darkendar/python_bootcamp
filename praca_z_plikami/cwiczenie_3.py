# import sys
#
# try:
#     print(sys.argv[1])
#     print(sys.argv[2])
# except IndexError:
#     print("Zapomniałeś podać nazwę pliku")
#
# with open(sys.argv[1]) as f:
#     for line in f:
#         ilosc_malp = 0
#         line = line.strip(" ").lower()
#         for znak in line:
#             if znak == "@":
#                 ilosc_malp += 1
#         if ilosc_malp > 1:
#             line = line.lstrip("@")
#
#         print(line, ilosc_malp)

import sys

file_in = sys.argv[1]
file_out = sys.argv[2]

try:
    print(file_in)
    print(file_out)
except IndexError:
    print("Zapomniałeś podać nazwę pliku")

with open(file_in) as f:
    unique_emails = set()
    for line in f:
        line = line.strip().lower()
        if line.count("@") == 1:
            unique_emails.add(line)

emails = sorted(unique_emails)

with open(file_out, "w") as f:
    for email in emails:
        f.write(email + "\n")