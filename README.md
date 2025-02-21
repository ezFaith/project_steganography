# Secure Data Hiding in Image Using Steganography

## 📌 Project Overview
This project implements **image steganography** using **Least Significant Bit (LSB) encoding** to hide encrypted messages inside images. It enhances security by incorporating **AES-128 encryption (Fernet)** before embedding the message.

## 🔍 Features
✅ **Steganography using LSB encoding**
✅ **AES-128 encryption for enhanced security**
✅ **Supports image formats like PNG & JPG**
✅ **Dual functionality: Encrypt & Decrypt messages**
✅ **Password-protected message retrieval**

## 🛠️ Technologies Used
- **Python** – Core language for implementation
- **OpenCV (cv2)** – Image processing & pixel manipulation
- **Cryptography (Fernet - AES)** – Encrypts hidden messages
- **NumPy** – Efficient pixel array operations

## 📂 Project Structure
```
├── steganography_encrypt.py  # Encryption script
├── steganography_decrypt.py  # Decryption script
├── mypic.png                # Default input image
├── EncryptedImage.png        # Output steganographic image
├── README.md                 # Project documentation
```

## 🚀 Installation & Setup
1️⃣ **Clone the repository**
```sh
git clone https://github.com/your-repo-link.git
cd your-repo-folder
```
2️⃣ **Install dependencies**
```sh
pip install opencv-python cryptography numpy
```
3️⃣ **Run the encryption script**
```sh
python steganography_encrypt.py
```
4️⃣ **Run the decryption script**
```sh
python steganography_decrypt.py
```

## 🔐 Usage Instructions
### ➤ **Encryption Process**
- The script reads `mypic.png`.
- The user enters a **message** & **password**.
- The message is **AES-encrypted** and hidden inside the image.
- A new **EncryptedImage.png** is generated.

### ➤ **Decryption Process**
- The script reads `EncryptedImage.png`.
- The user enters the correct **password**.
- The message is extracted & decrypted.
- If the password is wrong, access is denied.


## 🔗 GitHub Repository
[Click here to visit the repository](https://github.com/ezFaith/project_steganography.git)

## 🔮 Future Scope
- 🔹 **Multi-layer encryption for added security**
- 🔹 **GUI interface for user-friendly interaction**
- 🔹 **Support for audio & video steganography**

## 👨‍💻 Author
**Dipankar Saha**  
[Your GitHub Profile](https://github.com/ezFaith)

---
📌 **If you like this project, give it a ⭐ on GitHub!**
