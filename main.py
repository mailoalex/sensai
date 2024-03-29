from taipy.gui import Gui, notify
from api import API
text = ""

results=''
# Definition of the page

button_text = "say"

# Define the content for the "About" page
home = """
# Welcome to Sensai

## Introduction
At Sensai, we offer customized education experiences tailored to your unique needs, just as TikTok delivers personalized, bite-sized content. Powered by GPT-4, Sensai uses advanced prompt engineering to curate a learning environment where the AI adapts to you, not the other way around. But we go a step further—our intelligent feedback loop gathers insights from your past interactions, ensuring that each learning session is better than the last. We're on a mission to democratize education, making it accessible, inclusive, and engaging for everyone, whether you're a student, a professional, or a lifelong learner. In a world where education often takes a one-size-fits-all approach, Sensai is the game-changer you've been waiting for. 

## How it Sensai going to create an accessible and inclusive learning experience?
Sensai relies on two important concepts: Prompt Engineering and the ability for LLM to fine tune itself by relying on the retrieval and reflection of past experiences for improvement.<sup>[[1]](https://arxiv.org/abs/2309.04658)</sup>

- **Prompt Engineering**: Sensai uses Large Language Models (LLMs), like ChatGPT, to interact with users. By leveraging the power of prompt engineering<sup>[[2]](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)</sup>, we tailor the system's responses to suit individual learning styles and requirements.<sup>[[3]](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4475995)</sup>

- **Reflection on past experiences**: Sensai has a built-in feedback loop that allows it to gather insights from previous interactions. This not only enhances its future responses but also helps in offering a truly personalized learning journey.


## Why It's Effective?

Sensai's effectiveness lies in its seamless adaptation to each user's unique needs, delivering an engaging learning experience without the need for users to master prompt engineering. 
You don't have to be an expert in crafting prompts or AI technology; Sensai simplifies the learning process for you, effortlessly tailoring content to match your learning style, much like having a personal tutor who understands your preferences. 
This approach along side the efficient Feynman model for education<sup>[[4]](https://www.colorado.edu/artssciences-advising/resource-library/life-skills/the-feynman-technique-in-academic-coaching)</sup> not only makes learning effortless but also fuels continuous improvement. Sensai continues to learns from past interactions to become an even more valuable educational companion with each engagement.

## Who Should Use This Resource?

Sensai is designed for students, educators, and anyone seeking to deepen their understanding of complex subjects. Whether you're looking for quick answers, extended study sessions, or a continuously adaptive learning partner, Sensai is your go-to platform.

## Get Started

Ready to embark on your personalized learning journey with Sensai? [Start Exploring](learn) now and experience the future of education today.

## Contact Us

Have questions or feedback? Feel free to [contact us](mailto:your-email@example.com). We're excited to hear from you and help you unlock your full learning potential!

Thank you for choosing Sensai as your educational companion. Together, we'll redefine how we learn and grow.

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
