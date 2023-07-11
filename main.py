import streamlit as st
from agents.chemcrow import ChemCrow
from agents.tools import make_tools
from agents.prompts import QUESTION_PROMPT
from langchain import BaseLanguageModel

# Ask the user for their OpenAI API key
api_key = st.text_input("Enter your OpenAI API key", type="password")

# If the API key has been entered, set up the ChemCrow agent
if api_key:

    # Create an instance of BaseLanguageModel (you'll need to provide the necessary parameters)
    llm = BaseLanguageModel(api_key)

    # Create the tools
    tools = make_tools(llm)

    # Create an instance of ChemCrow
    chemcrow = ChemCrow(tools=tools)

    # Create a text input for the user to enter their query
    user_input = st.text_input("Enter your query")

    # If the user has entered a query, generate a response using the ChemCrow agent
    if user_input:
        prompt = QUESTION_PROMPT.format(input=user_input)
        with st.spinner("Generating response..."):
            response = chemcrow.run(prompt)
        st.write(f"Response: {response}")

# If the API key has not been entered, display a warning message
else:
    st.warning("Please enter your OpenAI API key")
