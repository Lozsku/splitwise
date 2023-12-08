# main.py - Python script for the main application

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import psycopg2
from urllib.parse import urlparse

class MyApp(App):
    def build(self):
        # UI layout
        layout = BoxLayout(orientation='vertical')

        # UI components
        text_input = TextInput(text='Enter text here')
        submit_button = Button(text='Submit', on_press=self.on_submit)

        # Add components to layout
        layout.add_widget(text_input)
        layout.add_widget(submit_button)

        return layout

    def on_submit(self, instance):
        user_input = instance.parent.children[0].text  # Get text from TextInput

        # Parse ElephantSQL URL
        url = "postgres://pgglbqsz:4dVgYAhf7PLt727STsJ4kml7lwXIRIIP@ella.db.elephantsql.com/pgglbqsz"
        parsed_url = urlparse(url)
        
        # Database operations
        connection = psycopg2.connect(
            database=parsed_url.path[1:],
            user=parsed_url.username,
            password="4dVgYAhf7PLt727STsJ4kml7lwXIRIIP",
            host=parsed_url.hostname,
            port=parsed_url.port
        )
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS user_data (input_text TEXT)')
        cursor.execute('INSERT INTO user_data VALUES (%s)', (user_input,))
        connection.commit()
        connection.close()

if __name__ == '__main__':
    MyApp().run()

