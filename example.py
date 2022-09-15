import streamlit as st
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link
import json

st.write(f"User agent is {streamlit_js_eval(js_expressions='window.navigator.userAgent', want_output = True, key = 'UA')}")

st.write(f"Screen width is {streamlit_js_eval(js_expressions='screen.width', want_output = True, key = 'SCR')}")

st.write(f"Browser language is {streamlit_js_eval(js_expressions='window.navigator.language', want_output = True, key = 'LANG')}")

st.write(f"Page location is { streamlit_js_eval(js_expressions='window.location.origin', want_output = True, key = 'LOC')}")

# Copying to clipboard only works with a HTTP connection

copy_to_clipboard("Text to be copied!", "Copy something to clipboard (only on HTTPS)", "Successfully copied" , component_key = "CLPBRD")

# Share something using the sharing API
create_share_link(dict({'title': 'streamlit-js-eval', 'url': 'https://github.com/aghasemi/streamlit_js_eval', 'text': "A description"}), "Share a URL (only on mobile devices)", 'Successfully shared', component_key = 'shdemo')
                
