import tkinter

screen = tkinter.Tk()

screen.title("Learn German you prick!!!")
# screen.minsize(width=400, height=400)
screen.config(padx=25, pady=25, background="#b8dcc4")

img = tkinter.PhotoImage(file="D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/card_front.png")

canvas = tkinter.Canvas(width = 500, height = 350,  background="#b8dcc4")

image_id = canvas.create_image(400, 300, image = img)
canvas.grid(row=0, column=0,columnspan=2,padx=5,pady=5)

def change():
    
    img_back = tkinter.PhotoImage(file="D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/card_back.png")
    canvas.itemconfig(image_id , image = img_back)
    canvas.image = img_back

button = tkinter.Button(text= "click", command=change)
button.grid(row=1, column=0)

screen.mainloop()