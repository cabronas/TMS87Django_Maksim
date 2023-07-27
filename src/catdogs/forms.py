from django import forms


class PetsFilterForm(forms.Form):
    kinds = (('cat', 'CAT')
             , ('dog', "DOG"))
    pet = forms.ChoiceField(choices=kinds)

    format_kinds = (('png', 'png'), ('gif', 'gif'), ('jpg', 'jpg'), ('jpeg', 'jpeg'))
    format = forms.ChoiceField(choices=format_kinds)
