
fopen = open("areaCodeAct.txt", "r")

count_map = {}

for line in fopen.readlines():
    line = line.replace('\n', '')
    tmp = count_map.get(line)
    if tmp is None:
        count_map[line]=1
    else:
        print tmp
        count_map[line] = int(tmp)+1

for item in count_map:
    print item

print count_map