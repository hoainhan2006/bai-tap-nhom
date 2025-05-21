import tkinter as tk
from tkinter import PhotoImage
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
import easyocr
root=tk.Tk()
root.title("Nhận diện biển số xe")
root.geometry("800x400")
img=Image.open("xe.jpg")
img=img.resize((1920,1080))
img=ImageTk.PhotoImage(img)
img_label=tk.Label(root,image=img)
img_label.place(x=0,y=0)
tk.Label(root,text="Bài tập nhận diện biển số xe",bg="black",fg="white",font=("Times New Roman",22),relief=tk.GROOVE,bd=3,width=25).pack(pady=30)
img_label1=tk.Label(root)
text_label=tk.Label(root)
bienso=' '
def nut_tai_file():
    filepath=filedialog.askopenfilename(initialdir="/home",title="Chọn file ảnh ",filetypes=( ("Tất cả ảnh", "*.jpg *.jpeg *.png *.bmp *.gif"), ("JPEG", "*.jpg *.jpeg"),("PNG", "*.png"),("Bitmap", "*.bmp"),("GIF", "*.gif")))
    global img_tk,bienso
    anh=cv2.imread(filepath)
    reader = easyocr.Reader(['en'])
    result = reader.readtext(anh)
    for bbox, text, conf in result:
        bienso = bienso + text
    img_pil = Image.fromarray(anh)
    img_tk = img_pil.resize((500, 450))
    img_tk = ImageTk.PhotoImage(img_tk)
    img_label1.configure(image=img_tk)
    img_label1.pack()
    text_label.configure(text=bienso)
    text_label.pack()
button=tk.Button(root,text="Tải ảnh",command=nut_tai_file)
button.pack()
root.mainloop()
