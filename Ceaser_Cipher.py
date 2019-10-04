import sys
iput = input("Cipherable word: ")
nput = input("letter amount to cipher by: ")
cip = ""
cip2 = ""

#Tries to turn 'nput' into an int if possible, else it raises an exception and stops the program
try:
  nput = int(nput)
except ValueError:
  print("Second input needs to be a number")
  sys.exit(1)

#Encryption
for x in iput:
  x = ord(x) + nput
  cip += chr(x)

#Decryption
for x2 in cip:
  x2 = ord(x2) - nput
  cip2 += chr(x2)            
        
    


        
print("Ciphered text: ", cip, "\n Decrypted Text: ", cip2)