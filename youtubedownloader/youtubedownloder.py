import pytube
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

root = Tk()
root.title('Youtube Downloader')
root.geometry('700x500')




   




# url = 'https://www.youtube.com/watch?v=4SFhwxzfXNc'
# my_video = pytube.YouTube(url)

# check_availiability = my_video.check_availability()



entry = Entry(root, width=50)
entry.pack(side = TOP, pady = 2)



def search_link ():    
    my_video = pytube.YouTube(entry.get())
    print(my_video.title)
    # video_title.config(text = my_video.title, font = ('Helvetica 15'))


def download_video():
    my_video = pytube.YouTube(entry.get())
    video = my_video.streams.get_highest_resolution()
    video.download('./Downloads')






# m = Menu(root, tearoff = 0)
# m.add_command(label ="Cut")
# m.add_command(label ="Copy")
# m.add_command(label ="Paste", command=lambda:paste_selected_text())
#
# def paste_selected_text():
#     global data
#     entry.insert(root,data)
#
#
#
#
# def do_popup(event):
#     try:
#         m.tk_popup(event.x_root, event.y_root)
#     finally:
#         m.grab_release()
#
#
#
# entry.bind("<Button-2>", do_popup)


search_button = ttk.Button(root, text = "Search", command = search_link)
search_button.pack(side = TOP, pady = 10)


image = PhotoImage(file="thumbnail.png", height = 300, width = 500)
img = Label(root, image=image)
img.pack(side=TOP, pady=2)

video_title = ttk.Label(root, text=" ")
video_title.pack(side=TOP, pady=2)


button_one = Radiobutton(root, text="Lowest Resolution")
button_one.pack(side = LEFT)

button_two = Radiobutton(root, text="Highest Resolution")
button_two.pack(side = LEFT)

button_three = Radiobutton(root, text="audio only")
button_three.pack(side = LEFT)


download_button = ttk.Button(root, text = "Download", command = download_video)
download_button.pack(side= RIGHT, pady = 2)





# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Paste Youtube Link:").grid(column=0, row=0)

# e = Entry()



# ttk.Entry(frm, textvariable = input_link).grid(column=0, row=1)
# ttk.Button(frm, text="Download", command=root.destroy).grid(column=0, row=2)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=3)
root.mainloop()