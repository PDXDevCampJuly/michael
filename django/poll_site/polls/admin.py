from django.contrib import admin
from .models import Question
from .models import Choice

# tells Django admin to put the models
# Register your models here.

# makes custom changes
classQuestionAdmin(admin.ModelAdmin):
  # rearranges fields in admin
  fields = ['pub_date', 'question_text']
  # displays the question instead of 'question' object
  list_display = ('question_text', 'pub_date', 'was_published_recently')
  list_filter = ['pub_date']

# 'question' object
admin.site.register(Question, QuestionAdmin)

# 'choice' object
admin.site.register(Choice)
