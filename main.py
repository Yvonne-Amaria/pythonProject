import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text="First Name: "))
        self.firstName = TextInput(multiline=False)
        self.add_widget(self.firstName)

        self.add_widget(Label(text="Last Name: "))
        self.lastName = TextInput(multiline=False)
        self.add_widget(self.lastName)

        self.add_widget(Label(text="Email address: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)

        self.submit = Button(text="Next", font_size=30)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
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
