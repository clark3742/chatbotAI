import openai
from api_key import API_KEY
import streamlit as st
openai.api_key = st.secrets["API_KEY"]

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def gpt3_completion(prompt, engine='text-davinci-002', temp=.9, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['AI:', 'USER:']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text


if __name__ == '__main__':
    conversation = list()
    user_input = st.text_input(label='input') #input('USER: ')
    conversation.append('USER: %s' % user_input)
    #this line is basically a list comprehesion
    text_block = '\n'.join(conversation)
    prompt = open_file('prompt_chat.txt').replace('<<BLOCK>>', text_block)
    prompt = prompt + '\nAI:'
    response = gpt3_completion(prompt)
    st.write('AI:',response)
    conversation.append('AI: %s' % response)

    
