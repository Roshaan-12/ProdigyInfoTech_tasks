from PIL import Image
import numpy as np

def encrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    image_array = np.array(image)

    # Encrypt the image by adding the key to each pixel value
    encrypted_array = (image_array + key) % 256

    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, key, output_path):
    image = Image.open(image_path)
    image_array = np.array(image)

    # Decrypt the image by subtracting the key from each pixel value
    decrypted_array = (image_array - key) % 256

    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice! Please choose 'E' for encryption or 'D' for decryption.")
        return

    image_path = input("Enter the path to the image: ")
    key = int(input("Enter the key (integer value): "))
    output_path = input("Enter the path to save the output image: ")

    if choice == 'E':
        encrypt_image(image_path, key, output_path)
    else:
        decrypt_image(image_path, key, output_path)

if __name__ == "__main__":
    main()
