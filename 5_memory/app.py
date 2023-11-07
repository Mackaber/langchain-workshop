from playground import generate_response
import playground as pg
import streamlit as st

st.title('🦜🔗 ChatGPT clone')

pg.openai_api_key = st.sidebar.text_input('OpenAI API Key')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Say something")
if prompt:
	response = generate_response(prompt)
	# Add user message to chat history
	st.session_state.messages.append({"role": "user", "content": prompt})
	st.session_state.messages.append({"role": "assistant", "content": response})

	# Display user message in chat message container
	with st.chat_message("user"):
		st.markdown(prompt)
	# Display assistant response in chat message container
	with st.chat_message("assistant"):
		st.write(response)