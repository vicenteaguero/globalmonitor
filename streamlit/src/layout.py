# streamlit/src/layout.py

import streamlit as st

from PIL import Image

from src.params import PATHS, GITHUB_URL, ABOUT_URL

def setup_layout(page_title: str, page_icon: str):
    favicon = Image.open(PATHS['favicon'])
    st.set_page_config(
        layout='wide',
        page_title=page_title,
        initial_sidebar_state='expanded',
        page_icon=favicon,
        menu_items={
            'Get help': GITHUB_URL,
            'Report a bug': GITHUB_URL+'/issues',
            'About': ABOUT_URL
        }
    )
    st.logo(image=PATHS['logo-dark'], link=GITHUB_URL, size='large')

def setup_pages():
    pages = {
        'Home': [
            st.Page(page=PATHS['pages']['home'], title='Home', icon='🏠'),
            st.Page(page=PATHS['pages']['docs'], title='Docs', icon='📚'),
        ],
        'Global Monitor': [
            st.Page(page=PATHS['pages']['paginator'], title='Paginator', icon='📰'),
            st.Page(page=PATHS['pages']['formatter'], title='Format Pages', icon='🗞️'),
        ],
    }
    nav = st.navigation(pages)
    nav.run()

def setup_custom_css():
    styles = ['base']
    for style in styles:
        with open(PATHS[f'{style}_css']) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
