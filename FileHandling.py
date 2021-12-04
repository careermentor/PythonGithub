#obj=open("D:\\RobotFramework\\TestData.txt",'r') #r -read mode
#print(obj.read())
#print(obj.readline())
#print(obj.readline())

#print(obj.read(5))

#for i in obj.read():
 #   print(i)

#s=obj.readline()
#while(s):
 #   print(s)
  #  s=obj.readline()
try:
    obj1=open("D:\\RobotFramework\\TestData2.txt",'r')
    print(obj1.readline())
    print(obj1.tell())
    obj1.seek(25)
    print(obj1.tell())
except:
    print("file not found")

    def hello():
        print("this is my test function")
hello()
