import streamlit as st


def tools():#
    st.write('<style>div.row-widget.stButton > button:first-child '
             '{ width: 100%; background-color: #074986; color: #FFFFFF; border-color: #0072C6; } '
             'div.row-widget.stButton > button:first-child:hover { background-color: #005EA2; border-color: #005EA2; } '
             'div.row-widget.stButton > button:first-child:active { background-color: #003B6F; border-color: #003B6F; '
             '}</style>',
             unsafe_allow_html=True)
    with st.expander("Tools"):
        col1, col2 = st.columns(2)

        with col1:
            # AI translator
            url = "https://www.deepl.com/translator"
            if st.button("DeepL AI translator", key="DeepL"):
                st.write(f"[Visit]({url})", unsafe_allow_html=True)

        with col2:
            # Rgb picker
            url = "https://redketchup.io/color-picker"
            if st.button("RGB picker", key="rgb_picker"):
                st.write(f"[Visit]({url})", unsafe_allow_html=True)
