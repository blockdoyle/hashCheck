import hashCheck # imports hashCheck.py

inFile = input("Enter file path for hash value: ") # asks the user for file location
algSelect = input("Enter the algorithm you would like to use from below list:\n\n"+str(hashCheck.hashlib.algorithms_available)+"\n") # asks user to select algorithm from displayed list
hashResult = hashCheck.fileHash(inFile, algSelect) # stores return value from hashCheck.fileHash(inFile, algSelect)

writeOrCompare = input("Would you like to write or compare? ") #asks user if they would like to write or compare hash
match writeOrCompare:
    case "write":
        conOrFile = input("Would you like to write to console, or file? ") # asks user if they would like to write to console or to file
        match conOrFile:
            case "console":
                print(inFile + ":" + algSelect + ":" + hashResult) # writes filename, algorithm, and hashResult to console
            case "file":
                hashCheck.write2File(inFile,algSelect,hashResult) # writes filename, algorithm, and hashResult to file
    case "compare":
        print(hashCheck.compareHash(inFile,hashResult)) # compares saved *.hash file with current file hash