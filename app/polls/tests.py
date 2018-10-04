import datetime

from django.test import TestCase

from django.test import TestCase
from django.utils import timezone

from polls.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        # 미래의 datetime 객체를 time 변수에 할당
        time = timezone.now() + datetime.timedelta(days=30)
        # 새 Question 인스턴스를 생성, pub_date 가 미래시간을 주어줌
        futuer_question = Question(pub_date=time)
        # 주어진 두개의 객체가 같아야 할 것(is) 으로 기대함
        # 같지 않으면 실패
        self.assertIs(
            futuer_question.was_published_recently(),
            False,
        )