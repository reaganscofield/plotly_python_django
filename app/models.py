from django.db import models
from django.conf import settings
from django.core.validators import validate_comma_separated_integer_list

# account model 
class Account(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete="models.CASCADE")
    account_number = models.IntegerField()
    trasaction_day_record = models.CharField(
        validators=[validate_comma_separated_integer_list],
        max_length=200, blank=True, null=True,default=''
    )
    weekly_day_record = models.CharField(max_length=100, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(null=False, default=True)

    def __str__(self):
        return f"{self.account_number}"   