import requests
import speech_recognition as sr     # import the library
# import subprocess
from gtts import gTTS
# import playsound

from text_to_speech import texttospeech
# sender = input("What is your name?\n")

bot_message = ""
message=""

r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Học hệ thống thông tin quản lý ra trường làm gì ạ?"})

print("Bot says, ",end=' ')
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

# myobj = gTTS(text=bot_message)
# myobj.save("ok.mp3")
# print('Đã lưu')
# # Playing the converted file
# subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])
texttospeech(bot_message)

while bot_message != "bye" or bot_message!='thanks':

    r = sr.Recognizer()  # initialize recognizer
    with sr.Microphone() as source:  # mention source it will be either Microphone or audio files.
        print("MỜi bạn nói :")
        audio = r.listen(source)  # listen to the source
        try:
            message = r.recognize_google(audio,language="vi-VI")  # use recognizer to convert our audio into text part.
            print("You said : {}".format(message))

        except:
            print("Xin lỗi bạn nói khó nghe quá! kHông hiểu đâuu.")  # In case of voice not recognized  clearly
    if len(message)==0:
        continue
    print("Gửi thông điệp...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    # myobj = gTTS(text=bot_message)
    # myobj.save("welcome.mp3")
    # print('saved')
    # # Playing the converted file
    # subprocess.call(['mpg321', "welcome.mp3", '--play-and-exit'])
    texttospeech(bot_message)