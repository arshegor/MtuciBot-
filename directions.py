from datetime import datetime

now = datetime.now()
year = now.year

directionBVT = []
for i in range(4):
    for j in range(5):
        directionBVT.append("бвт" + str(year - 2000 - i) + "0" + str(j + 1))

directionBFI = []
for i in range(4):
    for j in range(5):
        directionBVT.append("бфи" + str(year - 2000 - i) + "0" + str(j + 1))

directionBST = []
for i in range(4):
    for j in range(5):
        directionBVT.append("бст" + str(year - 2000 - i) + "0" + str(j + 1))


directions = ['бвт', 'бст', 'бфи']

courses = {directions[0]:{1:5, 2:5, 3:3, 4:2}, directions[1]:{1:4, 2:4, 3:3, 4:2},directions[2]:{1:2, 2:2, 3:1, 4:1}}

