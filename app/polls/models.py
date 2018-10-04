import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """
        자신의 게시일자 >= 지금 - 1

        :return: 최근에 게시되었는지 여부
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('게시일자')


class Choice(models.Model):

    def __str__(self):
        return self.choice_text

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
    )
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
