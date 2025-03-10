c1 = int(input("Enter the first cylist's speed: "))
c2 = int(input("Enter the second cylist's speed: "))
c3 = int(input("Enter the third cylist's speed: "))

avg = int((c1+c2+c3)/3)
print ("The average speed is: ", avg)

if c1 < avg:
    print ("The first cyclist is going slower than average speed.")
elif c2 < avg:
    print ("The second cyclist is going slower than average speed.")
elif c3 < avg:
    print ("The third cyclist is going slower than average speed.")
else:
    print ("None are going below the average speed.")