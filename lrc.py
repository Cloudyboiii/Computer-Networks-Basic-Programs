# # # // Write a code of longitudinal redundancy check in pytho
# # c = 0
# # n = 0
# # def xyz(bin, c):
# #     for i in range (0,n):
# #         i < 9
# #         if bin[i] == '1':
# #             c = c + 1
        
# #     i = i + 1
# #     if c%2 == 0:
# #         bin[8] = '0'
# #         print("Even")
# #     else:
# #         bin[8] = '1'
# #         print("odd")

# #     print("bin")
    

# # print(input("Enter the 8 bit binary number",bin))
# # xyz(bin[10],c)

# # flag = 0

# # def xyz(a,n):
# #     print("Enter Data: ")
# #     for i in range (n):
# #         print(a[i])

# #     for j in range (n):
# #         if a[j] == 1:
# #             flag = flag + 1

# #     print("\n Flag count -", flag)
# #     if flag%2 == 0:
# #         print("\n No. of 1s are even")
        
# #         print("Data to be sent-")
# #         for k in range (n):
# #             print(a[k])
# #     else:
# #         print("\n No. of 1s are odd")
# #         print("\n fter adding Parity bit -")
# #         a[n]=1
# #         for l in range (n):
# #             print(a[l])

# # n = int(input("enter n "))
# # a=[25]
# # print("Enter the length of binary data-",n)
# # xyz(a,n)



# # # count = 0
# # # bit=[100]
# # # choice = 0
# # # def xyz(bit,n,choice):
# # #     print("Enter data stream :")
# # #     for i in range(n):
# # #         print(bit[i])
# # #         if bit[i] == 1:
# # #             count == count + 1

# # #     print("No.s of 1's are:",count)
# # #     print("Enter choice to implement parity bit 1 for sender and 2 for reciver", choice)

# # #     while choice:
# # #         if count%2 == 0:
# # #             bit[1] = 0
# # #         else:
# # #             bit[1] = 1
# # #     print("Databit after adding parity bit")


# # # l =int(input("Enter value of l"))

# # # print("Enter length of data stream",l)
# # # xyz(bit,l,choice)



# import sys
# val1= 'hi'

# if (len(sys.argv)>1):
#         val1=str(sys.argv[1])

# def parityOf(int_type):
# 	parity = 0
# 	while (int_type):
# 		parity = ~parity
# 		int_type = int_type & (int_type-1)
	
# 	if (parity==-1):
# 		return(0)
# 	return(1)

# def calcLRC(input):

#     lrc = ord(input[0])
    
#     for i in range(1,len(input)):
# 	    lrc ^= ord(input[i])     
#     return lrc


# def showLRC(input,res):
#     input = input[:7]

#     print ('Char\tHex\tBinary')
#     print ('------------------------------------')
#     for i in range(0,len(input)):
# 	    print (input[i],"\t",hex(ord(input[i])),"\t",bin(ord(input[i])))


#     print ('\nBit\tBinary         LRC')
#     print ('----------------------------')
#     print ('  \t',)
#     for i in range(0,len(input)):  
#     	print (input[i],)
#     print( "")

#     mask=1
#     for bitpos in range(0,7):
#         bit = (res & mask) >> bitpos
#         print ("b",bitpos,"\t",)

#     	for i in range(0,len(input)):    	
#         	bitchar = (ord(input[i]) & mask) >> bitpos
# 		print bitchar,
		
#         print bit
# 	mask = mask << 1

# # Show VRC
#     print "VRC\t",
#     for i in range(0,len(input)):    	
#         print parityOf(ord(input[i])),

#     print parityOf(res),
#     return

# res = calcLRC(val1)

# print ""
# print "Input: ",val1," LRC is ",hex(res),"- Char: ",chr(res)
# print ""

# showLRC(val1,res)



#concept of lrc
#function definitions


def add_even_parity(a,r,c):
    
    #sender's side
    
    horizontal_parity_row=""
    count=0
    for j in range(c):
        for i in range(r):
            if a[i][j]=="1":
                count+=1
        
        if count%2==0:
            horizontal_parity_row+="0"
        else:
            horizontal_parity_row+="1"
        count=0
    
    a=a+[horizontal_parity_row]
    print("after adding parity bits the data becomes :")
    print("\n")
    print(a)
    check_even_parity(a,r,c)
    


def check_even_parity(a,r,c):
    #receiver's side
    
    
    count=0

    for j in range(c):
        for i in range(r+1):
            if a[i][j]=="1":
                count+=1      
                
                
    if count%2==0:
        print("Data is received correct count is even:")
        a.pop()
        print("after removing the parity bits:")
        for i in range(r):
            print(a[i])
            
            
    else:
        print("Error was introduced while receiving data!")
        
        
        
#main


row=int(input("Enter the number of Data you want to enter:"))
column=int(input("Enter the number of columns of the data:"))
arr=[]
for i in range(row):
    x=input("Enter data in binary form")
    print("\n")
    arr=arr+[x[:column]]

add_even_parity(arr,row,column)

