#for loop
#range(start,end,skip)

price_list= []

print("for loop")
for i in range(0,100,1):
    price_list = price_list + [i]

print("value of price_ls" +  str(price_list))


#while loop

price_list=[]
#initialization : 0 is like i=0

i=0
print("while loop")

while(i<100):

    price_list= price_list + [i]

    i=i+1


print(price_list)
# break statement come out of the loop


price_list=[]

i=0

print("continue loop")

while(i<100):
    price_list=price_list + [i]
    i=i+1
    if (i==50):
        print("Continue")
        pass

print(price_list)




# pass is like "continue" statement in Java skips the iteration and continues to be in the loop



