from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label_name_list = ('Joe', 'Bob', 'Peter', 'Paul')

    def build(self):
        self.title = "Label Maker"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.label_name_list:
            print(name)
            temp_label = Label(text=name, id=name)
            print(temp_label)
            self.root.ids.output_label.add_widget(temp_label)


DynamicLabelApp().run()
