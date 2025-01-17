from django.test import TestCase
from .models import ContactMessage
from .forms import ContactForm
from django.urls import reverse

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

# Test Submission
class ContactSubmissionTests(TestCase):
    # Test a valid form submission
    def test_valid_submission(self):
        # simulate form submission
        response=self.client.post(reverse('contact'), {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message.'
        })
        # check redirection back to contact page
        self.assertRedirects(response, reverse('contact'))
        # verify one object has been created in the database
        self.assertEqual(ContactMessage.objects.count(), 1)

    # Test an invalid form submission
    def test_invalid_submission(self):
        # simulate form submission with invalid data
        response=self.client.post(reverse('contact'), {
            'name': '',
            'email': 'invalid-email',
            'message': ''
        })

        # check status code
        #page reloads indicating errors instead of redirecting
        self.assertEqual(response.status_code,200)
        # verify expected error message
        self.assertContains(response, "Please correct the errors below.")
        # check data not saved- verify no message objects were created in the database
        self.assertEqual(ContactMessage.objects.count(), 0)
