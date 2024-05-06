import tkinter
import customtkinter
from pytube import YouTube

def start_download():
    print

#system setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#adding UI elements
label = customtkinter.CTkLabel(app, text="Insert youtube link here", font=("calibri", 15))
label.pack(padx=10, pady=10)

#link input
url_link = tkinter.StringVar()
link = customtkinter.CTkEntry(app, textvariable= url_link, width= 350, height=30)
link.pack()

#download button
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=15, pady=15)

#Run app
app.mainloop()
