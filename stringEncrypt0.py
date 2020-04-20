
def encrypt(s):   
    # Define XOR key  Any character value will work 
	xorKey = 'P'; 
	eList =[]
	print(" * * * * * * * ")
	for n in range (0,len(s)):
		newChr = ord(s[n]) ^ ord("P")
		print (chr(newChr+33)," ",end="")
	
def printString(s):
	print(" * * * * * * * ")
	for n in range (0,len(s)):
		print(s[n]," ",end="")
	print("\n **** \n")

def main():
	startString = "Messenger"
	printString(startString)
	encrypt(startString)
	
if __name__ == '__main__':
	main()



'''
fileList = [] # fileList is a list
with open("data.txt") as f:
  while True:
    c = f.read(1)
    fileList.append(c) 
    if not c:
      print ("End of file")
      break
    print ("Read a character:", c)



# The same function is used to encrypt and 
# decrypt 
def encryptDecrypt(inpString): 
  
    # Define XOR key 
    # Any character value will work 
    xorKey = 'P'; 
  
    # calculate length of input string 
    length = len(inpString); 
  
    # perform XOR operation of key 
    # with every caracter in string 
    for i in range(length): 
      
        inpString = (inpString[:i] +  chr(ord(inpString[i]) ^ ord(xorKey)) +     inpString[i + 1:]); 
        print(inpString[i], end = ""); 
      
    return inpString; 
  
# Driver Code 
if __name__ == '__main__': 
    sampleString = "GeeksforGeeks"; 
  
    # Encrypt the string 
    print("Encrypted String: ", end = ""); 
    sampleString = encryptDecrypt(sampleString); 
    print("\n"); 
  
    # Decrypt the string 
    print("Decrypted String: ", end = ""); 
    encryptDecrypt(sampleString); 
  
# This code is contributed by Princi Singh 
'''
