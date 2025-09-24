import streamlit as st
import random

valorant_agents = ["Brimstone", "Viper", "Omen", "Cypher", "Sova", "Sage", 
                   "Phoenix", "Jett", "Reyna", "Raze", "Breach", "Skye", 
                   "Yoru", "Astra", "KAY/O", "Chamber", "Neon", "Fade", 
                   "Harbor", "Gekko", "Deadlock", "Iso", "Waylay", "Clove", 
                   "Vyse", "Tejo", "Killjoy"]

rig = valorant_agents + ["Iso"] * 27

st.title("Random Valorant Agent Picker")

if st.button("pick an Agnet!"):
    agent = random.choice(rig)
    st.success(f"You got: {agent}")
