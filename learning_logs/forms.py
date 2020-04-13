from django import forms

from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:
        # 告诉Django根据哪个模型创建表单，以及在表单中包含哪些字段
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # widget 是一个HTML表单元素，如单行文本框、多行文本区域或下拉列表
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
