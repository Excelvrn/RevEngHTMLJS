#new py program
import sys
print("Start")              
print(sys.path) 
sys.path+=['/home/excelvrn/Pyth/js-beautify-main/python']
print(sys.path) 
import jsbeautifier
print(sys.argv)
for i in range(1,len(sys.argv)):
    print(sys.argv[i])
    OpenedFile = open(sys.argv[i], 'r')
    text = OpenedFile.read()
    #print(text)
    res = jsbeautifier.beautify(text)
    #print(res)
    NF = "0."+sys.argv[i]
    k = open(NF, 'w')
    k.write(res)
    k.close()
    OpenedFile.close()
# Path import
print("End")


