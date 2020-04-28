from kivy.app import App
#from kivy.app import Widget
from kivy.lang import Builder

MILES_TO_KM_RATIO = 1.60934

class MilesToKmConverter(App):
    def build(self):
        self.title: "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, mile, increment):
        value = mile + increment
        self.root.ids.mile_input.text = str(value)

    def handle_convert(self):
        validated_value = self.validate_input_text()
        #km_value = mile_value * MILES_TO_KM_RATIO
        km_value = validated_value * MILES_TO_KM_RATIO
        self.root.ids.km_value_output.text = str(km_value)

    def validate_input_text(self):
        try:
            validated_value = float(self.root.ids.mile_input.text)
            return validated_value
        except ValueError:
            return 0.00

MilesToKmConverter().run()