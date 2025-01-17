from django.test import TestCase
from .models import ContactMessage
from .forms import ContactForm

# Create your tests here.
# Test the model
class ContactModelTests(TestCase):
    def test_contact_message_creation(self):
        message = ContactMessage.objects.create(
            name="Test User",
            email="test@example.com",
            message="This is a test."
        )
        self.assertEqual(str(message), "Message from Test User - test@example.com")

# Test the form
# Credit: adapted from learning found at 
# https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/?utm_source=chatgpt.com
class ContactFormTests(TestCase):
    # Test a valid form
    def test_valid_form(self):
        form = ContactForm(data={
            #correctly inputted data
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message.'
        })
        self.assertTrue(form.is_valid())

    # Test an invalid form
    def test_invalid_form(self):
        form = ContactForm(data={
            #correctly inputted data
            'name': '',
            'email': 'invalid-email',
            'message': ''
        })
        self.assertFalse(form.is_valid())
