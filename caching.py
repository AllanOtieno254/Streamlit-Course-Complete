#cache dat is used for immutable data

import streamlit as st
import time

@st.cache_data(ttl=60)  #cache this data for 60sec
def get_data():
    #simulate a slow data-fetching process
    time.sleep(5)  # Delays to mimic an API Call
    return {"data": "This is cached data"}  # return a dictionary

st.write("fetching data...")
data = get_data()
st.write("data fetched", data)


#cache resource
import streamlit as st
import time

@st.cache_resource
def load_resource():
    # Simulate an expensive resource initialization (e.g., a database connection)
    time.sleep(5)  # Delay to mimic a heavy initialization process
    resource = "Expensive Resource Loaded!"
    return resource

# Fetch the cached resource
resource = load_resource()

st.write("Cached resource:", resource)
