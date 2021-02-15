from django import forms



class factorial_form(forms.Form):
    n=forms.IntegerField(label="n",label_suffix="=")

    def clean_n(self):
        n=self.cleaned_data.get('n')
        if  n<0:
            raise forms.ValidationError('please enter a positive integer number')

        return n