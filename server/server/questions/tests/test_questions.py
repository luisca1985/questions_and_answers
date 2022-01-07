"""Questions tests."""

# Django
from django.test import TestCase

# Django REST Framework
from rest_framework.test import APITestCase
from rest_framework import status

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
    
    def test_title_generation(self):
        """Random codes should be generated automatically."""
        question = Question.objects.create(
            asked_by=self.user
        )
        # import pdb; pdb.set_trace()
        self.assertIsNotNone(question.title)
        self.assertIsNotNone(question.detail)

class QuestionsAPITestCase(APITestCase):
    """Question API Test case."""

    def setUp(self):
        """Test case setup."""
        self.user = User.objects.create(
            first_name='Sandra',
            last_name='Jimenez',
            email='sandra@gmail.com',
            username='sandra',
            password='sandra123'
        )
        self.question = Question.objects.create(
            asked_by=self.user,
            title='question title',
            detail='question detail'
        )

    def test_response_success(self):
        """Verify request success."""
        url = f'/api/questions/{ self.question.id }'
        print(url)
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)