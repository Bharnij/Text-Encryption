

print('''

  ____ _       _                 _____                             _     
 / ___(_)_ __ | |__   ___ _ __  | ____|_ __   ___ _ __ _   _ _ __ | |_   
| |   | | '_ \| '_ \ / _ \ '__| |  _| | '_ \ / __| '__| | | | '_ \| __|  
| |___| | |_) | | | |  __/ |    | |___| | | | (__| |  | |_| | |_) | |_ _ 
 \____|_| .__/|_| |_|\___|_|    |_____|_| |_|\___|_|   \__, | .__/ \__(_)
        |_|                                            |___/|_|          


''')


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

text = input("Type your message:\n").lower()

shift = int(input("Type the shift number:\n")) % 26 


def encrypt(plain_text, shift_amount):
    
    cipher_text = ""
    
    for letter in plain_text:
        
        if letter in alphabet:
            
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26              
            new_letter = alphabet[new_position]
            
            cipher_text += new_letter
        
        else:            
            cipher_text += letter  
    
    print(f"The encoded message is {cipher_text}")


def decrypt(cipher_text, shift_amount):
    
    plain_text = ""
    
    for letter in cipher_text:
    
        if letter in alphabet:
            position = alphabet.index(letter)    
         
            new_position = (position - shift_amount) % 26      
            plain_text += alphabet[new_position]
    
        else:
            plain_text += letter  

    print(f"The decoded message is {plain_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)

elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)

else:
    print("Invalid input. Please type 'encode' to encrypt or 'decode' to decrypt.")



    
