import gtts
import playsound

text=input("Enter a text You want to Convert: ")

#sound=gtts.gTTS(text,lang="en")
sound=gtts.gTTS(text,lang="hi")

sound.save("welcome.mp3")

playsound.playsound("welcome.mp3")