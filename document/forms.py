from django import forms

from document.models import Document, Event, Report, SigDoc


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file', 'name']
        widgets = {
            'file': forms.ClearableFileInput(
                attrs={'class': 'form-control',
                       'style': 'border-radius: .25rem 0 0 .25rem; height: 100%;',
                       }),
        }


class SigDocForm(forms.ModelForm):
    class Meta:
        model = SigDoc
        fields = ['sign_doc']
        widgets = {
            'sign_doc': forms.ClearableFileInput(
                attrs={'class': 'form-control',
                       'style': 'border-radius: .25rem 0 0 .25rem; height: 100%;',
                       }),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'time', "short_text", 'text']

    # date = forms.DateField(label='Дата')
    # time = forms.TimeField(label='Время')
    # text = forms.CharField(max_length=30)
    widgets = {
        'short_text': forms.ClearableFileInput(
            attrs={'class': 'form-control',
                   'style': 'border-radius: .25rem 0 0 .25rem; height: 100%;',
                   }),
        'text': forms.ClearableFileInput(attrs={'class': 'form-control',
                                                'style': 'border-radius: .25rem 0 0 .25rem; height: 100%;',
                                                }),
        'date': forms.ClearableFileInput(attrs={'class': 'vDateField',
                                                'style': 'border-radius: .25rem 0 0 .25rem; height: 100%;'
                                                }),
        'time': forms.ClearableFileInput(attrs={'class': 'vTimeField',
                                                'style': 'border-radius: .25rem 0 0 .25rem; height: 100%;'
                                                }),
    }


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['file', 'name']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control',
                                                    'style': 'border-radius: .25rem 0 0 .25rem; height: 100%;',
                                                    'required': 'true'
                                                    })
        }
