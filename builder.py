import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('ourrandom.kv')

# Builder.load_string(""" copy and paste the kivy design file on here"" - not advisible""")

class MyGrid(Widget):

    firstname = ObjectProperty(None)
    lastname = ObjectProperty(None)
    email = ObjectProperty(None)


def press(self):
    name = self.firstName.text
    last = self.lastName.text
    email = self.email.text

    print("First Name:", name, "Last Name:", last, "Email:", email)
    self.firstName.text = ""
    self.lastName.text = ""
    self.email.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
