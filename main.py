# import os
# from dotenv import load_dotenv
import json
from openai import APIConnectionError
import openai
import streamlit as st

# txt = st.text_input("Enter prompt")
# st.write(f"You: {txt}")

prompt = """You are a book reviewer that tells the genre of a book summary with how much percent of a genre is involved and give a list of similar books. Do not give extra information like summary. The genres are 
return the response in this exact json format:
{
    "BookName": "Name Of Book",
    "AuthorName": "Name Of Author",
    "GenreClassification": {
        "Short Story": "70",
        "Memoir & Autobiography": "30"
    },
    "SimilarBooks": ["Book1", "Book2"]
}
"""
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

        data = json.loads(completion.choices[0].message.content)

        try:
            with open("data.json", "r") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []
        existing_data.append(data)

        with open("data.json", "w") as file:
            json.dump(existing_data, file, indent=4)

        break

mainn()