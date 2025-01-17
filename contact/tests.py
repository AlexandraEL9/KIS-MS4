from django.test import TestCase
from .models import ContactMessage

# Create your tests here.
class ContactModelTests(TestCase):
    def test_contact_message_creation(self):
        message = ContactMessage.objects.create(
            name="Test User",
            email="test@example.com",
            message="This is a test."
        )
        self.assertEqual(str(message), "Message from Test User - test@example.com")
