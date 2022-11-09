import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download():
    result.set("downloading ...")
    tk.update
    
    flagOK = True
    msgTitle = "My YT Downloader"
    
    url = txtUrl.get().strip()
    if url == "":
        tk.messagebox.showerror(msgTitle,"the url was invalid")
        flagOK = False
    
    if flagOK:
        yt = YouTube(url)
        yt = yt.streams.get_highest_resolution()
        
        """
        if yt.length > 300:
            ans = tk.messagebox.askokcancel(msgTitle, "the clip looks too long.\do you want to download ?")
            flagOK = (ans == "ok")
        else:
            tk.messagebox.showinfo(msgTitle,"the clip is not too long")
        
        flagOK = False
        """
            
        if flagOK:
            try:
                yt.download()
                result.set("ok, the YouTube was downloaded successfully")
            except:
                result.set("fail, some error was found")



root = tk.Tk()
root.title("My YouTube Downloader")
root.geometry("400x100")

result = tk.StringVar()
result.set("")

lblUrl = tk.Label(root, text = "Please enter your YouTube url: ", anchor = tk.W)
lblUrl.grid(row = 0, column = 0)

txtUrl = tk.Entry(root, width = 65) #.grid(row = 1, column = 1)
txtUrl.grid(row = 1, column = 0)

btnStart = tk.Button(root, text = "Convert to MP4", command = download)
btnStart.grid(row = 2, column = 0)

lblResult = tk.Label(root, textvariable = result)
lblResult.grid(row = 3, column = 0)


root.mainloop()
quit()
