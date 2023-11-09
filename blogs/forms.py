from django import forms

from blogs.models import Blog


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('header', 'content', 'image',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']

        forbidden_words = ['казино', 'бесплатно', 'вирусы', "кибербуллинг", "приватный", "незаконное", "нарушение",
                           "авторских прав", "финансовые схемы", "обман", "криптовалюта", "биржа", "трейдинг", "дешево",
                           "казино"]

        for forbidden_word in forbidden_words:
            if forbidden_word in cleaned_data.lower():
                raise forms.ValidationError(f'В вашем названии курса есть запретное слово "{forbidden_word.title()}".')

        return cleaned_data


