import streamlit as st


def legal():
    with st.expander("Legal Info"):  # Element 5
        st.write(
            "<br><a href='https://linktr.ee/arm_andreasian_' style='color:gray;'>Armen-Jean Andreasian</a> "
            "<br>Free Apps for All © 2023",
            unsafe_allow_html=True)
    footer_container = st.container()
    footer_container.markdown(
        """
        <style>
        .disclaimer {
            padding: 10px;
            background-color: yellow;
            color: black;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


