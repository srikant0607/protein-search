from django.db import models

# Create your models here.


class Searchstr(models.Model):
    # input string to search
    search_text = models.CharField(max_length=1000)
    # date and time of submission
    sub_date = models.DateTimeField('time submitted')
    # result of search
    match = models.CharField(max_length=1000)
    # task ID
    task_id = models.CharField(max_length=50)

    def __str__(self):
        return self.search_text

