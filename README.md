# hashCheck
Generates a hash value for a given file, and outputs the hash to a file. It can also be used to check a hash in.

hashCheck imports modules 'hashlib' and 'os.'

## Usage

Example Usage of hashCheck. Replace 'var' with your own variable name.

`hashCheck.fileHash` will return the hash of the selected file using the selected hash.
```
var = hashCheck.fileHash(inFile, algSelect)
```

`hashCheck.write2File` will write the filename, algorithm and the hash stored in var to a selected file.
```
hashCheck.write2File(file,algorithm,var)
```

`hashCheck.compareHash` will comapre the hash in the selected file with the hash stored in var.
```
hashCheck.compareHash(inFile,var)
```