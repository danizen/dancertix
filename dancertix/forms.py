from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


color_names = [
    'AliceBlue',
    'Aqua',
    'Azure',
    'Beige',
    'Bisque',
    'Black',
    'BlanchedAlmond',
    'Blue',
    'BurlyWood',
    'CadetBlue',
    'Chocolate',
    'Coral',
    'Cyan',
    'DarkBlue',
    'DarkGoldenRod',
    'DarkGray',
    'DarkGreen',
    'DarkMagenta',
    'DarkOrange',
    'DarkOrchid',
    'DarkRed',
    'DarkSlateBlue',
    'DarkTurquoise',
    'DeepPink',
    'DimGray',
    'DodgerBlue',
    'FireBrick',
    'ForestGreen',
    'HoneyDew',
    'HotPink',
    'Khaki',
    'LightBlue',
    'LightCoral',
    'LightCyan',
    'LightGreen',
    'LightSalmon',
    'LightSlateGray',
    'Linen',
    'MediumSlateBlue',
    'MediumVioletRed',
    'MintCream',
    'MistyRose',
    'NavajoWhite',
    'Navy',
    'OldLace',
    'Olive',
    'OliveDrab',
    'Orange',
    'Orchid',
    'PaleGoldenRod',
    'PapayaWhip',
    'PeachPuff',
    'Pink',
    'PowderBlue',
    'Purple',
    'Salmon',
    'SandyBrown',
    'SlateBlue',
    'Snow',
    'SpringGreen',
    'Teal',
    'Wheat',
    'White',
    'Yellow'
]

color_choices = [('', '')] + [(c.lower(), c) for c in color_names]


class ColorForm(forms.Form):
    color = forms.ChoiceField(choices=color_choices, label='Favorite Color')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_layout(Layout(
            'color',
            Submit('submit', 'Submit', css_class='btn btn-primary')
        ))
