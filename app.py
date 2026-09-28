import streamlit as st
import ollama
# Image URL
image_url = "https://images.unsplash.com/photo-1677442136019-21780ecad995"

st.image(image_url, caption="AI Chatbot", use_container_width=True)


st.title("AI Chatbot")
st.caption("Ask something")

prompt = st.text_input("Enter your question:")

if st.button("Send", key="send_button"):
    response = ollama.chat(
        model="llama3.2",
        messages=[{
                "role": "user",
                "content": "prompt"
            }]
    )

    st.write(response["message"]["content"])

  