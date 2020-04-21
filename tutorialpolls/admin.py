from django.contrib import admin
from  .models import Question, Choice


admin.site.site_header = "Ave Imperator!"
admin.site.site_title = "Forum Area"
admin.site.index_title = "Salve, Amicus!"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
                (None, {'fields': ['question_text']}), 
                ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), 
                ]
    inlines = [ChoiceInLine]

# Register your models here.
# admin.site.register(Question) 
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)