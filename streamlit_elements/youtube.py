import streamlit as st


def com():

    st.write('<style>div.row-widget.stButton > button:first-child '
             '{ width: 100%; background-color: #074986; color: #FFFFFF; border-color: #0072C6; } '
             'div.row-widget.stButton > button:first-child:hover { background-color: #005EA2; border-color: #005EA2; } '
             'div.row-widget.stButton > button:first-child:active { background-color: #003B6F; border-color: #003B6F; '
             '}</style>',
             unsafe_allow_html=True)
    with st.expander("YouTubers"):
        col1, col2 = st.columns(2)

        with col1:
            url1 = "https://www.youtube.com/@Fireship"
            if st.button("Fireship (IT overall)"):
                st.write(f"[Visit]({url1})", unsafe_allow_html=True)

            url2 = "https://www.youtube.com/@NetworkChuck"
            if st.button("NetworkChuck (Cybersecurity, IT overall)"):
                st.write(f"[Visit]({url2})", unsafe_allow_html=True)

            url3 = "https://www.youtube.com/@nicholast"
            if st.button("Nicholas T.  (Jobs, IT overall)"):
                st.write(f"[Visit]({url3})", unsafe_allow_html=True)

        with col2:
            url4 = "https://www.youtube.com/@jomaoppa/videos"
            if st.button("Joma Tech (Jobs, IT overall)"):
                st.write(f"[Visit]({url4})", unsafe_allow_html=True)

            url5 = "https://www.youtube.com/@NeuralNine"
            if st.button("NeuralNine (Python) "):
                st.write(f"[Visit]({url5})", unsafe_allow_html=True)

            url6 = "https://www.youtube.com/@AZisk"
            if st.button("Alex Ziskind (AI, IT overall)"):
                st.write(f"[Visit]({url6})", unsafe_allow_html=True)
