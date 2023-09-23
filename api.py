# chatgpt
import os                                                                                                                                                                                                          
import openai 
from dotenv import load_dotenv
from pathlib import Path
import pyttsx3
import speech_recognition as sr
import time


load_dotenv(Path(".\.env"))


openai.api_key = os.getenv("SECRET_KEY")






class API:

    def __init__(self) -> None:
        self.engine =  pyttsx3.init()
    def chatgpt_input(self, userinput='Enter prompt'):
        
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                                                messages=[{"role": "user",
                                                            "content":userinput }])
        return completion
        




    def TextToSpeech(self,answer):
        
        self.engine.say(answer)
        
        self.engine.runAndWait()

        # time.sleep(2)
        # self.engine.stop()



    def SpeechToText(self):

        MyText ="something  went wrong"
        try:
            # use the microphone as source for input.
            with sr.Microphone() as source2:
                r = sr.Recognizer()
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2)
                    
                #listens for the user's input
                print("Try and say something")
                audio2 = r.listen(source2)
                    
                # Using google to recognize audio
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()

                print("Did you say ",MyText)
                #return MyText
                # SpeechToText(MyText)
                    
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            return
                
        except sr.UnknownValueError:
            print("unknown error occurred") 
            return  
            
        self.TextToSpeech(MyText)
        
    # Loop infinitely for user to
    # speak



if __name__ == "__main__":
    api = API()
    api.SpeechToText()
