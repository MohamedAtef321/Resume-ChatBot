
import streamlit as st
from chatbot import Bot

# # Create columns with appropriate widths
# col1, col2, col3 = st.columns([1, 3, 1])

# # Display the image in the center column
# with col2:
  
# st.image("GP1_Dark_Blue_2.png", caption="A picture of me", width=200)

st.title("Welcome to Mohamed Atef's Personal Assistant ! 🤖👋")

bot = Bot()

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).markdown(message["content"])

prompt = st.chat_input("Ask me anything!")

if prompt:
    st.chat_message("User").markdown(prompt)
    st.session_state["messages"].append({"role": "user", "content": prompt})
    
    answer = bot.answer_question(prompt)
    st.chat_message("assistant").write_stream(bot.stream_data(answer))
    st.session_state["messages"].append({"role": "assistant", "content": answer})
    
    