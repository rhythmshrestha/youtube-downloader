import tkinter
import customtkinter
from pytube import YouTube

def start_download():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback= on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text= ytObject.title)
        finish_label.configure(text="")
        video.download()
        finish_label.configure(text="Download Completed", text_color="green")
    except Exception as e:
        finish_label.configure(text=f"Download Error, {str(e)}", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    progress_percentage.configure(text= per +"%")
    progress_percentage.update()

    # update progress bar
    progress_bar.set(float(percentage_of_completion) / 100)

#system setting
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#adding UI elements
title = customtkinter.CTkLabel(app, text="Insert youtube link here", font=("calibri", 15))
title.pack(padx=10, pady=10)

#link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, textvariable= url_var, width= 350, height= 30)
link.pack()

#download button
download = customtkinter.CTkButton(app, text="Download", command=start_download)
download.pack(padx=15, pady=15)

#finished download
finish_label = customtkinter.CTkLabel(app, text="")
finish_label.pack()

#progress percentage
progress_percentage = customtkinter.CTkLabel(app, text="0%")
progress_percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack()

#Run app
app.mainloop()
