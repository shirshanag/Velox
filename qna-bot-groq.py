from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
from langchain.agents import create_agent
from langchain_community.utilities import GoogleSerperAPIWrapper
import streamlit as st
load_dotenv()

llm=ChatGroq(model="openai/gpt-oss-20b",streaming=True)
search=GoogleSerperAPIWrapper()
tools=[search.run]
if "memory" not in st.session_state:
    st.session_state.memory=MemorySaver()
    st.session_state.history=[]


agents=create_agent(
    model=llm,
    tools=tools,
    checkpointer=st.session_state.memory,
    system_prompt="you are a amazing ai agent and can search on google as well"
)

print(st.session_state.memory)

## Building web-interface ..
st.subheader("🤖💬Velox")

for message in st.session_state.history:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)

query=st.chat_input("Ask Anything? ")

if query:
    st.chat_message("user").markdown(query)
    st.session_state.history.append({"role":"user","content":query})
    response=agents.stream(
        {"messages":[{"role":"user","content":query}]},
        {"configurable":{"thread_id":1}},
        stream_mode="messages"
        )
    # create a message container
    ai_container=st.chat_message("ai")

    with ai_container:
        # Create an empty space that can be updated
        space=st.empty() # creates a place-holder

        message=""
        for chunk in response:
            message=message+chunk[0].content
            space.write(message)

        st.session_state.history.append({"role":"ai","content":message})




    
    # answer=response["messages"][-1].content
    # st.chat_message("ai").markdown(answer)
    # st.session_state.history.append({"role":"ai","content":answer})
