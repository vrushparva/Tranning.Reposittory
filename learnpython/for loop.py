############################################
# n = int(input("Enter Value :" ))


# for row in range(0, 5):
#     for col in range(row - 1,4):
#         print("*", end=" ")
#     print()
#
############################################

#
# for row in range(0, 5):
#     for col in range(0,row+1):
#         print("*", end=" ")
#     print()

############################################

# for row in range(0, 5):
#     for col in range(0, 5):
#         if col == 0 or row == 4 or col == row:
#             print("*", end=" ")
#         else:
#             print(end="  ")
#     print()

###########################################
# print star like pyramid shape

# num = int(input("Enter Value:"))

# for i in range(0, num):
#     for j in range(0, num-i-1):
#         print( end=" ")
#     for j in range(0, i+1):
#         print("*", end=" ")
#     print("")


###########################################
# print star like pyramid shape using function


# def pyramid(rows):
#     for i in range(rows):
#         print(" " * (rows - i - 1) + "*" * i + 1)#


##############################################################
# heart shape for loop

# for i in range(0,6):
#     for j in range(i, 0):
#         print(" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

##############################################################

# for i in range(0,6):
#     for j in range(i, 0):
#         print(" ")
#     for j in range(i+1):
#         print("", end=" ")
#     print()
#
##############################################################

# n = int(input("Enter row Which you want to print :"))
# num = 1
#
# for row in range(1,n+1):
#     print(" ",end=" ")
#     for col in range(1,row+1):
#         print(num ,end=" ")
#         num += 1
#     print()
##############################################################
# # heart shape star print
# for row in range(0, 6):
#     for col in range(0, 7):
#         if col % 3 != 0 and row == 0:
#             print("*", end="")
#         else:
#             print(" ", end="")
#
#         # for col in range(0, 7):
#         if col % 3 == 0 and row == 1:
#             print("*", end="")
#         else:
#             print("  ", end="")
#
#         if col == 7 and row == 2:
#             print("*", end="")
#         else:
#             print(" ", end="")

for row in range(0, 6):
    for col in range(0, 7):
        if (col % 3 != 0 and row == 0) or (col % 3 == 0 and row == 1) or (row - col == 2) or (row + col == 8):
            print("%", end=" ")
        else:
            print("", end="  ")

    print()
