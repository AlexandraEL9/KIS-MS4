from django.test import SimpleTestCase
from profiles.forms import UserProfileForm

class TestUserProfileForm(SimpleTestCase):
    """
    Tests for the UserProfileForm using SimpleTestCase.
    """
    def test_form_fields(self):
        """
        Test that the form contains the correct fields.
        """
        form = UserProfileForm()
        expected_fields = [
            'default_phone_number',
            'default_street_address1',
            'default_street_address2',
            'default_town_or_city',
            'default_county',
            'default_postcode',
            'default_country',
        ]
        # Check if all expected fields are in the form
        self.assertEqual(list(form.fields.keys()), expected_fields)

    def test_labels_removed(self):
        """
        Test that the labels are removed for all fields.
        """
        form = UserProfileForm()
        for field_name, field in form.fields.items():
            self.assertFalse(
                field.label,
                f"Label for field '{field_name}' should be removed."
            )