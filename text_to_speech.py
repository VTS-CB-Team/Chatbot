# import subprocess
# from gtts import gTTS
# # from mpyg321.mpyg321 import MPyg321Player
# # player = MPyg321Player()
# mytext = 'Chào mừng đến dự án'

# # language = "vi-VI"
# myobj = gTTS(text=mytext,lang="vi")
# myobj.save("welcome.mp3")

# #play
# subprocess.call(['mpg321',"C:/Users/LENOVO/rasa_des_ver2/rasa_test_demo/welcome.mp3",'--play-and-exit'],shell=True)



from gtts import gTTS
import playsound


text = "học bổng" 
def texttospeech(text):
    output = gTTS(text,lang="vi", slow=False)
    output.save("output_final.mp3")
    playsound.playsound(R'C:\Users\LENOVO\rasa_des_ver2\Chatbot\output_final.mp3', True)

# texttospeech("Bạn khỏe không")