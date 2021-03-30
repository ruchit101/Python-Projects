from tkinter import *
from PIL import Image,ImageTk

root= Tk()
root.geometry("710x450")
root.title("My Newspaper")
D = Label(text="Date:-07.06.2020", bg="black", fg="white", borderwidth=3, padx=5, pady=5, relief=SUNKEN)
D.pack()
# Header
Name= Label(text = "Economics Times", bg="white",fg="black",font="arial 50 bold")
Name.pack(side=TOP)
line=Label(text="________________________________________________________________________________________________________________________________________________________________________")
line.pack()
# news 1
news1= Label(text = ''' Abdul Rashid Salim Salman Khan is an Indian \nfilm actor, producer, occasional playback singer and television personality. In a film career spanning \nalmost thirty years, Khan has received numerous awards, including two National Film Awards as a film \nproducer, and two Filmfare Awards for acting. He has a significant following in Asia and the Indian \ndiaspora worldwide, and is cited in the media as one of the most commercially successful actors of Indian \ncinema. According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was \nthe highest ranked Indian with 82nd rank with earnings of $37.7 million.''',
             bg="white",fg="black",font="calibri 12",relief = SUNKEN)
news1.place(x=50, y=150)

photo=Image.open("PHOTO.jpg")
picture=ImageTk.PhotoImage(photo)
pic=Label(image=picture,relief=SUNKEN)
pic.place(x=50, y=300)

#news2

news2= Label(text = ''' Abdul Rashid Salim Salman Khan is an Indian \nfilm actor, producer, occasional playback singer and \ntelevision personality. In a film career spanning \nalmost thirty years, Khan has received numerous awards,\n including two National Film Awards as a film \nproducer, and two Filmfare Awards for acting. He has a \nsignificant following in Asia and the Indian \ndiaspora worldwide, and is cited in the media as one of\n the most commercially successful actors of Indian \ncinema. According to the Forbes 2018 list of Top-Paid 100\n Celebrity Entertainers in world, Khan was \nthe highest ranked Indian with 82nd rank with earnings of $37.7 million.''',
             bg="white",fg="black",font="calibri 12",relief = SUNKEN,justify=LEFT)
news2.place(x=800, y=150)
#image
photo1= PhotoImage(file="download.png")
pic1 = Label(image=photo1,relief=SUNKEN,)
pic1.place(x=900,y=400)
root.mainloop()