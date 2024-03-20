from tkinter import *
from tkinter import filedialog
from PIL import Image

def encrypt_decrypt(image_path):
    key = 255  # Key for bitwise XOR operation
    image = Image.open(image_path)
    image = image.convert("RGB")

    width, height = image.size
    for i in range(width):
        for j in range(height):
            r, g, b = image.getpixel((i, j))
            image.putpixel((i, j), (r ^ key, g ^ key, b ^ key))

    return image

def open_image():
    image_path = filedialog.askopenfilename()
    if image_path:
        result_image = encrypt_decrypt(image_path)
        result_image.show()
        save_path = filedialog.asksaveasfilename(defaultextension=".png")
        if save_path:
            result_image.save(save_path)

root = Tk()
root.geometry("400x400")  # Set window size to 400x400
root.configure(bg="dark blue")  # Set window background color to dark blue
Button(root, text="Open Image", command=open_image).pack()
root.mainloop()
