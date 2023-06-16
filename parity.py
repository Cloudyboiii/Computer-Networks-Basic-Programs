# print("Enter a number")
# x = int(input())
#
# print("no. entered by the user", x)
# parity = 0
#
# while x != 0:
#     if (x & 1) == 1:
#         parity = 1
#     x >>= 1
#
# print("Parity is: ", parity)

# parity


# def cloudy(x):
#     parity = 0
#     while x:
#         parity = ~parity
#         x = x & (x - 1)
#     return parity


# print("Enter the value")
# n = int(input())

# binary = bin(n)
# print(binary)

# print("Parity of no ", n, " = ", ("odd" if cloudy(n) else "even"))


def sender_add_parity(x):
  print("")
  print("SENDER'S SIDE")
  print("The Data to be transferred is",x)

  one_count=0

  for i in x:
    if i=="1":
      one_count+=1

  if one_count%2==0:
    x=x+"0"
  else:
    x=x+"1"

  print("-------------------------------")  
  receiver_check_parity(x)


def receiver_check_parity(x):
  print("RECEIVER'S SIDE")
  print("the data received is ",x)
  one_count=0

  for i in x:
    if i=="1":
      one_count+=1
      
  if one_count%2==0:
    print(x[:(len(x)-1)]," is the CORRECT data!!")
  else:
    print("Error While data transfer")

data=input("Enter your data in binary form:")
sender_add_parity(data)

# print("PARITY ADDED DATA TO BE SENT: ",x)
  # print("-------------------------------")
  # con=input("WANT TO CHANGE BIT IN THE DATA?:(y/n): ")

  # if con=="y" or con=="Y":
  #   loc=int(input("Enter the location at which data is to be changed:"))

  #   if x[loc]=="1":
  #     l1=list(x)
  #     l1[loc]="0"
  #     x=""

  #     for i in l1:
  #       x=x+i
  #   else:
  #     l1=list(x)
  #     l1[loc]="1"
  #     x=""

  #     for i in l1:
  #       x=x+i
  # else:
  #   print("NO DATA BIT CHANGED! ")
  #   pass
    