import hashlib
import os

def getContent(file):
    openFile = open(file, "rb")
    content = openFile.read()
    openFile.close()
    return content

def write2File(file, hashValue):
    openFile = open(f'.\hashes\{file}', "w")
    openFile.write(file + ":" + hashValue)
    openFile.close()
    
def fileHash(file, alg):
    fileContent = getContent(file)
    hashContent = hashlib.new(alg)
    hashContent.update(fileContent)
    return hashContent.hexdigest()
    # return hashlib.md5(fileContent).hexdigest()

inFile = input("Enter file path for hash value: ")
algSelect = input("Enter the algorithm you would like to use from below list:\n\n"+str(hashlib.algorithms_available)+"\n")
hashResult = fileHash(inFile, algSelect)

consoleOrFile = input("Would you like to write to console, or file? ")
match consoleOrFile:
    case "file":
        write2File(inFile,hashResult)
    case "console":
        print(inFile + ":" + hashResult)