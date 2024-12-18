import tkinter
import pandas
import random

# initally the words_to_learn.csv is not created hence we catch the error
try:
    df =pandas.read_csv("D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/words_to_learn.csv") # creates a dataframe from the words_to_learn.csv file if exists

except FileNotFoundError:
    df = pandas.read_csv("D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/words.csv") #if the words_to_learn.csv file does not exist then the dataframe is created from the main file i.e words.csv

finally:
    words = df.to_dict(orient="records") # uses pandas to change the dataframe to dictionary...... "orient" attribute is used to create the dictionary using each row as a dictionary inside a list with key being the heading i.e German or English and value being the corresponding words


current_card = { }  #to make current card i.e a randomly selected item from the list in the next card function


screen = tkinter.Tk()
img_back = tkinter.PhotoImage(file="D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/card_back.png")
img = tkinter.PhotoImage(file="D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/card_front.png")


# this function is called to change the card from german to english which called every 3 seconds using .after() method it changes the background image, text and its colors.
def change():
    global current_card, img_back
    canvas.itemconfig(image_id , image = img_back)
    canvas.image = img_back
    canvas.itemconfig(german , text =current_card["English"],fill="white")  # the current_card holds the german and its equivalent english word hence current_card["English"] gives the english part of the word.
    canvas.itemconfig(head, fill="white")

def next_card():
    global current_card, flip_window
    screen.after_cancel(flip_window) # the method .after_cancel is used to cancel the .after() call which gets called every time the func is called hence to cancel the previous .after() call .after_cancel() is used.... flip_window is the id/variable name of the function
    current_card = random.choice(words)
    canvas.itemconfig(head,text="German",fill="black")
    canvas.itemconfig(german, text=current_card["German"],fill="black") # similar to the above function itemconfig
    canvas.itemconfig(image_id, image = img )
    flip_window = screen.after(3000,change)


#this function is called when the check button is clicked which means the user knows the words hence removing it from the words dictionary and saving the remaining words into a new csv file 
def is_known():
    words.remove(current_card)
    to_learn = pandas.DataFrame(words)
    print(len(to_learn))
    to_learn.to_csv("D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/words_to_learn.csv", index=False)  #creates a new csv file
    next_card()

screen.title("Learn German you prick!!!")
# screen.minsize(width=400, height=400)
screen.config(padx=25, pady=25, background="#b8dcc4")
flip_window = screen.after(3000, func=change)



canvas = tkinter.Canvas(width = 500, height = 350, highlightthickness=0, background="#b8dcc4")
image_id = canvas.create_image(400, 300, image = img)
head = canvas.create_text(250,100, text="German", font=("Ariel",20,"italic"))
german = canvas.create_text(250,225, text = "Word", font=("Ariel",40,"bold"))
canvas.grid(row=0, column=0,columnspan=2,padx=5,pady=5)


img1 = tkinter.PhotoImage(file="D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/right.png")
right = tkinter.Button(image=img1, borderwidth=0, highlightthickness=0, command=is_known)
right.grid(row = 1,column=1,padx=10,pady=10)

img2 = tkinter.PhotoImage(file="D:/ramesh.belbase/Desktop/leaen/LEARNING PYTHON/GRAMS/DAY-31/wrong.png")
wrong = tkinter.Button(image=img2, highlightthickness=0, borderwidth=0, command= next_card)
wrong.grid(row=1, column=0,padx=10,pady=10)

next_card()

screen.mainloop()