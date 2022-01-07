"""Questions tests."""

# Django
from django.test import TestCase

from server.questions.models import Question
from server.users.models import User

class QuestionsManagerTestCase(TestCase):
    """Questions manager test case."""

    def setUp(self):
        """Test case setup."""
        self.user = User.objects.create(
            first_name='Sandra',
            last_name='Jimenez',
            email='sandra@gmail.com',
            username='sandra',
            password='sandra123'
        )
    
    def test_code_generation(self):
        """Random codes should be generated automatically."""
        question = Question.objects.create(
            asked_by=self.user
        )
        # import pdb; pdb.set_trace()
        self.assertIsNotNone(question.title)
        self.assertIsNotNone(question.detail)