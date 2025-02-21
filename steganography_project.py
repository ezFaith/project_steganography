# steganography_encrypt.py
import cv2
import numpy as np
from cryptography.fernet import Fernet
import base64
import getpass

def generate_key(password: str) -> bytes:
    return base64.urlsafe_b64encode(password.ljust(32).encode()[:32])

def encrypt_message(message: str, password: str) -> bytes:
    key = generate_key(password)
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

def encode_message(image, message):
    binary_msg = ''.join(format(byte, '08b') for byte in message)
    binary_msg += '1111111111111110'  # Delimiter to signal end of message
    
    data_index = 0
    data_length = len(binary_msg)
    img_data = image.flatten()
    
    for i in range(len(img_data)):
        if data_index < data_length:
            img_data[i] = (img_data[i] & 0xFE) | int(binary_msg[data_index])
            data_index += 1
        else:
            break
    
    return img_data.reshape(image.shape)

def decode_message(image):
    binary_msg = ""
    for pixel in image.flatten():
        binary_msg += str(pixel & 1)
    
    delimiter = "1111111111111110"
    end_idx = binary_msg.find(delimiter)
    if end_idx != -1:
        binary_msg = binary_msg[:end_idx]
    
    byte_data = [binary_msg[i:i+8] for i in range(0, len(binary_msg), 8)]
    return bytes([int(b, 2) for b in byte_data])

def decrypt_message(encrypted_message: bytes, password: str) -> str:
    key = generate_key(password)
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()

def main():
    choice = input("Choose operation: (1) Encrypt (2) Decrypt: ")
    
    if choice == "1":
        image = cv2.imread(r"F:\Edunet CS internship\mine\mypic.png")
        if image is None:
            print("Error: Could not load 'mypic.png'. Check the file path.")
            return

        message = input("Enter the message to hide: ")
        password = getpass.getpass("Enter a password: ")
        
        encrypted_message = encrypt_message(message, password)
        modified_image = encode_message(image, encrypted_message)
        
        cv2.imwrite("EncryptedImage.png", modified_image)
        print("Encryption complete. Image saved as EncryptedImage.png")
    
    elif choice == "2":
        image = cv2.imread(r"F:\Edunet CS internship\mine\EncryptedImage.png")
        if image is None:
            print("Error: Could not load 'EncryptedImage.png'. Check the file path.")
            return
        
        password = getpass.getpass("Enter the password: ")
        
        encrypted_message = decode_message(image)
        print("Extracted Encrypted Message (Raw):", encrypted_message)  # Debugging statement
        try:
            message = decrypt_message(encrypted_message, password)
            print("Decrypted message:", message)
        except Exception as e:
            print("Decryption failed! Error:", e)
        
        input("Press Enter to exit...")  # Prevents automatic closing
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
