
# Python program to demonstrate 
# seek() method 


# Opening "GfG.txt" text file 
f = open('test_2', 'r')

# Second parameter is by default 0 
# sets Reference point to twentieth  
# index position from the beginning 
f.seek(3)

# prints current postion 
print(f.tell())

print(f.readline())
f.close()