# **Shop K-Beauty Testing Results**

![amiresponsive mock-ups of Keep it Sweet!](./docs/.png)

<br/>

**[Link to the Deployed Site](#)**

---
## TABLE OF CONTENTS

* [Automated Testing and Validation](#automated-testing-and-validation)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [JavaScript Validation](#javascript-validation)
    * [Python Validation](#python-validation)
    * [Lighthouse Report](#lighthouse-report)
        * [Desktop](#desktop)
        * [Mobile](#mobile)
    * [WAVE Web Accessibility Evaluation Tool](#wave-web-accessibility-evaluation-tool)
    * [Django Automated Testing](#django-automated-testing)
        * [Coverage](#coverage)
* [Manual Testing](#manual-testing)
    * [Testing User Stories](#testing-user-stories)
    * [Full Testing](#full-testing)
* [Bugs, Errors & Solutions](#bugs-found-during-testing-and-development-phase)
    * [Solved Bugs](#solved-bugs)
    * [Known Bugs](#known-bugs)
---

## Automated Testing and Validation
### Automated Testing

#### Overview  
I implemented automated testing on **Python forms** using Django's `SimpleTestCase`.

#### Forms Testing  
- Focused on validating form functionality and ensuring form inputs meet expected validation rules.  
- **Example:** Testing required fields, invalid inputs, and clean method logic for Django forms.

---

### Testing Results  

| **Test Name**               | **Test Type**                | **Description**                                                               | **Result** | **Screenshot**                                      |
|-----------------------------|------------------------------|-------------------------------------------------------------------------------|------------|----------------------------------------------------|
| **ReviewForm Validation**   | Django - SimpleTestCase      | Uses 4 tests to ensure the functionality and validation of the `ReviewForm` in the reviews app: Valid Data Test, Missing Title Test, Missing Content Test, Invalid Rating Test.       | ✅ Pass    | ![Screenshot](/docs/testing/automated-testing/review-forms-testing.png)   |
| **CheckoutForm Validation** | Django - SimpleTestCase      | Uses 4 tests to ensure the functionality and validation of the `orderForm` in the checkout app: Valid Data Test, Missing Required Fields Test, Optional Fields Test, Invalid Email Test. | ✅ Pass    | ![Screenshot](/docs/testing/automated-testing/checkout-form-testing.png) |
| **UserProfilesForm Validation** | Django - SimpleTestCase      | Uses 2 tests to ensure the functionality and validation of the `UserProfileForm` in the checkout app: Correct Fields Test, Labels Removed Test | ✅ Pass    | ![Screenshot](/docs/testing/automated-testing/profile-form-testing.png) |


### HTML Validation
I used [W3C Markup Validation Service](https://validator.w3.org/) to validate all the HTML files by direct input:
| Page | Result | Validation Details & Screenshots |
| ---- | :-: | -------------------------- |
| 'templates/home/index.html' | # error and # warning | [Homepage](./docs/) |

### CSS Validation
I used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate all CSS files by direct input.
| File | Result | Test Details & Screenshots |
| ---- | :-: | -------------------------- |
| /.css | Pass | [checkout.css](./docs/.png) |

### JavaScript Validation
I used [JSHint](https://jshint.com/) to validate all JavaScript and JQuery files
| Function | Result | Validation Details & Screenshots |
| :-- | :-: | -------------------------- |
| **bag.html** |  |  |
| bag/templates/bag/bag.html (Update quantity on click) | All clear, no errors found | [bag.update-quantity](./docs/testing/jshint/bag-update-quantity.png) |
| bag/templates/bag/bag.html (Remove item and reload on click) | All clear, no errors found | [bag.remove-reload](./docs/testing/jshint/bag-remove-reload.png) |
| Complete section | All clear, no errors found | [bag.full-section](./docs/testing/jshint/bag-full-section.png) |
| **checkout app** |  |  |
| checkout/static/checkout/js/stript_elements.js (Stripe elements) | Added Stripe as a global variable- no errors- all clear. | [checkout.static.checkout.js.stripe_elements.js](./docs/testing/jshint/bag-update-quantity.png) |
| **products app** |  |  |
| products/templates/products/products.html (sort selector) | no errors- all clear. | [products.html- sort-selector](./docs/testing/jshint/products-sort-selector.png) |
| products/templates/products/products.html (scroll button) | no errors- all clear. | [products.html- scroll button](./docs/testing/jshint/products-scroll.png) |
| products/templates/products/edit_product.html (edit product- image) | no errors- all clear. | [edit products](./docs/testing/jshint/products-edit-image.png) |
| products/templates/products/add_product.html(add product- image) | no errors- all clear. | [add products](./docs/testing/jshint/products-add-image.png) |
| products/templates/products/includes/quantity_input_script.html| no errors- all clear. | [products.includes/quantity_input_script](./docs/testing/jshint/products-quantity-input-script.png) |
| **profiles app** |  |  |
| profiles/static/profiles/js/countryfield.js| no errors- all clear. | [profiles-countryfield.js](./docs/testing/jshint/profiles-countryfield.png) |
| **reviews app** |  |  |
| reviews/templates/reviews/product_reviews.html| no errors- all clear. | [reviews- modal](./docs/testing/jshint/reviews-product-reviews-modal.png) |
| **templates** |  |  |
| templates/base.html- 'show toasts'| no errors- all clear. | [templates.base.toasts](./docs/testing/jshint/templates-base-toasts.png) |



### Python Validation
I used [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) to lint my Python code.
| File | Result | Validation Details & Screenshots |
| :-- | :-: | -------------------------- |
| manage.py | All clear, no errors found | [manage.py](./docs/testing/python-linter/managepy.png)|
| custom_storages.py | All clear, no errors found | [custom_storages.py](./docs/testing/python-linter/custom_storages.png)|
| **Keep_it_sweet** |  |  |
| keep_it_sweet/wsgi.py | All clear, no errors found | [keep_it_sweet.wsgi.py validation](./docs/testing/python-linter/kis-wsgi.png) |
| keep_it_sweet/urls.py | All clear, no errors found | [keep_it_sweet.urls.py validation](./docs/testing/python-linter/kis-urls.png) |
| keep_it_sweet/settings.py | All clear, no errors found | [keep_it_sweet.settings.py validation](./docs/testing/python-linter/kis-settings.png) |
| **Checkout app** |  |  |
| checkout/webhooks.py | All clear, no errors found | [checkout/webhooks.py validation](./docs/testing/python-linter/checkout-webhooks.png) |
| checkout/webhook_handler.py | All clear, no errors found | [checkout/webhook_handler.py validation](./docs/testing/python-linter/checkout-webhook-handler.png) |
| checkout-views.py | All clear, no errors found | [checkout/views.py validation](./docs/testing/python-linter/checkout/views.png) |
 checkout/urls.py | All clear, no errors found | [checkout/urls.py validation](./docs/testing/python-linter/checkout-urls.png) |
| checkout/signals.py | All clear, no errors found | [checkout/signals.py validation](./docs/testing/python-linter/checkout-signals.png) |
| checkout/models.py | All clear, no errors found | [checkout/models.py validation](./docs/testing/python-linter/checkout-models.png) |
| checkout/forms.py | All clear, no errors found | [checkout/forms.py validation](./docs/testing/python-linter/checkout-forms.png) |
| checkout/apps.py | All clear, no errors found | [checkout/apps.py validation](./docs/testing/python-linter/checkout-apps.png) |
| checkout/admin.py | All clear, no errors found | [checkout/admin.py validation](./docs/testing/python-linter/checkout-admin.png) |
| checkout/tests/test_forms.py | All clear, no errors found | [checkout/tests/test_forms.py validation](./docs/testing/python-linter/checkout-admin.png) |
| **Favourites app** |  |  |
| favourites/view.py | All clear, no errors found | [favourites.views.py validation](./docs/testing/python-linter/favourites-views.png) |
| favourites/urls.py | All clear, no errors found | [favourites.urls.py validation](./docs/testing/python-linter/favourites-urls.png) |
| favourites/models.py | All clear, no errors found | [favourites.models.py validation](./docs/testing/python-linter/favourites-models.png) |
| favourites/apps.py | All clear, no errors found | [favourites.apps.py validation](./docs/testing/python-linter/favourites-apps.png) |
| **Home app** |  |  |
| home/view.py | All clear, no errors found | [home.views.py validation](./docs/testing/python-linter/home-views.png) |
| home/urls.py | All clear, no errors found | [home.urls.py validation](./docs/testing/python-linter/home-urls.png) |
| home/apps.py | All clear, no errors found | [home.apps.py validation](./docs/testing/python-linter/home-apps.png) |
| **Products app** |  |  |
| products/widgets.py | All clear, no errors found | [products.widgets.py validation](./docs/testing/python-linter/products-widgets.png) |
| products/views.py | All clear, no errors found | [products.views.py validation](./docs/testing/python-linter/products-views.png) |
| products/urls.py | All clear, no errors found | [products.urls.py validation](./docs/testing/python-linter/products-urls.png) |
| products/models.py | All clear, no errors found | [products.models.py validation](./docs/testing/python-linter/products-models.png) |
| products/models.py | All clear, no errors found | [products.models.py validation](./docs/testing/python-linter/products-models.png) |
| products/forms.py | All clear, no errors found | [products.forms.py validation](./docs/testing/python-linter/products-forms.png) |
| products/apps.py | All clear, no errors found | [products.apps.py validation](./docs/testing/python-linter/products-apps.png) |
| products/admin.py | All clear, no errors found | [products.admin.py validation](./docs/testing/python-linter/products-admin.png) |
| **Profiles app** |  |  |
| profiles/views.py | All clear, no errors found | [profiles.views.py validation](./docs/testing/python-linter/profiles-views.png) |
| profiles/urls.py | All clear, no errors found | [profiles.urls.py validation](./docs/testing/python-linter/profiles-urls.png) |
| profiles/models.py | All clear, no errors found | [profiles.models.py validation](./docs/testing/python-linter/profiles-models.png) |
| profiles/forms.py | All clear, no errors found | [profiles.forms.py validation](./docs/testing/python-linter/profiles-forms.png) |
| profiles/tests/test_forms.py | All clear, no errors found | [profiles.tests.test_forms.py validation](./docs/testing/python-linter/profiles-tests-testforms.png) |
| **Reviews app** |  |  |
| reviews/views.py | All clear, no errors found | [reviews.views.py validation](./docs/testing/python-linter/reviews-views.png) |
| reviews/urls.py | All clear, no errors found | [reviews.urls.py validation](./docs/testing/python-linter/reviews-urls.png) |
| reviews/models.py | All clear, no errors found | [reviews.models.py validation](./docs/testing/python-linter/reviews-models.png) |
| reviews/forms.py | All clear, no errors found | [reviews.forms.py validation](./docs/testing/python-linter/reviews-forms.png) |
| reviews/apps.py | All clear, no errors found | [reviews.apps.py validation](./docs/testing/python-linter/reviews-apps.png) |
| reviews/admin.py | All clear, no errors found | [reviews.admin.py validation](./docs/testing/python-linter/reviews-admin.png) |
| reviews/tests/test_forms.py | All clear, no errors found | [reviews.tests.test_forms.py validation](./docs/testing/python-linter/reviews-tests-testforms.png) |
| **Subscribe app** |  |  |
| subscribe/views.py | All clear, no errors found | [subscribe.views.py validation](./docs/testing/python-linter/subscribe-views.png) |
| subscribe/urls.py | All clear, no errors found | [subscribe.urls.py validation](./docs/testing/python-linter/subscribe-urls.png) |
| subscribe/models.py | All clear, no errors found | [subscribe.models.py validation](./docs/testing/python-linter/subscribe-models.png) |
| subscribe/forms.py | All clear, no errors found | [subscribe.forms.py validation](./docs/testing/python-linter/subscribe-forms.png) |
| subscribe/apps.py | All clear, no errors found | [subscribe.apps.py validation](./docs/testing/python-linter/subscribe-apps.png) |
| subscribe/admin.py | All clear, no errors found | [subscribe.admin.py validation](./docs/testing/python-linter/subscribe-admin.png) |



### Lighthouse Report
[Chrome DevTools' Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to test the performance, accessibility, best practices and SEO of the site

# Notes
During the first round of testing I saw some disappointing scores for 'Performance' and 'Best Practices'. <br> <br  >
With regards to 'Performance', A further step I hope to make in the future would be to upgrade images to 'next gen' formats like AVIF or Webp. I believe this would make a big step in bettering the performance. <br> <br  >
With regarde to the 'Best Practices' scoring, issues center on the use of cookies by 'Stripe'. Stripe is integral to the working of this project. Example of evidence of this:['bag.html- dev tools- lighthouse screenshot'](/docs/testing/lighthouse-testing/bag-lighthouse-screenshot.png) I have fouds a fix for this issue- details of which can be found in the 'Bug Fixes' section, which put the Stripe script within a conditional block to ensure it only runs on the 'checkout' pages it is needed on. This has inproved scores accross the site.


#### Desktop
| Page | Performance (%) | Accessibility (%) | Best Practices (%) | SEO (%) | If score is below 90% |
| :-- | :-: | :-: | :-: | :-: | :-- |
| [' Current index.html'](/docs/testing/lighthouse-testing/homepage-desktop2.png) | 96 | 91 | 100 | 90 | New scores are now all above 90%. Initial test results found here:['index.html'](/docs/testing/lighthouse-testing/homepage-desktop.png) |
| ['Current subscribe.html'](/docs/testing/lighthouse-testing/subscribe-desktop2.png) | 70 | 91 | 100 | 90 | New scores are now all above 90% with the exception of 'Performance' (see above). Initial test results found here: [subscribe.html'](/docs/testing/lighthouse-testing/subscribe-desktop1.png)|
| ['Current privacy-policy.html'](/docs/testing/lighthouse-testing/privacy-policy-desktop2.png) | 94 | 92 | 100 | 90 | New scores are now all above 90%. Initial test results found here:['privacy-policy.html'](/docs/testing/lighthouse-testing/privacy-policy-desktop1.png) |
| ['Current signup.html'](/docs/testing/lighthouse-testing/signup-desktop2.png) | 94 | 92 | 100 | 90 | New scores are now all above 90%. Initial test results found here:['signup.html'](/docs/testing/lighthouse-testing/signup-desktop1.png)  |
| ['Current login.html'](/docs/testing/lighthouse-testing/login-desktop2.png) | 94 | 92 | 78 | 90 | New scores are now all above 90%. Initial test results found here:['login.html'](/docs/testing/lighthouse-testing/login-desktop1.png) |
| ['Current add-product.html'](/docs/testing/lighthouse-testing/add-product-desktop2.png) | 70 | 92 | 100 | 90 | Scores are above 90% on average, with the exception of 'Performance' (see above) Initial test results found here: ['add-product.html'](/docs/testing/lighthouse-testing/add-product-desktop1.png) |
| ['Current products.html'](/docs/testing/lighthouse-testing/products-desktop2.png) | 41 | 92 | 100 | 82 | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'SEO' (Which is beyond the scope of this project). Initial test results found here:['products.html'](/docs/testing/lighthouse-testing/products-desktop1.png) |
| ['Current product_detail.html'](/docs/testing/lighthouse-testing/product-detail-desktop2.png) | 56 | 92 | 100 | 91 | Scores are above 90% on average, with the exception of 'Performance' (see above) Initial test results found here: ['product_detail.html'](/docs/testing/lighthouse-testing/product-detail-desktop1.png) |
| ['Current bag.html'](/docs/testing/lighthouse-testing/bag-desktop2.png) | 74 | 92 | 100 | 82 | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'SEO' (Which is beyond the scope of this project). Initial test results found here:['bag.html'](/docs/testing/lighthouse-testing/bag-desktop1.png)  |
| ['Current checkout.html'](/docs/testing/lighthouse-testing/checkout-desktop2.png) | 71 | 90 | 78 | 91 | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'Best Practices'. The 'Best Practices issue stems from 'Stripe' and it's use of cookies: ['Screenshot'](/docs/testing/lighthouse-testing/stripe-cookies.png) .Not only is Stripe integral to the running of the site, cookies (Which is beyond the scope of this project)are also needed. As such, I have decided to leave this as is and research a better solution in the future. Initial test results found here: ['checkout.html'](/docs/testing/lighthouse-testing/checkout-desktop.png) |
| ['Current checkout_success.html'](/docs/testing/lighthouse-testing/checkout-success-desktop2.png) | 91 | 92 | 78 | 90 | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'Best Practices'. The 'Best Practices issue stems from 'Stripe' and it's use of cookies: ['Screenshot'](/docs/testing/lighthouse-testing/stripe-cookies.png) .Not only is Stripe integral to the running of the site, cookies (Which is beyond the scope of this project)are also needed. As such, I have decided to leave this as is and research a better solution in the future. Initial test results found here:['checkout_success.html'](/docs/testing/lighthouse-testing/checkout-success-desktop.png)  |
| ['Current favourites.html'](/docs/testing/lighthouse-testing/favourites-desktop2.png) | 54 | 92 | 100 | 82 |  | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'SEO' (Which is beyond the scope of this project). Initial test results found here:['favourites.html'](/docs/testing/lighthouse-testing/favourites-desktop.png) |
| ['Current profile.html'](/docs/testing/lighthouse-testing/profile-desktop2.png) | 91 | 92 | 100 | 90 | All scores above 90%. Initial scores here: ['profile.html'](/docs/testing/lighthouse-testing/profile-desktop.png)  |
| ['Current product_reviews.html'](/docs/testing/lighthouse-testing/product-reviews-desktop2.png) | 42 | 92 | 100 | 91 |  All scores above 90%, with the exception of 'Performance' (see above). Initial scores here: ['product_reviews.html'](/docs/testing/lighthouse-testing/product-reviews-desktop.png)|
| ['Current add_review.html'](/docs/testing/lighthouse-testing/add-review-desktop2.png) | 52 | 91 | 100 | 90 |  All scores above 90%, with the exception of 'Performance', (see above). Initial scores here:['add_review.html'](/docs/testing/lighthouse-testing/add_review-desktop.png) |




#### Mobile
| Page | Performance (%) | Accessibility (%) | Best Practices (%) | SEO (%) | If score is below 90% |
| :-- | :-: | :-: | :-: | :-: | :-- |
| ['Current index.html'](/docs/testing/lighthouse-testing/home-mobile2.png) | 82  | 98 | 100 | 90 | New scores are now all above 90% apart from 'Performance' (see above) Initial test results found here: ['index.html'](/docs/testing/lighthouse-testing/home-mobile.png)    |
| ['Current subscribe.html'](/docs/testing/lighthouse-testing/subscribe-mobile2.png) | 80 | 98 | 100 | 90 | New scores are now all above 90% apart from 'Performance' (see above) Initial test results found here:['subscribe.html'](/docs/testing/lighthouse-testing/subscribe-mobile1.png) |
| ['Current privacy-policy.html'](/docs/testing/lighthouse-testing/privacy-policy-mobile2.png) | 48 | 100 | 100 | 90 |  New scores are now all above 90% with the exception of 'Performance' (see above). Initial test results found here:['privacy-policy.html'](/docs/testing/lighthouse-testing/privacy-policy-mobile1.png)   |
| ['Current signup.html'](/docs/testing/lighthouse-testing/signup-mobile2.png) | 82 | 98 | 100 | 90 | New scores are now all above 90% apart from 'Performance' (see above) Initial test results found here:['signup.html'](/docs/testing/lighthouse-testing/signup-mobile1.png) |
| ['Current login.html'](/docs/testing/lighthouse-testing/login-mobile2.png) | 82 | 98 | 79 | 90 | New scores are now all above 90% apart from 'Performance' (see above) Initial test results found here:['login.html'](/docs/testing/lighthouse-testing/login-mobile1.png) |
| ['Current add-product.html'](/docs/testing/lighthouse-testing/add-product-mobile2.png) | 81 | 100 | 100 | 90 | New scores are now all above 90% apart from 'Performance' (see above) Initial test results found here:['add-product.html'](/docs/testing/lighthouse-testing/add-product-mobile1.png) |
| ['Current products.html'](/docs/testing/lighthouse-testing/products-mobile2.png) | 37 | 98 | 100 | 82 | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'SEO' (Which is beyond the scope of this project). Initial test results found here: ['products.html'](/docs/testing/lighthouse-testing/products-mobile1.png) |
| ['Current product_detail.html'](/docs/testing/lighthouse-testing/product-detail-mobile2.png) | 40 | 98 | 100 | 91 | New scores are now all above 90% apart from 'Performance' (see above) Initial test results found here:['product_detail.html'](/docs/testing/lighthouse-testing/product-detail-mobile1.png) |
| ['Current bag.html'](/docs/testing/lighthouse-testing/bag-mobile2.png) | 39 | 98 | 100 | 82 | SScores are above 90% on average, with the exception of 'Performance' (see above), and 'SEO' (Which is beyond the scope of this project). Initial test results found here: ['bag.html'](/docs/testing/lighthouse-testing/bag-mobile1.png) |
| ['Current checkout.html'](/docs/testing/lighthouse-testing/checkout-mobile2.png) | 30 | 95 | 79 | 91 | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'Best Practices'. The 'Best Practices issue stems from 'Stripe' and it's use of cookies: ['Screenshot'](/docs/testing/lighthouse-testing/stripe-cookies.png) .Not only is Stripe integral to the running of the site, cookies (Which is beyond the scope of this project)are also needed. As such, I have decided to leave this as is and research a better solution in the future. Initial test results found here: ['checkout.html'](/docs/testing/lighthouse-testing/checkout-mobile.png)  | 
| ['Current checkout_success.html'](/docs/testing/lighthouse-testing/checkout-mobile2.png) | 69 | 98 | 79 | 90 | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'Best Practices'. The 'Best Practices issue stems from 'Stripe' and it's use of cookies: ['Screenshot'](/docs/testing/lighthouse-testing/stripe-cookies.png) .Not only is Stripe integral to the running of the site, cookies (Which is beyond the scope of this project)are also needed. As such, I have decided to leave this as is and research a better solution in the future. Initial test results found here: ['checkout_success.html'](/docs/testing/lighthouse-testing/checkout-success-mobile.png)  |
| ['Current favourites.html'](/docs/testing/lighthouse-testing/favourites-mobile2.png) | 36 | 98 | 100 | 82 | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'SEO' (Which is beyond the scope of this project). Initial test results found here: ['favourites.html'](/docs/testing/lighthouse-testing/favourites-mobile.png)  |
| ['Current profile.html'](/docs/testing/lighthouse-testing/profile-mobile2.png) | 37 | 98 | 100 | 90 | Scores are above 90% on average, with the exception of 'Performance' (see above). Initial test results found here:  ['profile.html'](/docs/testing/lighthouse-testing/profile-mobile.png) |
| ['Current product_reviews.html'](/docs/testing/lighthouse-testing/product-reviews-mobile2.png) | 66 | 98 | 100 | 91 | All scores above 90%, with the exception of 'Performance' (see above). Initial scores here: ['product_reviews.html'](/docs/testing/lighthouse-testing/product-reviews-mobile.png) |
| ['Current add_review.html'](/docs/testing/lighthouse-testing/add_review-mobile2.png) | 73 | 98 | 100 | 90 | All scores above 90%, with the exception of 'Performance', (see above). Initial scores here: ['add_review.html'](/docs/testing/lighthouse-testing/add_review-mobile.png) |




## Manual Testing
### Testing User Stories
### **User Stories**
| **User Story #** | **As a/an** | **I want to be able to...** | **So that I can...** | **How was this achieved** | **Evidence**
| :-- | :-- | :-- | :-- | :-- | :-- |
| **VIEWING & NAVIGATION** |  |  |  |  |  |
| 1 | Shopper | Navigate around the site | View a list of products | The navbar's main navigation component allows the shoppers to browse for products. The all products link from the main navigation enables the visitors to view the list of all the products available on the site. | [desktop](./documentation/user_stories_testing/user-stories/.png), [tablet](./documentation/user_stories_testing/user-storyies/.png), [mobile](./documentation/user_stories_testing/user-stories/.png) |

## Bugs found during testing and development phase
### Solved Bugs
| # | Bugs, Errors and Issues | Solutions |
| :--- | :--- | :--- |
| 1 | Error:   | **Solution:** <br/>  |

### Known Bugs
| # | Known Bugs, Errors and Issues | Justification |
| :--- | :--- | :--- |
| 1 | Browser: Chrome, Error: **#**. This error appears ... | Justification explanation... |


