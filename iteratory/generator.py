def generator(jakis_max):
    for i in range(0, jakis_max, 2):
        yield i


for x in generator(15):
    print(x)
