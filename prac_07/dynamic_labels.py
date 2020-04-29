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
            temp_label = Label(text=name, id=name)
            print(temp_label)
            #temp_label.bind(on_release=self.press_item)
            #self.root.ids.output_label.add_widget(Label(name))
            #self.root.ids.output_label.text = name
            self.root.ids.output_label.add_widget(temp_label)

    #def press_item(self, instance):
     #   name = instance.id  # or name = instance.text
        # update status text
      #  self.status_text = "{}".format(self.name)



DynamicLabelApp().run()