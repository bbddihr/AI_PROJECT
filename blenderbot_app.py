import streamlit as st
import pandas as pd
from streamlit_chat import message
import requests
 
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
 
st.header("🤖 치매봇 (Demo)")

 
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
 
if 'past' not in st.session_state:
    st.session_state['past'] = []
 
# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()
def response(message,headers=headers, json=payload):
    # additional_input_info의 텍스트를 챗봇의 대답 뒤에 추가합니다.
    response = predict(model, message, dataset.wordvocab.index2word, device)
    return response 
 
with st.form('form', clear_on_submit=True):
    user_input = st.text_input('You: ', '', key='input')
    submitted = st.form_submit_button('Send')
 
if submitted and user_input:
    output = response({
        "inputs": {
            "past_user_inputs": st.session_state.past,
            "generated_responses": st.session_state.generated,
            "text": user_input,
        },
        "parameters": {"repetition_penalty": 1.33},
    })
 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output["generated_text"])
 
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))