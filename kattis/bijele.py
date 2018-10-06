wanted = [1,1,2,2,2,8]
input = input().split(" ")
for x in range(len(wanted)):
    wanted[x] = str(wanted[x] - int(input[x]))
print(" ".join(wanted))