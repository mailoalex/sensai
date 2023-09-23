from taipy.gui import Gui, notify
from api import API
text = ""

results=''
# Definition of the page

button_text = "say"

home="""
# Welcome to SensAI

## This is the home page

"""

speech_to_text="""
# Speech to Text 
"""

text_to_speech="""
#  Text to Speech
<|{text}|input|>
"""


search = """

# Welcome to SensAI

<|{text}|input|>

<|Search|button|on_action=on_button_action|>

<|{results}|>

<|say|button|on_action=say_chatgpt_results|>
<|Stop Speech|button|on_action=stop_speech|>

~~
"""
api = API()


def stop_speech():
    api.engine.stop()

def say_chatgpt_results(state):
   
    api.TextToSpeech(state.results)
 
    

def on_button_action(state):
    state.results = 'Loading......'
    data = api.chatgpt_input(state.text)
    data = data["choices"][0]["message"]["content"]
    
    state.results = data 
    results = data
   
    

    notify(state, 'permission', f"SENT \"{state.text}\" to the API!")

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return


pages = {
    "/":"<|toggle|theme|>\n<center>\n<|navbar|>\n</center>",
    "home":home,
    "search":search,
  
}

if __name__ == "__main__":
    Gui(pages=pages).run()
