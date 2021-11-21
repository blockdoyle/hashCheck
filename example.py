import hashCheck

inFile = input("Enter file path for hash value: ")
algSelect = input("Enter the algorithm you would like to use from below list:\n\n"+str(hashCheck.hashlib.algorithms_available)+"\n")
hashResult = hashCheck.fileHash(inFile, algSelect)
print(hashResult)
writeOrCompare = input("Would you like to write or compare? ")
match writeOrCompare:
    case "write":
        conOrFile = input("Would you like to write to console, or file? ")
        match conOrFile:
            case "console":
                print(inFile + ":" + hashResult)
            case "file":
                hashCheck.write2File(inFile,algSelect,hashResult)
    case "compare":
        print(hashCheck.compareHash(inFile,algSelect))