from django.test import TestCase
from django.urls import reverse
from .models import ContactMessage
from .forms import ContactForm


# Test the model
class ContactModelTests(TestCase):
    """ Test the ContactMessage model """

    def test_contact_message_creation(self):
        """ Ensure that a ContactMessage object is created correctly """
        message = ContactMessage.objects.create(
            name="Test User",
            email="test@example.com",
            message="This is a test."
        )
        self.assertEqual(
            str(message),
            "Message from Test User - test@example.com"
        )


# Test the form
# Credit: adapted from learning found at
# https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/?utm_source=chatgpt.com
class ContactFormTests(TestCase):
    """ Test the Contact Form """

    def test_valid_form(self):
        """ Test a valid form submission """
        form = ContactForm(data={
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message.'
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """ Test an invalid form submission with incorrect data """
        form = ContactForm(data={
            'name': '',
            'email': 'invalid-email',
            'message': ''
        })
        self.assertFalse(form.is_valid())


# Test Submission
class ContactSubmissionTests(TestCase):
    """ Test form submission behavior """

    def test_valid_submission(self):
        """ Test a valid form submission and database creation """
        response = self.client.post(reverse('contact'), {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'This is a test message.'
        })

        # Check redirection back to the contact page
        self.assertRedirects(response, reverse('contact'))

        # Verify one object has been created in the database
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_invalid_submission(self):
        """ Test an invalid form submission with incorrect data """
        response = self.client.post(reverse('contact'), {
            'name': '',
            'email': 'invalid-email',
            'message': ''
        })

        # Check status code (page reloads instead of redirecting)
        self.assertEqual(response.status_code, 200)

        # Verify expected error message appears on the page
        self.assertContains(response, "Please correct the errors below.")

        # Ensure that no message objects were created in the database
        self.assertEqual(ContactMessage.objects.count(), 0)
