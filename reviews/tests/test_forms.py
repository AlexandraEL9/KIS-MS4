from django.test import SimpleTestCase
from reviews.forms import ReviewForm

class TestReviewForm(SimpleTestCase):

    def test_form_with_valid_data(self):
        """Test the form with valid data."""
        form = ReviewForm(data={
            'title': 'Great Product',
            'content': 'This is a fantastic product!',
            'rating': 4,
        })
        self.assertTrue(form.is_valid(), "The form should be valid with correct data")

    def test_form_with_missing_title(self):
        """Test the form when the title is missing."""
        form = ReviewForm(data={
            'title': '',
            'content': 'This is a fantastic product!',
            'rating': 4,
        })
        self.assertFalse(form.is_valid(), "The form should not be valid if the title is missing")
        self.assertIn('title', form.errors, "The form should contain errors for the missing title")

    def test_form_with_missing_content(self):
        """Test the form when the content is missing."""
        form = ReviewForm(data={
            'title': 'Great Product',
            'content': '',
            'rating': 4,
        })
        self.assertFalse(form.is_valid(), "The form should not be valid if the content is missing")
        self.assertIn('content', form.errors, "The form should contain errors for the missing content")

    def test_form_with_invalid_rating(self):
        """Test the form when the rating is invalid."""
        form = ReviewForm(data={
            'title': 'Great Product',
            'content': 'This is a fantastic product!',
            'rating': 6,  # Assuming rating should be between 1 and 5
        })
        self.assertFalse(form.is_valid(), "The form should not be valid with an invalid rating")
        self.assertIn('rating', form.errors, "The form should contain errors for an invalid rating")
