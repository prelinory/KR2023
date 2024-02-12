from django import forms
from .models import *
from django.core.validators import MinValueValidator


class EquationForm(forms.Form):
    n = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"min": "1","max": "50", "class": "form-control form-control-lg"}
        ),
        validators=[MinValueValidator(0)],
    )


class EquationFormTwo(forms.Form):
    def __init__(self, n, *args, **kwargs):
        super(EquationFormTwo, self).__init__(*args, **kwargs)
        for x in range(0, n):
            for j in range(0, n):
                field_name = f"Коэффициент x[{x+1}][{j+1}]"
                self.fields[field_name] = forms.IntegerField(
                    widget=forms.NumberInput(
                        attrs={"class": "form-control form-control-lg"}
                    )
                )

            self.fields[f"Свободный член y[{x+1}]"] = forms.IntegerField(
                widget=forms.NumberInput(
                    attrs={"class": "form-control form-control-lg"}
                )
            )

        for x in range(0, n):
            self.fields[f"Начальное приближение x[{x+1}]"] = forms.IntegerField(
                widget=forms.NumberInput(
                    attrs={"class": "form-control form-control-lg"}
                )
            )

        self.fields["Точность"] = forms.FloatField(
            widget=forms.NumberInput(attrs={"class": "form-control form-control-lg"})
        )
        self.fields["Максимальное число итераций"] = forms.IntegerField(
            widget=forms.NumberInput(attrs={"class": "form-control form-control-lg"})
        )
