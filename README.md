# hashCheck
Generates a hash value for a given file, and outputs the hash to a file. It can also be used to check a hash in.

hashCheck imports modules 'hashlib', 'os', and 'sys'

## Requirements

Pytohn 3.10+

## Usage

Example Usage of hashCheck. Replace variable names with your own.

```
inFile = input()
```
Enter the file path into `inFile`.
```
algSelect = input()
```
Enter the hashing algorithm name. `hashCheck.hashlib.algorithms_available` can be used to display all available algorithms.
```
hashResult = fileHash(inFile, algSelect)
```
hashResult stores the result from fileHash
```
hashResult = hashCheck.fileHash(inFile, algSelect)
```
`hashCheck.fileHash` will return the hash of the selected file using the selected hash.

```
hashCheck.write2File(inFile,algSelect,hashResult)
```
`hashCheck.write2File` will write the filename, algorithm and the hash stored in var to a selected file.

```
hashCheck.compareHash(inFile,hashResult)
```
`hashCheck.compareHash` will comapre the hash in the selected file with the hash stored in var.


### Disclaimer
This code was written for the "Python for Networking" course at Mohawk College and should not be used in a production setting.
