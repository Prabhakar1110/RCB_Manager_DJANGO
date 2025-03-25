from django import forms
from .models import Player, Food

class PlayerForm(forms.ModelForm):
    fav_food = forms.ModelMultipleChoiceField(
        queryset=Food.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Player
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding Bootstrap classes
        for field_name, field in self.fields.items():
            if field_name not in ['fav_food', 'is_captain']:
                field.widget.attrs.update({'class': 'form-control'})
        
        self.fields['name'].widget.attrs.update(
            {'placeholder': 'Enter player Name'}
        )
        self.fields['age'].widget.attrs.update(
            {'placeholder': 'Enter player Age'}
        )

        self.fields["role"].choices = list(self.fields["role"].choices)
        self.fields["role"].choices.pop(0)

        self.fields["country"].choices = list(self.fields["country"].choices)
        self.fields["country"].choices.pop(0)

        # Special handling for checkboxes (BooleanField and ManyToManyField)
        self.fields['is_captain'].widget.attrs.update({'class': 'form-check-input'})
        # self.fields['fav_food'].widget.attrs.update({'class': 'form-check-input'})