import streamlit as st
from model_llm import get_output
from email_llm import send_email_to_user
from excel_llm import add_data_to_excel

st.title("Your Friendly Email Sending Bot")
st.header("Please fill the details before sendind mail")

name=st.text_input(label='User Name',placeholder='John')
sender_email=st.text_input(label="Sender Email",placeholder="abc@gmail.com")
st.text('The password should be "app password" from google securities')
password=st.text_input(label='Password',placeholder='********')
reciver_email=st.text_input(label='Reciver Email',placeholder='abc@gmail.com')



if name and sender_email and password and reciver_email:

    prompt=st.chat_input(placeholder="Type your message here...")
    if prompt:

        generation=get_output(prompt,name)
        print(len(generation.split("</think>")))
        reasoning=generation.split("</think>")[0]
        responce=generation.split("</think>")[1]
        subject=responce.split('\n',1)[0]
        subject=subject.replace("Subject","").strip()
        body=responce.split('\n',1)[1].strip()

        st.text(body)

        if generation:
            send_email_to_user(sender_email,password,reciver_email,subject,body)

            add_data_to_excel(name,prompt,reasoning,responce)

            st.title("Successfully Sent Mail...")





