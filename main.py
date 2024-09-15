# import os
# from dotenv import load_dotenv
from openai import APIConnectionError
import openai
import streamlit as st

# txt = st.text_input("Enter prompt")
# st.write(f"You: {txt}")

prompt = """You are a book reviewer that tells the genre of a book summary with how much percent of a genre is involved and give a list of similar books. give the percentages in tabular form. Do not give extra iinformation like summary. The genres are """
promptHelperText = "onlyGenres.txt"

def getGenreInfo():
    with open(promptHelperText, 'r') as file:
        data = file.read()
    return data


def mainn():
    # load_dotenv()
    openai.api_key = ""
    client = openai.OpenAI()
    genreInfo = getGenreInfo()

    global prompt
    prompt = prompt + genreInfo
    
    inputt = st.text_input("Give me a book summary")
    while inputt != "exit":
        # inputt = input("Enter prompt: ")
        completion = client.chat.completions.create(
            model = "gpt-4o-mini",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": inputt}
            ],
            
        )
        # print(completion.choices[0].message.content)
        st.write(completion.choices[0].message.content)

        break

mainn()