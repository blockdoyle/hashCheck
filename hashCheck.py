import hashlib, os # import 'hashlib' and 'os' modules

def getContent(file): # gets content of file in binary mode
    openFile = open(file, "rb")
    content = openFile.read()
    openFile.close()
    return content

def write2File(file, alg, hashValue): # writes filename, algorithm, and hash to file
    openFileBasename = os.path.basename(file)
    openFile = open(f'.\hashes\{openFileBasename}.hash', "w")
    openFile.write(alg + ":" + hashValue)
    openFile.close()
    
def fileHash(file, alg): # generates a hash of a file based on selected algorithm
    fileContent = getContent(file)
    hashContent = hashlib.new(alg)
    hashContent.update(fileContent)
    return hashContent.hexdigest()
    
def compareHash(file,currentHash): # compares current hash with saved hash
    openFileBasename = os.path.basename(file)
    hashFile = open(f'.\hashes\{openFileBasename}.hash', 'r')
    fileContent = hashFile.read()
    hashFile.close()
    fileContent = fileContent.split(":")
    fileContent = fileContent[1]
    if fileContent == currentHash:
        return "Hash matches stored value."
    else:
        return "Hash does not match stored value."