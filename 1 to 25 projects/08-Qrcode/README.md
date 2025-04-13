# QR Code Encoder / Decoder Project

## 📚 Overview

This project allows you to generate and decode QR codes easily using Python. It includes two main functionalities:

1. **Generate QR codes with custom data and save them as images**
2. **Decode QR codes from saved image files**

---

## 🛠 Libraries Used

- `qrcode` — for generating QR codes
- `opencv-python` (cv2) — for decoding QR codes from images
- `Pillow` — for image display and manipulation

---

## ✅ Installation

Before running the project, install the required libraries using the following commands:

```bash
pip install qrcode
pip install opencv-python
pip install pillow
```

---

## 🚀 How to Use

1. **Run the script**
2. Choose one of the following options:
   - **1**: Generate a QR code
     - Enter the data you want to encode.
     - Enter the filename (it will automatically save as `.png` if you don’t add an extension).
     - The generated QR code image will be saved and displayed.
   - **2**: Decode a QR code
     - Enter the filename of the QR code image.
     - The decoded data will be printed.
   - **3**: Exit the program

---

## 📂 Example Usage

### ➡️ Generate a QR Code

Select an option:

1. Generate QR Code
2. Decode QR Code
3. Exit
Enter choice (1/2/3): 1
Enter the data to encode: Hello World!
Enter filename to save (example: mycode.png): hello_world_qr
✅ QR Code saved as 'hello_world_qr.png'

### ➡️ Decode a QR Code

Select an option:

1. Generate QR Code
2. Decode QR Code
3. Exit
Enter choice (1/2/3): 2
Enter QR Code image filename to decode: hello_world_qr.png
✅ Decoded data: Hello World!

## 🔎 Features

- Automatically saves QR codes as `.png` if the user forgets the extension
- Displays the generated QR image for quick verification
- Handles errors if file not found or unreadable
- Clean and user-friendly console interface

## 🤝 Contributing

Feel free to fork the repository and submit pull requests to improve or add new features.

## 📜 License

This project is open-source and free to use for educational and personal projects.
