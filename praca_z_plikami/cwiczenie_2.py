import sys

try:
    print(sys.argv[1])
except IndexError:
    print("Zapomniałeś podać nazwę pliku")

with open(sys.argv[1]) as f:
    dane = {}
    for line in f:
        line = line.split(";")
        user = line[0]
        action = line[1]
        time = line[2]
        time = int(time)
        user_time = 0
        for i in f:
            i = i.split(";")
            user1 = i[0]
            action1 = i[1]
            time1 = line[2]
            if user == user1 and action != action1:
                user_time += time1 - time
            elif user == user1 and action == action1:
                time = time1
        print(f"user: {user}, time: {user_time}")
