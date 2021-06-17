import pyttsx3
# connecting to sound driver by creating an object
user1=input("enter your message : ")
myaudio=pyttsx3.init()
# storing data in a buffer 
myaudio.say(user1)
# now asking to speaker to run the data 


#  save to a mp3 file
myaudio.save_to_file(user1, 'lnb.mp3')
myaudio.runAndWait()

