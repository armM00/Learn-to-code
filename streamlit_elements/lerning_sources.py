import streamlit as st


def sources():

    st.write('<style>div.row-widget.stButton > button:first-child '
             '{ width: 100%; background-color: #074986; color: #FFFFFF; border-color: #0072C6; } '
             'div.row-widget.stButton > button:first-child:hover { background-color: #005EA2; border-color: #005EA2; } '
             'div.row-widget.stButton > button:first-child:active { background-color: #003B6F; border-color: #003B6F; '
             '}</style>',
             unsafe_allow_html=True)
    with st.expander("Learning primary resources"):
        st.info("“For the things we have to learn before we can do them, we learn by doing them” - Aristotle")

        col1, col2, col3 = st.columns(3)
        with col1:
            link = "https://www.freecodecamp.org/learn/"
            st.info(
                "FreeCodeCamp is a great learning resource for programming. Visit their website for interactive coding challenges, tutorials, and more.")
            if st.button("freeCodeCamp website courses", key="freecodecamp"):
                st.write(f"[Visit freeCodeCamp]({link})")

            link3 = "https://www.sololearn.com/learn"
            st.info(
                "SoloLearn provides courses in various programming languages, including HTML, Python, JavaScript, Kotlin, C#, C++, JS and much much more.")
            if st.button("SoloLearn website courses"):
                st.write(f"[Visit SoloLearn]({link3})")

            link_udemy = "https://www.udemy.com/"
            st.info("Udemy is an online learning platform with a wide range of courses in various fields including IT. It offers both free and paid courses.")
            if st.button("Udemy courses"):
                st.write(f"[Visit Udemy]({link_udemy})")

        with col2:
            # freecodecamp
            link2 = "https://www.youtube.com/@freecodecamp/videos"
            st.info(
                "freeCodeCamp's YouTube channel offers a wide range of programming video-tutorials, live coding sessions, and coding interviews.")
            if st.button("freeCodeCamp YouTube tutorials"):
                st.write(f"[Visit freeCodeCamp YouTube Channel]({link2})")

            # stepik
            link_stepik = "https://stepik.org/catalog/search?free=true&lang=en"
            st.info("Stepik offers numerous free and paid courses in different fields including IT. Some courses are in Russian, but it's possible to find courses in English.")
            if st.button("Stepik courses"):
                st.write(f"[Visit Stepik]({link_stepik})")

            link_coursera = "https://www.coursera.org/"
            st.info("Coursera is an online learning platform that offers courses from top universities and institutions around the world.")
            if st.button("Coursera courses"):
                st.write(f"[Visit Coursera]({link_coursera})")




        with col3:
            # w3schools
            link_w3schools = "https://my-learning.w3schools.com/tutorials"
            st.info("W3Schools is a top learning resource. It provides web development tutorials and references for enormous amount of languages.")
            if st.button("W3Schools courses and tutorials", key="w3schools"):
                st.write(f"[Visit W3Schools]({link_w3schools})")

            # edx
            link_edx = "https://www.edx.org/"
            st.info(
                "edX is an online learning platform that offers university-level courses from renowned institutions around the world.")
            if st.button("edX courses"):
                st.write(f"[Visit edX]({link_edx})")

            # khan academy
            link_khanacademy = "https://www.khanacademy.org/"
            st.info(
                "Khan Academy provides free educational resources in various subjects, including math, science, programming, and much more.")
            if st.button("Khan Academy courses"):
                st.write(f"[Visit Khan Academy]({link_khanacademy})")



