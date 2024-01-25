# Exercise 8: Print the following pattern

#Expected output
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

#Create a for loop for the row pattern
for column in range(1,6):
#Create another for loop for the column of pattern
    for row in range(column):
#Display the output for the column
        print(column, end=" ")
#Display the output for the row
    print("")