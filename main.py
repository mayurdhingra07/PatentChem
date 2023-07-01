import streamlit as st
import openai
os.environ["OPENAI_API_KEY"] = "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"
from chemcrow.agents import ChemCrow
chem_model = ChemCrow(model="gpt-3.5-turbo-0613", temp=0.1, verbose=True)
chem_model.run("What is the molecular weight of tylenol?")
