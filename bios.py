import tkinter as tk
from tkinter import *
from PIL import Image,  ImageTk

def Anmol_bio():
    root1 = tk.Tk()
    photo1 = Image.open(r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Anmol KC.jpg')
    image1 = ImageTk.PhotoImage(photo1)
    panel1 = Label(root1, image=image1)
    panel1.pack(side=tk.LEFT)

    text1 = tk.Text(root1, height=15, width=45)
    scroll1 = tk.Scrollbar(root1, command=text1.yview)
    text1.configure(yscrollcommand=scroll1.set)
    text1.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text1.tag_configure('big', font=('Verdana', 20, 'bold'))
    text1.tag_configure('color',
                        foreground='#476042',
                        font=('Tempus Sans ITC', 12, 'bold'))
    text1.insert(tk.END, '\nAnmol KC\n', 'big')
    quote1 = """
To be, or not to be that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
            """
    text1.insert(tk.END, quote1, 'color')
    text1.pack(side=tk.LEFT)
    scroll1.pack(side=tk.RIGHT, fill=tk.Y)

    root1.wm_title("Anmol's Bio")

    root1.bind("n", lambda x: root1.destroy())
    root1.mainloop()

def Daya_bio():
    root2 = tk.Tk()
    photo2 = Image.open(
        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Dayahang Rai.jpg')
    image2 = ImageTk.PhotoImage(photo2)
    panel2 = Label(root2, image=image2)
    panel2.pack(side=tk.LEFT)

    text2 = tk.Text(root2, height=15, width=45)
    scroll2 = tk.Scrollbar(root2, command=text2.yview)
    text2.configure(yscrollcommand=scroll2.set)
    text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    text2.tag_configure('color',
                        foreground='#476042',
                        font=('Tempus Sans ITC', 12, 'bold'))
    text2.insert(tk.END, '\nDayahang Rai\n', 'big')
    quote2 = """
To be, or not to be that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
            """
    text2.insert(tk.END, quote2, 'color')
    text2.pack(side=tk.LEFT)
    scroll2.pack(side=tk.RIGHT, fill=tk.Y)

    root2.wm_title("Dayahang Rai's Bio")

    root2.bind("n", lambda x: root2.destroy())
    root2.mainloop()

def Kabita_bio():
    root3 = tk.Tk()
    photo3 = Image.open(
        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Kabita Ale.jpg')
    image3 = ImageTk.PhotoImage(photo3)
    panel3 = Label(root3, image=image3)
    panel3.pack(side=tk.LEFT)

    text3 = tk.Text(root3, height=15, width=45)
    scroll3 = tk.Scrollbar(root3, command=text3.yview)
    text3.configure(yscrollcommand=scroll3.set)
    text3.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text3.tag_configure('big', font=('Verdana', 20, 'bold'))
    text3.tag_configure('color',
                        foreground='#476042',
                        font=('Tempus Sans ITC', 12, 'bold'))
    text3.insert(tk.END, '\nKabita Ale\n', 'big')
    quote3 = """
To be, or not to be that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
            """
    text3.insert(tk.END, quote3, 'color')
    text3.pack(side=tk.LEFT)
    scroll3.pack(side=tk.RIGHT, fill=tk.Y)

    root3.wm_title("Kabita Ale's Bio")

    root3.bind("n", lambda x: root3.destroy())
    root3.mainloop()


def Upasna_bio():
    root4 = tk.Tk()
    photo4 = Image.open(r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Upasna.jpg')
    image4 = ImageTk.PhotoImage(photo4)
    panel4 = Label(root4, image=image4)
    panel4.pack(side=tk.LEFT)

    text4 = tk.Text(root4, height=15, width=45)
    scroll4 = tk.Scrollbar(root4, command=text4.yview)
    text4.configure(yscrollcommand=scroll4.set)
    text4.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text4.tag_configure('big', font=('Verdana', 20, 'bold'))
    text4.tag_configure('color',
                        foreground='#476042',
                        font=('Tempus Sans ITC', 12, 'bold'))
    text4.insert(tk.END, '\nUpasna Singh Thakuri\n', 'big')
    quote4 = """
To be, or not to be that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
        """
    text4.insert(tk.END, quote4, 'color')
    text4.pack(side=tk.LEFT)
    scroll4.pack(side=tk.RIGHT, fill=tk.Y)

    root4.wm_title("Upasna's Bio")

    root4.bind("n", lambda x: root4.destroy())
    root4.mainloop()


def Wilson_bio():
    root5 = tk.Tk()
    photo5 = Image.open(
        r'C:\Users\sanam\Desktop\MovieCharacter\FaceRecognition-master (Nepali)\facesrecognized\Wilson Rai.jpg')
    image5 = ImageTk.PhotoImage(photo5)
    panel5 = Label(root5, image=image5)
    panel5.pack(side=tk.LEFT)

    text5 = tk.Text(root5, height=15, width=45)
    scroll5 = tk.Scrollbar(root5, command=text5.yview)
    text5.configure(yscrollcommand=scroll5.set)
    text5.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text5.tag_configure('big', font=('Verdana', 20, 'bold'))
    text5.tag_configure('color',
                        foreground='#476042',
                        font=('Tempus Sans ITC', 12, 'bold'))
    text5.insert(tk.END, '\nWilson Rai\n', 'big')
    quote5 = """
To be, or not to be that is the question:
Whether 'tis Nobler in the mind to suffer
The Slings and Arrows of outrageous Fortune,
Or to take Arms against a Sea of troubles,
            """
    text5.insert(tk.END, quote5, 'color')
    text5.pack(side=tk.LEFT)
    scroll5.pack(side=tk.RIGHT, fill=tk.Y)

    root5.wm_title("Wilson Rai's Bio")

    root5.bind("n", lambda x: root5.destroy())
    root5.mainloop()