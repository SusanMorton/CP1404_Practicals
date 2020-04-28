from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.label import Label

class DynamicLabelApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label_name_list = ('Joe', 'Bob', 'Peter')

    def build(self):
        self.title = "Label Maker"
        self.root = Builder.load_file('dynamic_labels.kv')
        #self.label_name_list = ('Joe', 'Bob', 'Peter')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.label_name_list:
            print(name)
            #self.root.ids.output_label.add_widget(Label(name))
            self.root.ids.output_label.text = name

#i dont know how to do this. a sample solution would have been much more helpful than referring to dynamic widgets and the very minimal instructions. :( 



DynamicLabelApp().run()