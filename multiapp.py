import streamlit as st

st.set_page_config(
    page_title="CareLink - Community",
    page_icon="🗨️",
)
class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })
    def run(self):
        selected_app = st.selectbox(
            'Disease Name',
            [app['title'] for app in self.apps]
        )
        for app in self.apps:
            if app['title'] == selected_app:
                app['function']()