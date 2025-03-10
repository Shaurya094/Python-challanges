print ("Enter a numeratior: ")
n = int(input())
print ("Enter a demoninator: ")
d = int(input())

if n%d == 0:
    print ("\n" +str(n)+ " is divisable by " +str(d))
else:
     print ("\n" +str(n)+ " is not divisable by " +str(d))