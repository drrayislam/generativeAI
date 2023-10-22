#!/usr/bin/env python
# coding: utf-8
#Dr. Ray Islam - Chatbot with ChatGPT (gpt-3.5-turbo) with userdefined data

#Intstall ipywidgets for interaction with Jupyter Notebook
get_ipython().system('pip install openai ipywidgets')

#import libraries
import os
import openai
import ipywidgets as widgets
#IPython : IPython is a command shell for interactive computing in multiple programming languages
#display: This is a function in the IPython.display module that can display elements graphically in a Jupyter Notebook env.
# clear_output: This function is used to clear the output of a cell in a Jupyter Notebook. 
#It is helpful for updating cell outputs
from IPython.display import display, clear_output

#check directory
import os
print(os.getcwd())

# Change the current working directory
os.chdir('C:/Users/ray/Documents/Knowledge/daddy')

#check again
import os
print(os.getcwd())

# Get all .txt files in the current directory
txt_files = [f for f in os.listdir() if f.endswith('.txt')]

# Create a dictionary to store the content of each text file
file_contents = {}

# Read and print the content of each text file
for txt_file in txt_files:
    with open(txt_file, 'r') as file:
        content = file.read()
        file_contents[txt_file] = content
        print(f"Contents of {txt_file}:\n{content}\n" + "="*50)

#Combine all text file contents into one string
local_data = "\n".join(file_contents.values())

#Define a function to interact with GPT-3.5 Turbo:

API_KEY = '..........8eRo5lW4e................'
openai.api_key = API_KEY

def ask_gpt_turbo(question):
    #to construct the message
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": local_data},
        {"role": "user", "content": question}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response['choices'][0]['message']['content'].strip()


#Create interactive widgets for the chatbot:
input_area = widgets.Textarea(
    value='',
    placeholder='Type your question here...',
    description='Question:',
    disabled=False,
    layout=widgets.Layout(width='50%')
)

send_button = widgets.Button(description="Send")

output_area = widgets.Output(layout={'border': '1px solid black'})

def on_button_click(b):
    with output_area:
        question = input_area.value
        answer = ask_gpt_turbo(question)
        print(f"Dr. Ray: {question}\nGPT-3.5 Turbo: {answer}\n" + "-"*50)

send_button.on_click(on_button_click)

display(input_area, send_button, output_area)

