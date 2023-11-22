from django.db import models


class AudioRecord(models.Model):
    phonenumber = models.CharField(max_length=15)
    audio  = models.URLField()

    def __str__(self):
        return self.phonenumber

    class Meta:
        db_table='mytable'




