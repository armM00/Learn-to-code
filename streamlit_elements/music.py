import streamlit as st


def ncs():
    with st.expander("Music"):
        st.write("Choose the genre: ")
        if st.checkbox("Lo-Fi"):
            lofi_url = "https://www.youtube.com/watch?v=jfKfPfyJRdk&ab_channel=LofiGirl"
            st.video(lofi_url)

        if st.checkbox("40's Jazz Classics"):
            jazz_url = "https://youtu.be/o0BgZdkyNro"
            st.video(jazz_url)

        if st.checkbox("Funk/Soul"):
            funk_url = "https://youtu.be/jRrWVMmNYEI"
            st.video(funk_url)

        if st.checkbox("Bob Marley"):
            reggae_url = "https://youtu.be/gGagPdT3L-s"
            st.video(reggae_url)

        if st.checkbox("Bossa nova"):
            bossa = "https://youtu.be/uj-fZfscY9Y"
            st.video(bossa)
