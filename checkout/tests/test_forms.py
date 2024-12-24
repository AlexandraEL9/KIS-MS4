from django.test import SimpleTestCase
from checkout.forms import OrderForm


class TestOrderForm(SimpleTestCase):

    def test_form_with_valid_data(self):
        """
        Test the form with all valid input data.
        """
        form_data = {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone_number': '123456789',
            'street_address1': '123 Main St',
            'street_address2': 'Apt 4B',
            'town_or_city': 'Sampletown',
            'postcode': 'AB12 3CD',
            'country': 'GB',
            'county': 'Sample County',
        }
        form = OrderForm(data=form_data)
        self.assertTrue(
            form.is_valid(),
            "The form should be valid with correct input data."
        )

    def test_form_missing_required_fields(self):
        """
        Test the form when required fields are missing.
        """
        form_data = {
            'email': 'john@example.com',
            'town_or_city': 'Sampletown',
        }
        form = OrderForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            "The form should be invalid when required fields are missing."
        )
        self.assertIn(
            'full_name', form.errors,
            "The form should include 'full_name' in errors."
        )
        self.assertIn(
            'phone_number', form.errors,
            "The form should include 'phone_number' in errors."
        )

    def test_form_optional_fields_empty(self):
        """
        Test the form when optional fields are empty.
        """
        form_data = {
            'full_name': 'Jane Doe',
            'email': 'jane@example.com',
            'phone_number': '987654321',
            'street_address1': '456 Another St',
            'town_or_city': 'Another Town',
            'postcode': 'CD34 5EF',
            'country': 'GB',
        }
        form = OrderForm(data=form_data)
        self.assertTrue(
            form.is_valid(),
            "The form should be valid even if optional fields are empty."
        )

    def test_form_invalid_email(self):
        """
        Test the form with an invalid email.
        """
        form_data = {
            'full_name': 'John Doe',
            'email': 'not-an-email',  # Invalid email format
            'phone_number': '123456789',
            'street_address1': '123 Main St',
            'town_or_city': 'Sampletown',
            'postcode': 'AB12 3CD',
            'country': 'GB',
        }
        form = OrderForm(data=form_data)
        self.assertFalse(
            form.is_valid(),
            "The form should be invalid with an improperly formatted email."
        )
        self.assertIn(
            'email', form.errors,
            "The form should include 'email' in errors."
        )
