from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopingInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_tag = 0
        for form in self.forms:
            if form.cleaned_data.get('main'):
                count_tag += 1
            else:
                continue
        if count_tag == 0:
            raise ValidationError('Выберите основной раздел')
        elif count_tag > 1:
            raise ValidationError('Основной раздел уже выбран')

        return super().clean()


class ScopingInline(admin.TabularInline):
    model = Scope
    formset = ScopingInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopingInline]


@admin.register(Tag)
class TopicAdmin(admin.ModelAdmin):
    pass
