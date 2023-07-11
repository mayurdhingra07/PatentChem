import streamlit as st
from chemcrow.agents import ChemCrow

# Add a sidebar for entering the OpenAI API Key
openai_api_key = st.sidebar.text_input("Enter OpenAI API Key", type="password")

# If the API Key is provided, run the ChemCrow model
if openai_api_key:
    chem_model = ChemCrow(model="gpt-3.5-turbo-0613", temp=0.1, verbose=True)

    # Create a text input for the user query
    user_input = st.text_input("Enter your query:")

    # When the user enters a query and presses the 'Generate Response' button,
    # generate a response using the ChemCrow model
    if st.button("Generate Response"):
        with st.spinner('Generating response...'):
            response = chem_model.run(user_input)
        st.write(f"Response: {response}")
else:
    st.sidebar.warning("Please enter your OpenAI API Key")

