from django.db import models
from django.core.validators import MinLengthValidator

class Today(models.Model):
    tasks = models.TextField( 
        validators=[
            MinLengthValidator(1,'Вы пропустили ввод задачи!')
            ]   
        )
    edit_mode = models.BooleanField(default=False)
