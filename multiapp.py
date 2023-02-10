import streamlit as st

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
            'Diease Name',
            [app['title'] for app in self.apps]
        )
        for app in self.apps:
            if app['title'] == selected_app:
                app['function']()

    # def run(self):
    #     selected_app = st.sidebar.selectbox(
    #         'Go To',
    #         [app['title'] for app in self.apps]
    #     )
    #     for app in self.apps:
    #         if app['title'] == selected_app:
    #             app['function']()