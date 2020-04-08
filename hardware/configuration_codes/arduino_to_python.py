import serial
arduino = serial.Serial('COM9', 9600)

rawdata=[]
count=0
while count<=10: 
    rawdata.append(str(arduino.readline()))
    count+=1
print(rawdata)
def clean(L):
    newl=[]
    for i in range(len(L)):
        temp=L[i][2:]
        newl.append(temp[:-5])
    return newl
cleandata=clean(rawdata)

# def write(L):
#     file=open("data.txt",mode='w')
#     for i in range(len(L)):
#         file.write(L[i]+'\n')
#     file.close()

print(cleandata)
