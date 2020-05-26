ALPHABET=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_encrypt(plain_text,key):
	plain_text=plain_text.upper()
	key=key.upper()
	cipher_text=""
	key_index=0

	for i in plain_text:
		index=(ALPHABET.find(i)+(ALPHABET.find(key[key_index])))%len(ALPHABET)
		cipher_text=cipher_text+ALPHABET[index]
		key_index=key_index+1
		if key_index==len(key):
			key_index=0
	return cipher_text
	
def vigenere_decrypt(cipher_text, key):

	cipher_text = cipher_text.upper()
	key = key.upper()
	
	plain_text = ''
	key_index = 0
	
	for character in cipher_text:
		index = (ALPHABET.find(character)-(ALPHABET.find(key[key_index])))%len(ALPHABET)
		plain_text = plain_text + ALPHABET[index]
		
		key_index = key_index + 1
		
		if key_index == len(key):
			key_index = 0
			
	return plain_text

banner="""
         _________ _______  _______  _        _______  _______  _______    _______ _________ _______           _______  _______ 
|\     /|\__   __/(  ____ \(  ____ \( (    /|(  ____ \(  ____ )(  ____ \  (  ____ \\__   __/(  ____ )|\     /|(  ____ \(  ____ )
| )   ( |   ) (   | (    \/| (    \/|  \  ( || (    \/| (    )|| (    \/  | (    \/   ) (   | (    )|| )   ( || (    \/| (    )|
| |   | |   | |   | |      | (__    |   \ | || (__    | (____)|| (__      | |         | |   | (____)|| (___) || (__    | (____)|
( (   ) )   | |   | | ____ |  __)   | (\ \) ||  __)   |     __)|  __)     | |         | |   |  _____)|  ___  ||  __)   |     __)
 \ \_/ /    | |   | | \_  )| (      | | \   || (      | (\ (   | (        | |         | |   | (      | (   ) || (      | (\ (   
  \   /  ___) (___| (___) || (____/\| )  \  || (____/\| ) \ \__| (____/\  | (____/\___) (___| )      | )   ( || (____/\| ) \ \__
   \_/   \_______/(_______)(_______/|/    )_)(_______/|/   \__/(_______/  (_______/\_______/|/       |/     \|(_______/|/   \__/
                                                                                                                                
   				Developed By Akash CHakraborty

"""
if __name__ == '__main__':
	print(banner)
	print("Welcome User! I am your Vigenere Cipher\n")
	print("What do you want to do\nEncrypt = E or Decrypt = D")
	x=input()
	if (x=="E" or x=="e"):

		print("Enter the plain text\n")
		plainText=input()
		print("Enter the key for encryption\n")
		keyForEncrypt=input()
		encryptedText=vigenere_encrypt(plainText,keyForEncrypt)
		print("The Encrypted text is: \n%s"%(encryptedText))

	elif (x=="D" or x=="d"):
		
		print("Enter the encrypted text\n")
		cipherText=input()
		print("Enter the key for encryption\n")
		keyForDecrypt=input()
		decryptedText=vigenere_decrypt(cipherText,keyForDecrypt)
		print("The Decypted text is: \n%s"%(decryptedText))

	else:
		print("Sorry Something went wrong")