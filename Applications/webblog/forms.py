from django import forms

class QuestionsForm(forms.Form):
   
    ch = [('ch1', 'ตอบ ประเทศไทย'), ('ch2', 'ตอบ ประเทศสยาม')]
    question1 = forms.ChoiceField(
        label='ข้อที่ 1 จงตอบคำถามต่อไปนี้',
        choices=ch,
        widget=forms.RadioSelect,
        required=True,
        disabled=False,              
    )
    
    memo1 = forms.CharField(
        label='เพิ่มเติม',
        required=False,
        max_length=15,
        widget=forms.Textarea(attrs={
            'placeholder': 'บันทึกช่วยจำ',
            'cols': '30',
            'rows': '3',
        })  
    )

    ch = [('ch1', 'ตอบ ประเทศไทย'), ('ch2', 'ตอบ ประเทศสยาม')]
    question2 = forms.ChoiceField(
        label='ข้อที่ 2 จงตอบคำถามต่อไปนี้',
        choices=ch,
        widget=forms.RadioSelect,
        required=True,
        disabled=False,                 
    )

    memo2 = forms.CharField(
        label='เพิ่มเติม',
        required=False,
        max_length=15,
        widget=forms.Textarea(attrs={
            'placeholder': 'บันทึกช่วยจำ',
            'cols': '30',
            'rows': '3',
        })  
    )