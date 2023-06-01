import streamlit as st


def train():
    st.write('<style>div.row-widget.stButton > button:first-child '
             '{ width: 100%; background-color: #074986; color: #6DAC70; border-color: #0072C6; } '
             'div.row-widget.stButton > button:first-child:hover { background-color: #005EA2; border-color: #005EA2; } '
             'div.row-widget.stButton > button:first-child:active { background-color: #003B6F; border-color: #003B6F; '
             '}</style>',
             unsafe_allow_html=True)
    with st.expander("Practice"):
        col1, col2, col3 = st.columns(3)
        with col1:
            # Codewars (KataWars)
            link_codewars = "https://www.codewars.com/"
            st.info("Codewars is a platform where you can improve your coding skills by completing coding challenges.(easy/medium)")
            if st.button("Solve Codewars problems", key="codewars"):
                st.write(f"[Visit Codewars]({link_codewars})")

            # topcodee
            link_topcoder = "https://www.topcoder.com/"
            st.info(
                "Topcoder is a platform for competitive programming challenges and coding competitions. It offers a variety of problems to solve across different domains.")
            if st.button("Topcoder problems"):
                st.write(f"[Visit Topcoder]({link_topcoder})")

        with col3:
            # hackerrank
            link = "https://www.hackerrank.com/dashboard"
            st.info(
                "HackerRank is a platform that provides coding challenges, competitions, and interview preparation "
                "materials. (easy/medium) ")
            if st.button("Solve HackerRank probs", key="19"):
                st.write(f"[Visit HackerRank]({link})")
        with col2:
            # LeetCode
            link_leetcode = "https://leetcode.com/"
            st.info("LeetCode is a great platform that offers coding challenges and interview preparation resources. (medium/hard)")
            if st.button("Solve LeetCode problems", key="leetcode"):
                st.write(f"[Visit LeetCode]({link_leetcode})")

