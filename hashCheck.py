import hashlib
import os

def getContent(file):
    openFile = open(file, "rb")
    content = openFile.read()
    openFile.close()
    return content

def write2File(file, alg, hashValue):
    openFileBasename = os.path.basename(file)
    openFile = open(f'.\hashes\{openFileBasename}.hash', "w")
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