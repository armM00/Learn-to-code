import streamlit as st


def com():

    st.write('<style>div.row-widget.stButton > button:first-child '
             '{ width: 100%; background-color: #074986; color: #FFFFFF; border-color: #0072C6; } '
             'div.row-widget.stButton > button:first-child:hover { background-color: #005EA2; border-color: #005EA2; } '
             'div.row-widget.stButton > button:first-child:active { background-color: #003B6F; border-color: #003B6F; '
             '}</style>',
             unsafe_allow_html=True)
    with st.expander("Communities"):
        col1, col2 = st.columns(2)

        with col1:
            url = "https://discord.gg/pythonhow-862322959648948225"
            if st.button("PythonHow"):
                st.write(f"[Visit]({url})", unsafe_allow_html=True)

        with col2:
            url = "https://discord.gg/bydpp"
            if st.button("Build your dream's python project", key="bydpp"):
                st.write(f"[Visit]({url})", unsafe_allow_html=True)
