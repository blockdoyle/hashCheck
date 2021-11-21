import hashlib
import os

def getContent(file):
    openFile = open(file, "rb")
    content = openFile.read()
    openFile.close()
    return content

def write2File(hashValue):
    outFile = input("Enter file location for write: ")
    openFile = open(outFile, "a")
    openFile.write(hashValue)
    openFile.close()
    
def fileHash(file):
    fileContent = getContent(file)
    return hashlib.md5(fileContent).hexdigest()

inFile = input("Enter file path for hash value: ")
print(fileHash(inFile))