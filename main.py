import tkinter






screen = tkinter.Tk()

screen.title("Learn German you prick!!!")
# screen.minsize(width=400, height=400)
screen.config(padx=25, pady=25, background="#b8dcc4")

    


img = tkinter.PhotoImage(file="D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/card_front.png")

canvas = tkinter.Canvas(width = 500, height = 350, highlightthickness=0, background="#b8dcc4")
image_id = canvas.create_image(400, 300, image = img)
canvas.create_text(250,100, text="German", font=("Ariel",20,"italic"))
canvas.create_text(250,225, text = "Word", font=("Ariel",40,"bold"))
canvas.grid(row=0, column=0,columnspan=2,padx=5,pady=5)


def change():
    img_back = tkinter.PhotoImage(file="D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/card_back.png")
    canvas.itemconfig(image_id , image = img_back)
    canvas.image = img_back
    
    

img1 = tkinter.PhotoImage(file="D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/right.png")
right = tkinter.Button(image=img1, borderwidth=0, highlightthickness=0)
right.grid(row = 1,column=1,padx=10,pady=10)

img2 = tkinter.PhotoImage(file="D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/wrong.png")
wrong = tkinter.Button(image=img2, highlightthickness=0, borderwidth=0, command=change)
wrong.grid(row=1, column=0,padx=10,pady=10)








screen.mainloop()