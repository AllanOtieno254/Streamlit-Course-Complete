import streamlit as st

if "step" not in st.session_state:
    st.session_state.step = 1
    
if "info" not in st.session_state:
    st.session_state.info = {}   
    
def go_to_step2(name):
    st.session_state.info["name"] = name  # Fixed dictionary key
    st.session_state.step = 2
    
def go_to_step1():
    st.session_state.step = 1  # Fixed step reset
    
if st.session_state.step == 1:
    st.header("part 1: info") 
    
    name = st.text_input("Name", value=st.session_state.info.get("name", ""))
    
    st.button("Next", on_click=go_to_step2, args=(name,))  # Removed extra colon
     
elif st.session_state.step == 2:
    st.header("Part 2: Review")
    
    st.subheader("please review this:")
    st.write(f"**name**: {st.session_state.info.get('name', '')}")  # Fixed f-string quotes
    
    if st.button("submit"):
        st.success("Great")
        st.balloons()
        st.session_state.info = {}
    
    if st.button("back"):
        st.session_state.step = 1
