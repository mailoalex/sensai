from taipy.gui import Gui, notify
from api import API
text = ""

results=''
# Definition of the page

button_text = "say"

# Define the content for the "About" page
home = """
# Welcome to SensAI

## Introduction

SensAI is revolutionizing the educational landscape by providing an intelligent, adaptive learning experience for students. In an age where one-size-fits-all models of education fall short, SensAI aims to bridge the gap between learning resources and individual needs using state-of-the-art machine learning technology.

### Inspiration
At SensAI, we draw inspiration from platforms like TikTok, where technology has the power to engage millions of users daily. Just as TikTok's recommendation algorithm customizes content to fit each user's preferences, we aim to bring The individualized approach of SensAI ensures that learning is targeted and efficient. Because it adapts to each user's needs, the system provides a highly engaging learning experience that conventional resources can't match. Furthermore, SensAI's capability to learn from past interactions allows it to constantly improve and better serve the needs of each learner.
Our Inspiration comes from the idea that learning should be as unique as each individual. Tiktok's success demonstrates the incredible potential for personalized technology experiences, and we're excited to bring that same level of excitement to the realm of education with SensAI.

## How is SensAI going to create an adaptable learning experience for students?

SensAI relies on two important concepts: Prompt Engineering and the ability for LLM to fine tune itself by relying on the retrieval and reflection of past experiences for improvement.<sup>[[1]](https://arxiv.org/abs/2309.04658)</sup>

- **Prompt Engineering**: SensAI uses Large Language Models (LLMs), like ChatGPT, to interact with users. By leveraging the power of prompt engineering<sup>[[2]](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)</sup>, we tailor the system's responses to suit individual learning styles and requirements.<sup>[[3]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4475995)</sup>

- **Reflection on past experiences**: SensAI has a built-in feedback loop that allows it to gather insights from previous interactions. This not only enhances its future responses but also helps in offering a truly personalized learning journey.


## Why It's Effective

SensAI's effectiveness lies in its seamless adaptation to each user's unique needs, delivering an engaging learning experience without the need for users to master prompt engineering. 
You don't have to be an expert in crafting prompts or AI technology; SensAI simplifies the learning process for you, effortlessly tailoring content to match your learning style, much like having a personal tutor who understands your preferences. 
This approach along side the efficient Feynman model for education<sup>[[4]](https://www.colorado.edu/artssciences-advising/resource-library/life-skills/the-feynman-technique-in-academic-coaching)</sup> not only makes learning effortless but also fuels continuous improvement. SensAI continues to learns from past interactions to become an even more valuable educational companion with each engagement.

## Who Should Use This Resource

SensAI is designed for students, educators, and anyone seeking to deepen their understanding of complex subjects. Whether you're looking for quick answers, extended study sessions, or a continuously adaptive learning partner, SensAI is your go-to platform.

## Get Started

Ready to embark on your personalized learning journey with SensAI? [Start Exploring](learn) now and experience the future of education today.

## Contact Us

Have questions or feedback? Feel free to [contact us](mailto:your-email@example.com). We're excited to hear from you and help you unlock your full learning potential!

Thank you for choosing SensAI as your educational companion. Together, we'll redefine how we learn and grow.

"""

speech_to_text="""
# Speech to Text 
"""

text_to_speech="""
#  Text to Speech
<|{text}|input|>
"""


learn = """

# Start Now!

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
    "learn":learn,
  
}

if __name__ == "__main__":
    Gui(pages=pages).run()
