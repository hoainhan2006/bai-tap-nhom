import tkinter as tk
from tkinter import PhotoImage
import cv2
from PIL import Image, ImageTk
root=tk.Tk()
root.title("Nhận diện biển số xe")
root.geometry("800x400")
img=Image.open("xe.jpg")
img=img.resize((1920,1080))
img=ImageTk.PhotoImage(img)
img_label=tk.Label(root,image=img)
img_label.place(x=0,y=0)
tk.Label(root,text="Bài tập nhận diện biển số xe",bg="black",fg="white",font=("Times New Roman",22),relief=tk.GROOVE,bd=3,width=25).pack(pady=30)
entry=tk.Entry(root,width=40)
tk.Label(text="Hãy nhập đường dẫn hình ảnh vào đây").pack()
baoloi2 = tk.Label(root)
baoloi = tk.Label(root)
baoloi3=tk.Label(root )
img_label1=tk.Label(root)
def anvao():
    try:
        global img1
        img1=Image.open(entry.get().strip())
        img1 = img1.resize((500, 450))
        img1=ImageTk.PhotoImage(img1)
        img_label1.config(image=img1)
        img_label1.pack(padx=10,pady=10 )
    except FileNotFoundError:
        baoloi.pack(padx=10,pady=10)
        baoloi.config(text='Không tìm thấy file')
    except     IsADirectoryError:
        baoloi3.config(text="Đây là thư mục ")
        baoloi3.pack(padx=20,pady=20)
    except AttributeError:
        baoloi2.config(text="Bạn chưa nhập đường dẫn ")
        baoloi2.pack()
but=tk.Button(root,text="Nhận dạng biển số ",command=anvao)
entry.pack()
but.pack()
root.mainloop()
