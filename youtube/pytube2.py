from pytube import YouTube

def YouTubeDownloader(url):
    yt = YouTube(url)
    yt = yt.streams.get_highest_resolution()
    
    try:
        yt.download()
        print("done")
    except:
        print("error")
        

url = "https://www.youtube.com/watch?v=bK4PP9OwlsI"
# url = input("enter your YouTube url: ")
YouTubeDownloader(url)

