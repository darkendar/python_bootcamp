# import sys
#
# try:
#     print(sys.argv[1])
# except IndexError:
#     print("Zapomniałeś podać nazwę pliku")
#
# with open(sys.argv[1]) as f:
#     dane = {}
#     for line in f:
#         line = line.split(";")
#         user = line[0]
#         action = line[1]
#         time = line[2]
#         time = int(time)
#         user_time = 0
#         for i in f:
#             i = i.split(";")
#             user1 = i[0]
#             action1 = i[1]
#             time1 = line[2]
#             time1 = int(time1)
#             if user == user1 and action != action1:
#                 user_time += time1 - time
#             elif user == user1 and action == action1:
#                 time = time1
#         print(f"user: {user}, time: {user_time}")

file_name = "dane/logs.txt"

def rozwiazanie_1():
    user_last_login = {}
    user_total_time = {}

    with open(file_name) as f:
        dane = {}
        for line in f:
            user, action, time_str = line.split(";")
            time = int(time_str)
            if action == "LOGIN":
                user_last_login[user] = time
            elif action == "LOGOUT":
                time_temp = time - user_last_login[user]
                user_total_time[user] = user_total_time.get(user, 0) + time_temp

    return user_total_time


def rozwiazanie_2():

    user_total_time_login = {}
    user_total_time_logout = {}

    with open(file_name) as f:
        dane = {}
        for line in f:
            user, action, time_str = line.split(";")
            time = int(time_str)
            if action == "LOGIN":
                user_total_time_login[user] = user_total_time_login.get(user, 0) + time
            elif action == "LOGOUT":
                user_total_time_logout[user] = user_total_time_logout.get(user, 0) + time

    final_result = {}
    for user in user_total_time_login:
        final_result[user] = user_total_time_logout[user] - user_total_time_login[user]

    return final_result


print("Czas przebywania w systemie: ")
for user, time in sorted(rozwiazanie_2().items(), key=lambda x: x[1], reverse=True):
        print(f" - {user}: {time} s")

print(rozwiazanie_1() == rozwiazanie_2())