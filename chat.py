import streamlit as st
import ollama

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Image
image_url = "https://images.unsplash.com/photo-1677442136019-21780ecad995"

st.image(
    image_url,
    caption="AI Chatbot",
    use_container_width=True
)

# Title
st.title("🤖 AI Chatbot")
st.caption("Ask anything and get an answer from Llama 3.2")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("Enter your question...")

if prompt:

    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    try:
        # Get response from Ollama
        response = ollama.chat(
            model="llama3.2",
            messages=st.session_state.messages
        )

        answer = response["message"]["content"]

        # Display AI response
        with st.chat_message("assistant"):
            st.write(answer)

        # Save AI response
        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        st.error("Error connecting to Ollama.")
        st.write(e)

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()