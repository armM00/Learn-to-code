import streamlit as st


def tools():
    st.write('<style>div.row-widget.stButton > button:first-child '
             '{ width: 100%; background-color: #074986; color: #FFFFFF; border-color: #0072C6; } '
             'div.row-widget.stButton > button:first-child:hover { background-color: #005EA2; border-color: #005EA2; } '
             'div.row-widget.stButton > button:first-child:active { background-color: #003B6F; border-color: #003B6F; '
             '}</style>',
             unsafe_allow_html=True)

    with st.expander("Learning tools"):
        col1, col2 = st.columns(2)
        with col1:
            # ChatGPT
            chat_gpt_url = "https://chat.openai.com/chat"
            if st.button("ChatGPT", key="chat_gpt"):
                st.write(f"[Visit]({chat_gpt_url})", unsafe_allow_html=True)

        with col2:
            # Evernote
            chat_gpt_url = "https://www.evernote.com/client/web?login=true#?anb=true&"
            if st.button("Evernote", key="Evernote"):
                st.write(f"[Visit]({chat_gpt_url})", unsafe_allow_html=True)
