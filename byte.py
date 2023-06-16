# # //Write a Python program for byte stuffing.?
# # >>> flagbyte + frame.replace(escapebyte,escapebyte*2)+ flagbyte
# 'ZLEONAARDOZ'


# def applyByteStuffing(flagbyte, escapebyte, payload):
#     x = payload.replace (escapebyte, escapebyte*2)
#     y = x.replace (flagbyte, escapebyte+flagbyte)
#     return flagbyte + y + flagbyte #return value


# assert applyByteStuffing('Z','A','LEONARDO') == 'ZLEONAARDOZ'


# str1=input("Enter the data to be stuffed:")
# print("HERE THE CHARACTER \'E' --> represents escape character:  ")
# print("AND THE CHARACTER \'F' --> represents flag byte")

# print("----------------------")
# print("SENDER's SIDE:")
# print(str1)
# print("----------------------")
# #stuffing
# data=list(str1)
# loc=[]
# for i in range(len(data)):
#     if data[i]=="E" or data[i]=="F":
#         loc=loc+[i]
# count=0
# for i in loc:
#     data.insert(i+count,"E")
#     count=count+1

# #ADDING FLAGS
# data=["F"]+data
# data.append("F")
# print("----------------------")
# print("AT RECEIVER's END:")
# print(data)

str1=input("Enter the data to be stuffed:")
print("HERE THE CHARACTER 'E' --> represents escape character:  ")
print("AND THE CHARACTER 'F' --> represents flag byte")

print("----------------------")
print("SENDER's SIDE:")
print(str1)
print("----------------------")
#stuffing
data=list(str1)
loc=[]
for i in range(len(data)):
    if data[i]=="E" or data[i]=="F" or data[i]=="e" or data[i]=="f":
        loc=loc+[i]
count=0
for i in loc:
    data.insert(i+count,"E")
    count=count+1
 
#ADDING FLAGS
data=["F"]+data
data.append("F")
print("----------------------")
print("AT RECEIVER's END:")
print(data)
 