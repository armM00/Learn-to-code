"""
Project: Learn to code
Version: 1.0
Author: Armen-Jean Andreasian
Year: 2023

"""

import streamlit as st

from streamlit_elements import sidebar, page_config, lerning_sources, legal_info, tools, learning_assistants, practice, music, communities

# styling
page_config.settings()

# resources
lerning_sources.sources()

# sidebar
sidebar.sidebar()

# practice
practice.train()

# learning assistants
learning_assistants.tools()

# communities

communities.com()

# tools
tools.tools()

# music
music.ncs()

# legal info
legal_info.legal()
