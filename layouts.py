import streamlit as st

#sidebar layout
st.sidebar.title("This is sidebar title")
st.sidebar.write("This is sidebar write")
sidebar_input = st.sidebar.text_input("Enter your name")
sidebar_button = st.sidebar.button("Submit")

#Tabs layout
tab1,tab2,tab3=st.tabs(["Tab1","Tab2","Tab3"])
with tab1:
    st.title("Tab1")
    st.write("This is tab1")
    
with tab2:
    st.title("Tab2")
    st.write("This is tab2")
    
with tab3:
    st.title("Tab3")
    st.write("This is tab3")
    
#column layout
col1,col2=st.columns(2)
with col1:
    st.title("column1")
    st.write("This is column1 content")
    
with col2:
    st.title("column2")
    st.write("This is column2 content")
    
with col2:
    st.title("column3")
    st.write("This is column3 content")
    
    
    
#container example
with st.container(border=True):
    st.title("Container")
    st.write("This is container content")
    st.write("This is container trial content")	
    st.write("This is container trial content")
    st.write("This is container trial content")
    
#empty placement
placeholder = st.empty()
placeholder.write("This is empty placement")  

if st.button("update placeholder"):
    placeholder.write("This is updated empty placement")
    
    
#expander layout
with st.expander("Click to expand"):
    st.write("This is expander content")
    st.write("This is expander content")
    st.write("This is expander content")
    st.write("This is expander content end point")
    
#over(Tooltip)
st.write("Hover over this button for a tooltip")
st.button("Hover me", help="This is a tooltip")

#sidebar input handling
if sidebar_input:
    st.write(f"Youve entered in the sidebar {sidebar_input}")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        



