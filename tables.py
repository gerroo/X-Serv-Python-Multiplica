import sys
a = int(input("TO -> ")) #I dont know spanish replace the thing in "<replace me>"
for i in range(1,a+1):
    for j in range(1,a+1):
        sys.stdout.write("{}\t".format(j*i))
    sys.stdout.write('\n')
