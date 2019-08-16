from django.db import models

class Addr(models.Model):
    GENDER_MAN = "男性"
    GENDER_WOMAN = "女性"
    GENDER_OTHER = "その他"
    GENDER_SET = (
            (0, GENDER_MAN),
            (1, GENDER_WOMAN),
            (2, GENDER_OTHER),
            )

    name = models.CharField(max_length=128)
    birthday = models.DateField()
    gender = models.IntegerField(choices=GENDER_SET)
    address = models.CharField(max_length=128)
    jobs = models.CharField(max_length=1024)
    note = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
