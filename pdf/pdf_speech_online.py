import gtts
import playsound

mytext = "hello, Suwijak. how are you ?"
mytext += "สวัสดี ยินดีต้อนรับสู่ python lab classes"
# gtts.lang.tss_langs()
mylang = "th"

gttsObj = gtts.gTTS(text = mytext, tld = "co.uk", lang = mylang, slow = False)
# gttsObj = gtts.gTTS(text = mytext, lang = mylang, slow = False)
gttsObj.save("welcome.mp3")

playsound.playsound("welcome.mp3")


print("done")