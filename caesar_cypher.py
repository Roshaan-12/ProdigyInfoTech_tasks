def caesar_cipher_encrypt(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice! Please choose 'E' for encryption or 'D' for decryption.")
        return

    text = input("Enter your message: ")
    shift = int(input("Enter the integer shift value: "))

    if choice == 'E':
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print(f"Encrypted message: {encrypted_text}")
    else:
        decrypted_text = caesar_cipher_decrypt(text, shift)
        print(f"Decrypted message: {decrypted_text}")

if __name__ == "__main__":
    main()
