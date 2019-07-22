import math

#Finds the row- , column spot and page number from 8 x 6 grid

P_MTotal = 0
col = 6
col2 = 1
remainder = 8
row_count = 0
row_countRem = 0
page_count = 0
pbol = 0
ip_num = input("Total amount: ")
num = int(ip_num)
p_num = num/48

#Gets the row.
while P_MTotal < num:
    P_MTotal  += 1
    row_count = P_MTotal/col
    if(row_count > 8.1):
         row_countRem = row_count % remainder
         if (row_countRem == 0):
             row_countRem = 8

    page_count = P_MTotal/48

             
#Gets the column.
for _ in range(1, P_MTotal):
        col2 += 1
        if (col2 > 6):
            col2 = 1


print("Row:", math.ceil(row_count), "\nColumn:" , col2, "\nPage Number:"  , math.ceil(page_count))

