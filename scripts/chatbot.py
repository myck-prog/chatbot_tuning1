from chat_functions import *
import streamlit as st
import streamlit as st
import os
from chat_functions import *
import streamlit as st
from langchain.schema.messages import HumanMessage, AIMessage


def show():
    # Prepare the documents

    doc_id = 1
    try:
        directory = 'data'
        doc_dict[doc_id] = create_documents(directory=directory, glob='*.csv')
    except:
        doc_dict[doc_id] = create_documents_from_csv()
        print('Done creating doc from CSV')
    retriever_dict = create_retriever(doc_dict[doc_id], 'recycle')
    description_dict['recycle'] = """
    This document provides information from the Recycle BC website or BC government 
    website. It has the most specific information 
    about whether or not an item is accepted for recycling and where to recycle it.
    This should be the main resource for recycling information for residents of British Columbia.
    """

    doc_id = 2
    try:
        directory = 'data'
        doc_dict[doc_id] = create_documents(
            directory=directory, glob='*.txt', loader_cls=TextLoader)
    except:
        directory = '../data'
        doc_dict[doc_id] = create_documents(
            directory=directory, glob='*.txt', loader_cls=TextLoader)
    retriever_dict = create_retriever(doc_dict[doc_id], 'mattress')
    description_dict['mattress'] = """
    Information from the City of Vancouver website about how to recycle mattresses.
    """
    tool_id = 1
    tool_dict[tool_id] = create_tools_list(retriever_dict, description_dict)

    conversation_id = 1
    input_id = 1

    conversation_dict[conversation_id] = create_chatbot(
        tool_dict[tool_id], streamlit=True)

    # Start the conversation
    st.title("Recycle Pro Bot!  ")
    """
    # RecyclePro Bot

    """
    # Initialize chat history
    # Initialization
    if 'key' not in st.session_state:
        st.session_state['key'] = 'langchain_messages'

    if "messages" not in st.session_state:
        st.session_state.messages = []
    # print(f'\nsession state: {st.session_state}')
    print(f'\nsession state messages: {st.session_state.messages}')
    # print(f'\nsession state: {st.session_state["langchain_messages"]}')
    # for index, message in enumerate(st.session_state['langchain_messages']):
    #     # if (message.content == ''):
    #     #     pass
    #     # elif type(message.content) == HumanMessage:
    #     if type(message.content) == HumanMessage:
    #     # elif index % 2 == 0:
    #         with st.chat_message("user"):
    #             st.write(f'{message.content}')
    #     elif type(message.content) == SystemMessage:
    #     # else:
    #         with st.chat_message("assistant"):
    #             st.write(f'{message.content}')
    #     else:
    #         print('not system or user message')

    for message in st.session_state.messages:
        if message['role'] == "user":
            with st.chat_message("user"):
                st.write(f'{message["content"]}')
        elif message['role'] == "assistant":
            print(f'Assistant message: {message["content"]}')
            with st.chat_message("assistant"):
                st.write(f'{message["content"]}')

    print(f'session state messages: {st.session_state.messages}')
    # print(f'langchain messages: {st.session_state["langchain_messages"]}')
    # Set a default model
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo-16k"

    # prompt =  st.chat_input('Say something')
    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        answer_dict[conversation_id] = chat_with_chatbot(
            prompt, conversation_dict[conversation_id], streamlit=True
        )
        chatbot_response = answer_dict[conversation_id]['output']
        st.session_state.messages.append(
            {"role": "assistant", "content": chatbot_response})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            st.markdown(chatbot_response)
