from django.contrib import admin
from django.forms.models import BaseInlineFormSet

from .models import *


class OptionInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_of_right_questions = 0
        for form in self.forms:
            try:
                cd = form.cleaned_data
                if cd:
                    if cd['is_right_option']:
                        count_of_right_questions += 1
            except AttributeError:
                pass
        if not count_of_right_questions:
            raise ValidationError('Вы должны выбрать хотя бы один правильный ответ!')


class TestsUsersAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'test', 'result']


class OptionInline(admin.StackedInline):
    model = Option
    formset = OptionInlineFormset


class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


admin.site.register(Topic)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Test)
admin.site.register(TestsUsers, TestsUsersAdmin)
