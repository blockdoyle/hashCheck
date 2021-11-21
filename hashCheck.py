import hashlib
import os

def getContent(file):
    openFile = open(file, "rb")
    content = openFile.read()
    openFile.close()
    return content

def write2File(file, alg, hashValue):
    openFile = open(f'.\hashes\{file}.hash', "w")
    openFile.write(alg + ":" + hashValue)
    openFile.close()
    
def fileHash(file, alg):
    fileContent = getContent(file)
    hashContent = hashlib.new(alg)
    hashContent.update(fileContent)
    return hashContent.hexdigest()
    # return hashlib.md5(fileContent).hexdigest()
    
def compareHash(file,alg):
    hashFile = open(f'.\hashes\{file}.hash', 'r')
    fileContent = hashFile.read()
    hashFile.close()
    fileContent = fileContent.split(":")
    fileContent = fileContent[1]
    if fileContent == hashResult:
        return "Hash matches stored value."
    else:
        return "Hash does not match stored value."

inFile = input("Enter file path for hash value: ")
algSelect = input("Enter the algorithm you would like to use from below list:\n\n"+str(hashlib.algorithms_available)+"\n")
hashResult = fileHash(inFile, algSelect)

writeOrCompare = input("Would you like to write or compare? ")
match writeOrCompare:
    case "write":
        conOrFile = input("Would you like to write to console, or file? ")
        match conOrFile:
            case "console":
                print(inFile + ":" + hashResult)
            case "file":
                write2File(inFile,algSelect,hashResult)
    case "compare":
        print(compareHash(inFile,algSelect))