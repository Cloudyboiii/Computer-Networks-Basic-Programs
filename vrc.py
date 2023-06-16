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
# 	lrc ^= ord(input[i])     
#     return lrc


# def showLRC(input,res):
#     input = input[:7]

#     print('Char\tHex\tBinary')
#     print('------------------------------------')
#     for i in range(0,len(input)):
# 	print (input[i],"\t",hex(ord(input[i])),"\t",bin(ord(input[i])))


#     print('\nBit\tBinary         LRC')
#     print('----------------------------')
#     print('  \t',)
#     for i in range(0,len(input)):  
#     	print(input[i],)
#     print("")

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


# def xyz(bin,c):
#     for i in range(9):
#         if bin[i] == '1':
#             c = c + 1
    
#     if c%2 == 0:
#         bin[8] = '0'
#         print("Even")
#     else:
#         bin[8] = '1'
#         print("odd")

#     print(bin)
# c = 100
# print(input("Enter 8 bit binary no.s:",bin))
# xyz(bin,c)


b = [4]
a = [5][4]
a[5][4] = [{1,0,1,1},{1,0,0,1},{0,1,0,0},{1,1,1,1}]

def xyz(a,b):
    print("Given Data is-")
    for col in range(4):
        flag = 0
        for row in range(4):
            if a[row][col] == 1:
                flag = flag + 1

        if flag%2 == 0:
            b[col] = 0
        else:
            b[col] = 1

    print("Parity is -")
    for k in range(4):
        print(b[k])

    for m in range(4):
        a[4][m] = b[m]

    print("\n \n \n fter appending \n")
    for l in range(5):
        for n in range(4):
            print(a[l][n])
        print("\n")

xyz(a,b)

