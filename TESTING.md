# **Keep it Sweet Testing Results**

![amiresponsive mock-ups of Keep it Sweet!](./docs/mockup-1.png)

<br/>

**[Link to the Deployed Site](https://keep-it-sweet-2ecaa2229785.herokuapp.com/)**

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
* [Manual Testing](#manual-testing)
    * [Testing User Stories](#testing-user-stories)
    * [Full Feature Testing](#full-feature-testing)
* [Responsivity Testing](#responsivity-testing)
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
| home/index.html | Pass | [Homepage](./docs/testing/html-validation/homepage.png) |
| bag.html | Pass | Validator came up with 2 warnings- [Warnings](./docs/testing/html-validation/bag-warnings.png) These were to do with an unnecessary use of 'type'. I found all files using this outdated info and deleted the 'type' attribute. Result here. [Bag](./docs/testing/html-validation/bag.png)  |
| checkout.html | Pass | Validator came up with 1 warning- [Warnings](./docs/testing/html-validation/checkout-warning.png) To do with an h1 element having no content. I decided to change this h1 elemnt into a div. While this made the spinner a bit smaller, the function worked perfectly fine. Result here. [Checkout](./docs/testing/html-validation/checkout.png)  |
| checkout_success.html | Pass | [Checkout_success](./docs/testing/html-validation/checkout-success.png)  |
| favourites.html | Pass | [Favourites](./docs/testing/html-validation/favourites.png)  |
| products.html | Pass | [Products](./docs/testing/html-validation/products.png)  |
| product_detail.html | Pass | [Product_detail](./docs/testing/html-validation/product-detail.png)  |
| add_product.html | Pass | [Add_product](./docs/testing/html-validation/add-product.png)  |
| edit_product.html | Pass | [Edit_product](./docs/testing/html-validation/edit-product.png)  |
| profile.html | Pass | [Profile](./docs/testing/html-validation/profile.png)  |
| product_reviews.html | Pass | Validator came up with 1 warning- [Warnings](./docs/testing/html-validation/product-reviews-warning.png) The error indicates that the action attribute of the form in the delete confirmation modal is empty. I made changes so that he action attribute in the form inside the modal is updated dynamically using JavaScript based on the data-form-action attribute of the delete button.I also set a fallback: (#) is provided in the action attribute to prevent it from being empty.[Product Reviews](./docs/testing/html-validation/product_reviews.png)  |
| add_review.html | Pass | [Add Review](./docs/testing/html-validation/add-review.png)  |
| edit_review.html | Pass | [Edit Review](./docs/testing/html-validation/edit-review.png)  |
| subscribe.html | Pass | [Subscribe](./docs/testing/html-validation/subscribe.png)  |
| privacy_policy.html | Pass | Validator came up with 2 warnings- [Warnings](./docs/testing/html-validation/privacy-policy-warning.png) The error indicates the p tags in the original template have invalid syntax because they include nested ul tags, which is not allowed. In HTML, a p tag cannot contain block-level elements like ul.With this in mind, I moved the ul tags outside of the p tags and adjusted the structure of the page. Results: [Privacy Policy](./docs/testing/html-validation/privacy-policy.png)  |

### CSS Validation
I used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate all CSS files by direct input.
| File | Result | Test Details & Screenshots |
| ---- | :-: | -------------------------- |
| /static/css/base.css | Pass | [base.css result](./docs/testing/jigsaw-css/base-css.png) |
| /checkout/static//checkout/css/checkout.css | Pass | [checkout.css result](./docs/testing/jigsaw-css/checkout-css.png) |
| /profiles/static/profiles/css/profile.css | Pass | [profile.css result](./docs/testing/jigsaw-css/profile-css.png) |

### JavaScript Validation
I used [JSHint](https://jshint.com/) to validate all JavaScript and JQuery files
| Function | Result | Validation Details & Screenshots |
| :-- | :-: | -------------------------- |
| **bag.html** |  |  |
| bag/templates/bag/bag.html (Update quantity on click) | All clear, no errors found | [bag](./docs/testing/jshint/bag-js.png) |
| **checkout app** |  |  |
| checkout/static/checkout/js/stript_elements.js (Stripe elements) | Added Stripe as a global variable- no errors- all clear. | [checkout.static.checkout.js.stripe_elements.js](./docs/testing/jshint/checkout-stripe-elements.png) |
| **products app** |  |  |
| products/templates/products/products.html (sort selector) | no errors- all clear. | [products.html- sort-selector](./docs/testing/jshint/products-sort-selector-js.png) |
| products/templates/products/products.html (scroll button) | no errors- all clear. | [products.html- scroll button](./docs/testing/jshint/products-scroll-js.png) |
| products/templates/products/edit_product.html (edit product- image) | no errors- all clear. | [edit products](./docs/testing/jshint/products-edit-image-js.png) |
| products/templates/products/add_product.html(add product- image) | no errors- all clear. | [add products](./docs/testing/jshint/products-add-image-js.png) |
| products/templates/products/includes/quantity_input_script.html| no errors- all clear. | [products.includes/quantity_input_script](./docs/testing/jshint/products-quantity-input-script.png) |
| **profiles app** |  |  |
| profiles/static/profiles/js/countryfield.js| no errors- all clear. | [profiles-countryfield.js](./docs/testing/jshint/profiles-countryfield.png) |
| **reviews app** |  |  |
| reviews/templates/reviews/product_reviews.html| no errors- all clear. | [reviews- modal](./docs/testing/jshint/reviews-product-reviews-modal-js.png) |
| **templates** |  |  |
| templates/base.html- 'show toasts'| no errors- all clear. | [templates.base.toasts](./docs/testing/jshint/templates-base-toasts.png) |

### Python Validation
I used [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) to lint my Python code.
| File | Result | Validation Details & Screenshots |
| :-- | :-: | -------------------------- |
| manage.py | All clear, no errors found | [manage.py](./docs/testing/python-linter/managepy.png)|
| custom_storages.py | All clear, no errors found | [custom_storages.py](./docs/testing/python-linter/env-py.png)|
| env.py | All clear, no errors found | [env.py](./docs/testing/python-linter/custom_storages.png)|
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
[Chrome DevTools' Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to test the performance, accessibility, best practices and SEO of the site.

#### Notes
During the first round of testing I saw some disappointing scores for 'Performance' and 'Best Practices'. <br> <br  >
For the purposes of this project, I focused on getting the scores for 'Accessibility' and 'Best Practices' as high as possible as those scores are within the remit and scope of the course. I did many rounds of research and testing to get these scores as high as possible. The details of these fixes can be found in the 'Fixed Bugs' section of this testing file. <br   >
With regards to 'Performance', A further step I hope to make in the future would be to upgrade images to 'next gen' formats like AVIF or Webp. I believe this would make a big step in bettering the performance. <br> <br  >
With regards to the 'Best Practices' scoring, issues center on the use of cookies by 'Stripe'. Stripe is integral to the working of this project. Example of evidence of this:['bag.html- dev tools- lighthouse screenshot'](/docs/testing/lighthouse-testing/bag-lighthouse-screenshot.png) I have found a fix for this issue- details of which can be found in the 'Bug Fixes' section, which put the Stripe script within a conditional block to ensure it only runs on the 'checkout' pages it is needed on. This has improved scores accross the site.


#### Desktop
| Page | Performance (%) | Accessibility (%) | Best Practices (%) | SEO (%) | If score is below 90% |
| :-- | :-: | :-: | :-: | :-: | :-- |
| [' Current index.html'](/docs/testing/lighthouse-testing/homepage-desktop-5.png) | 81 | 98 | 96 | 90 | New scores are now all above 90%, withthe exception of 'Performance' (see above). Initial test results found here:['index.html'](/docs/testing/lighthouse-testing/homepage-desktop.png) |
| ['Current subscribe.html' (Newsletter)](/docs/testing/lighthouse-testing/subscribe-desktop-5.png) | 86 | 98 | 100 | 90 | New scores are now all above 90%, with the exception of 'Performance' (see above). Initial test results found here: [subscribe.html'](/docs/testing/lighthouse-testing/subscribe-desktop1.png)|
| ['Current privacy-policy.html'](/docs/testing/lighthouse-testing/privacy-policy-desktop-5.png) | 96 | 100 | 100 | 90 | New scores are now all above 90%. Initial test results found here:['privacy-policy.html'](/docs/testing/lighthouse-testing/privacy-policy-desktop1.png) |
| ['Current signup.html'](/docs/testing/lighthouse-testing/signup-desktop-6.png) | 80 | 98 | 100 | 90 | New scores are now all above 90 with the exception of 'Performance'. Initial test results found here:['signup.html'](/docs/testing/lighthouse-testing/signup-desktop1.png)  |
| ['Current login.html'](/docs/testing/lighthouse-testing/login-desktop-4.png) | 76 | 98 | 96 | 90 | New scores are now all above 90%. Initial test results found here:['login.html'](/docs/testing/lighthouse-testing/login-desktop1.png) |
| ['Current add-product.html'](/docs/testing/lighthouse-testing/add-product-desktop-4.png) | 94 | 100 | 100 | 90 | Scores are above 90%. Initial test results found here: ['add-product.html'](/docs/testing/lighthouse-testing/add-product-desktop1.png) |
| ['Current products.html'](/docs/testing/lighthouse-testing/products-desktop-3.png) | 32 | 98 | 100 | 91 | Scores are above 90% on average, with the exception of 'Performance' (see above). Initial test results found here:['products.html'](/docs/testing/lighthouse-testing/products-desktop1.png) |
| ['Current product_detail.html'](/docs/testing/lighthouse-testing/product-detail-desktop-3.png) | 44 | 98 | 100 | 91 | Scores are above 90% on average, with the exception of 'Performance' (see above) Initial test results found here: ['product_detail.html'](/docs/testing/lighthouse-testing/product-detail-desktop1.png) |
| ['Current bag.html'](/docs/testing/lighthouse-testing/bag-desktop-4.png) | 70 | 98 | 100 | 82 | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'SEO' (Which is beyond the scope of this project). Initial test results found here:['bag.html'](/docs/testing/lighthouse-testing/bag-desktop1.png)  |
| ['Current checkout.html'](/docs/testing/lighthouse-testing/checkout-desktop-4.png) | 54 | 95 | 78 | 91 | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'Best Practices'. The 'Best Practices issue stems from 'Stripe' and it's use of cookies: ['Screenshot'](/docs/testing/lighthouse-testing/stripe-cookies.png) .Not only is Stripe integral to the running of the site, cookies (Which is beyond the scope of this project)are also needed. As such, I have decided to leave this as is and research a better solution in the future. Initial test results found here: ['checkout.html'](/docs/testing/lighthouse-testing/checkout-desktop.png) |
| ['Current checkout_success.html'](/docs/testing/lighthouse-testing/checkout-success-desktop-4.png) | 77 | 98 | 100 | 90 | Scores are above 90% on average, with the exception of 'Performance' (see above). Initial test results found here:['checkout_success.html'](/docs/testing/lighthouse-testing/checkout-success-desktop.png)  |
| ['Current favourites.html'](/docs/testing/lighthouse-testing/favourites-desktop-3.png) | 80 | 98 | 100 | 82 |  Scores are above 90% on average, with the exception of 'Performance' (see above), and 'SEO' (Which is beyond the scope of this project). Initial test results found here:['favourites.html'](/docs/testing/lighthouse-testing/favourites-desktop.png) |
| ['Current profile.html'](/docs/testing/lighthouse-testing/profile-desktop-3.png) | 70 | 100 | 100 | 90 | All scores above 90%, with the exception of 'Performance' (see above).S Initial scores here: ['profile.html'](/docs/testing/lighthouse-testing/profile-desktop.png)  |
| ['Current product_reviews.html'](/docs/testing/lighthouse-testing/product-reviews-desktop-3.png) | 40 | 98 | 100 | 91 |  All scores above 90%, with the exception of 'Performance' (see above). Initial scores here: ['product_reviews.html'](/docs/testing/lighthouse-testing/product-reviews-desktop.png)|
| ['Current add_review.html'](/docs/testing/lighthouse-testing/add-review-desktop-3.png) | 89 | 98 | 100 | 90 |  All scores above 90%, with the exception of 'Performance', (see above). Initial scores here:['add_review.html'](/docs/testing/lighthouse-testing/add_review-desktop.png) |

#### Mobile
| Page | Performance (%) | Accessibility (%) | Best Practices (%) | SEO (%) | If score is below 90% |
| :-- | :-: | :-: | :-: | :-: | :-- |
| ['Current index.html'](/docs/testing/lighthouse-testing/homepage-mobile-4.png) | 74 | 98 | 100 | 90 | New scores are now all above 90% apart from 'Performance' (see above) Initial test results found here: ['index.html'](/docs/testing/lighthouse-testing/homepage-mobile-1.png)    |
| ['Current subscribe.html'](/docs/testing/lighthouse-testing/subscribe-mobile-4.png) | 70 | 98 | 100 | 90 | New scores are now all above 90% apart from 'Performance' (see above) Initial test results found here:['subscribe.html'](/docs/testing/lighthouse-testing/subscribe-mobile1.png) |
| ['Current privacy-policy.html'](/docs/testing/lighthouse-testing/privacy-policy-mobile-5.png) | 63 | 100 | 100 | 90 |  New scores are now all above 90% with the exception of 'Performance' (see above). Initial test results found here:['privacy-policy.html'](/docs/testing/lighthouse-testing/privacy-policy-mobile1.png)   |
| ['Current signup.html'](/docs/testing/lighthouse-testing/signup-mobile-5.png) | 63 | 98 | 100 | 90 | New scores are now all above 90% apart from 'Performance' (see above) Initial test results found here:['signup.html'](/docs/testing/lighthouse-testing/signup-mobile1.png) |
| ['Current login.html'](/docs/testing/lighthouse-testing/login-mobile-4.png) | 92 | 98 | 100 | 90 | New scores are now all above 90%. Initial test results found here:['login.html'](/docs/testing/lighthouse-testing/login-mobile1.png) |
| ['Current add-product.html'](/docs/testing/lighthouse-testing/add-product-mobile-4.png) | 98 | 100 | 100 | 90 | New scores are now all above 90% apart from 'Performance' (see above) Initial test results found here:['add-product.html'](/docs/testing/lighthouse-testing/add-product-mobile1.png) |
| ['Current products.html'](/docs/testing/lighthouse-testing/products-mobile-4.png) | 36 | 98 | 100 | 91 | Scores are above 90% on average, with the exception of 'Performance' (see above). Initial test results found here: ['products.html'](/docs/testing/lighthouse-testing/products-mobile1.png) |
| ['Current product_detail.html'](/docs/testing/lighthouse-testing/product-detail-mobile-4.png) | 40 | 98 | 100 | 91 | New scores are now all above 90% apart from 'Performance' (see above) Initial test results found here:['product_detail.html'](/docs/testing/lighthouse-testing/product-detail-mobile1.png) |
| ['Current bag.html'](/docs/testing/lighthouse-testing/bag-mobile-4.png) | 56 | 98 | 100 | 82 | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'SEO' (Which is beyond the scope of this project). Initial test results found here: ['bag.html'](/docs/testing/lighthouse-testing/bag-mobile1.png) |
| ['Current checkout.html'](/docs/testing/lighthouse-testing/checkout-mobile-4.png) | 38 | 95 | 79 | 91 | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'Best Practices'. The 'Best Practices issue stems from 'Stripe' and it's use of cookies: ['Screenshot'](/docs/testing/lighthouse-testing/stripe-cookies.png) .Not only is Stripe integral to the running of the site, cookies (Which is beyond the scope of this project)are also needed. As such, I have decided to leave this as is and research a better solution in the future. Initial test results found here: ['checkout.html'](/docs/testing/lighthouse-testing/checkout-mobile.png)  | 
| ['Current checkout_success.html'](/docs/testing/lighthouse-testing/checkout-success-mobile-4.png) | 38 | 98 | 100 | 90 | Scores are above 90% on average, with the exception of 'Performance' (see above). Initial test results found here: ['checkout_success.html'](/docs/testing/lighthouse-testing/checkout-success-mobile.png)  |
| ['Current favourites.html'](/docs/testing/lighthouse-testing/favourites-mobile-5.png) | 50 | 98 | 100 | 82 | Scores are above 90% on average, with the exception of 'Performance' (see above), and 'SEO' (Which is beyond the scope of this project). Initial test results found here: ['favourites.html'](/docs/testing/lighthouse-testing/favourites-mobile.png)  |
| ['Current profile.html'](/docs/testing/lighthouse-testing/profile-mobile-4.png) | 45 | 100 | 100 | 90 | Scores are above 90% on average, with the exception of 'Performance' (see above). Initial test results found here:  ['profile.html'](/docs/testing/lighthouse-testing/profile-mobile.png) |
| ['Current product_reviews.html'](/docs/testing/lighthouse-testing/product-reviews-mobile-3.png) | 31 | 98 | 100 | 91 | All scores above 90%, with the exception of 'Performance' (see above). Initial scores here: ['product_reviews.html'](/docs/testing/lighthouse-testing/product-reviews-mobile.png) |
| ['Current add_review.html'](/docs/testing/lighthouse-testing/add-review-mobile-3.png) | 68 | 98 | 100 | 90 | All scores above 90%, with the exception of 'Performance', (see above). Initial scores here: ['add_review.html'](/docs/testing/lighthouse-testing/add-review-mobile.png) |


## Manual Testing
### Testing User Stories
### **User Stories**
| **USER STORY #** | **As a/an** | **I want to be able to...** | **So that I can...**| **How Was This Achieved** |  **Evidence**  |
|-----|-----|----|----|----|----|
| **VIEWING & NAVIGATION**    |
| 1                 | Customer           | Navigate around the site                                             | View a list of products available                                                  | Added clear navigation links and categories in the navbar.               | [user-story-1](./docs/testing/user-stories/user-story-1.png)                          |
| 2                 | Customer           | Easily and quickly understand the main purpose and products of 'Keep it Sweet' | Be sure I am in the right place for my needs                             | Created a welcoming homepage with a tagline and themed imagery.       | [user-story-2](./docs/testing/user-stories/user-story-2.png)       |
| 3                 | Customer           | View and search specific categories of products                      | Quickly access a range of products I may be interested in.               | Added a category menu and a search bar with filtering functionality.      | [user-story-3](./docs/testing/user-stories/user-story-3.png)                       |
| 4                 | Customer           | View individual product details                                      | Identify the price, description, product reviews, product image. | Built a detailed product page showing all relevant details.              | [user-story-4](./docs/testing/user-stories/user-story-4.png)                                |
| 5                 | Customer           | View the total amount of products in my shopping bag                 | Keep track of spending                                                   | Displayed a shopping bag summary in the navbar.                          | [user-story-5](./docs/testing/user-stories/user-story-5.png)          |
| 6                 | Customer           | View customer reviews of previous Keep it Sweet customers            | Feel safe in the knowledge that I will be treated well as a customer and feel confident about my purchase. | Integrated a product review section below each product detail.           | [user-story-6](./docs/testing/user-stories/user-story-6.png)                      |
| **REGISTRATION & USER ACCOUNTS**                                                                                                                                                                                               |
| 7                 | First time user           | Easily register for an account                                       | Have a personal account and be able to view my profile                   | Implemented user registration with Django's authentication system.        | [user-story-7](./docs/testing/user-stories/user-story-7.png)                |
| 8                 | First time user           | Receive an email after the above registration process                | Have feedback that my registration was successful                        | Configured email confirmation using Django's email backend.              | [user-story-6](./docs/testing/user-stories/user-story-8.png)                     |
| 9                 | Returning customer            | Easily log in and log out of my account                              | Access my personal information                                           | Added login/logout functionality using Django's authentication views.     | [user-story-9](./docs/testing/user-stories/user-story-9.png)              |
| 10                | Returning/ frequent customer  | Have a personalised user profile                                     | Access my stored information, order history, and favourites.               | Developed a user profile page showing order history and a page for favourite items.   | [user-story-10](./docs/testing/user-stories/user-story-10.png)             |
| **SORTING & SEARCHING**                                                                                                                                                                                                        |
| 11                | Customer           | Sort the list of available products                                  | Easily identify categorically and subcategorically sorted products        | Enabled sorting by category, price, and rating.                          | [user-story-11](./docs/testing/user-stories/user-story-11.png)                 |
| 12                | Customer           | Search for a product by name, or description             | Find a specific product                                                  | Added search functionality with keyword-based filtering.                  | [user-story-12](./docs/testing/user-stories/user-story-12.png)                       |
| 13                | Customer           | View the search results                                              | Identify products for more research or purchase                          | Displayed search results on a dedicated search results page.              | [user-story-13](./docs/testing/user-stories/user-story-13.png)                                |
| **PURCHASING & CHECKOUT**                                                                                                                                                                                                      |
| 14                | Customer           | Select the quantity of a product when purchasing                     | Ensure the correct quantity is purchased to meet my needs                | Added a quantity dropdown and buttons to increase and decreas quantity in the product detail page.                     | [user-story-14](./docs/testing/user-stories/user-story-14.png)                        |
| 15                | Customer           | View notifications/feedback when a product is added to the basket    | Receive immediate feedback if the action is completed                    | Implemented toast messages for add-to-basket actions.                     | [user-story-15](./docs/testing/user-stories/user-story-15.png)                 |
| 16                | Customer           | View items in my basket to be purchased                              | Quickly see the total cost of items                                      | Created a shopping bag page with an itemized list of products.            | [user-story-16](./docs/testing/user-stories/user-story-16.png)                                  |
| 17                | First time user           | Edit/update the items in my basket and adjust quantities             | Ensure my purchase is exactly what I want                                | Added functionality to update product quantities in the basket.           | [user-story-17](./docs/testing/user-stories/user-story-17.png)                              |
| 18                | Customer           | Enter payment information                                            | Checkout with minimal fuss.                                              | Integrated Stripe payment gateway for secure checkout.                    | [user-story-18](./docs/testing/user-stories/user-story-18.png)                 |
| 19                | Customer           | Receive confirmation of my order                                     | Know my payment has gone through and that my order is in the system.     | Displayed order confirmation on the success page.                         |   [user-story-19](./docs/testing/user-stories/user-story-19.png)                          |
| **SITE ADMIN**                                                                                                                                                                                                                |
| 20                | Store Owner               | Add a product                                                        | Add new items to my store                                                | Built an admin panel for adding new products.                             | [user-story-20](./docs/testing/user-stories/user-story-20.png)         |
| 21                | Store Owner               | Edit/update a product                                                | Amend a product's information so site info is up-to-date                 | Built an admin panel for editing product information.                     | [user-story-21](./docs/testing/user-stories/user-story-21.png)          |
| 22                | Store Owner               | Delete a product                                                     | Remove items that are no longer for sale                                 | Added a delete option in the admin panel with confirmation prompts.       | [user-story-22](./docs/testing/user-stories/user-story-22.png)                            |
| **DIGITAL MARKETING**                                                                                                                                                                                                         |
| 23                | Store Owner               | Signpost customers to social media                   | Build a community of repeat customers to drive sales                     | Added links to social media in the footer. These links open in a new tab. As this is an educational project, they open to general pages.          | [user-story-23](./docs/testing/user-stories/user-story-23.png)           |
| 24                | Store Owner | Signpost customers to Newsletter                       | Build a community of repeat customers to drive sales                                                    | Embedded a newsletter signup form accessed from main navbar.               | [user-story-24](./docs/testing/user-stories/user-story-24.png)                    |
| 25                | New/ returning customer               | Access site's social media                   | Access special offers, be updated on new products and read other reviews.                     | AAdded links to social media in the footer. These links open in a new tab. As this is an educational project, they open to general pages.          | [user-story-25](./docs/testing/user-stories/user-story-25.png)          |
| 26                | New/ returning customer | Sign up to digital marketing (Newsletter)                       | Access special offers, be updated on new products                                                    | Embedded a newsletter signup form accessed from main navbar.               | [user-story-26](./docs/testing/user-stories/user-story-26.png)                    |
| **PRODUCT REVIEWS**                                                                                                                                                                                                          |
| 27                | Customer           | View reviews for a product I am viewing                              | Be made aware of previous customers' views                               | Link to reviews below product details on the product page.               | [user-story-27](./docs/testing/user-stories/user-story-27.png)              |
| 28                | Returning Customer            | Add my own reviews to purchased products                             | Share my experiences of a product I purchased                            | Enabled logged-in users to submit reviews.                                | [user-story-28](./docs/testing/user-stories/user-story-28.png)                             |
| 29                | Returning Customer            | Edit my own reviews of purchased products                            | Maintain control of my published content                                 | Added an edit review option for logged-in users.                          | [user-story-29](./docs/testing/user-stories/user-story-29.png)                                  |
| 30                | Returning Customer            | Delete my own reviews of purchased products                          | Maintain control of my published content                                 | Added a delete review option with confirmation prompts.                   | [user-story-30](./docs/testing/user-stories/user-story-30.png)                       |
| **USER FAVOURITES LIST**                                                                                                                                                                                                      |
| 31                | Returning Customer            | Add favourite products to a 'Faves-list'                             | Access quickly in the future for speedier purchase                       | Built a 'Favourites' feature allowing users to save products.             | [user-story-31](./docs/testing/user-stories/user-story-31.png)    |
| 32                | Returning Customer            | Remove favourite products from a 'Faves-list'                        | Personalise my list to my own tastes                                     | Added a 'Remove from Favourites' button.                                  | [user-story-32](./docs/testing/user-stories/user-story-32.png)                           |


### Full Feature Testing
| **TEST** | **TEST DETAILS** | **EXPECTED RESULTS** | **ACTUAL RESULTS** | **PASS/FAIL** | **EVIDENCE**
| :-- | :-- | :-- | :-- | :-- | :-- |
| **General site opening** |  |  |  |  |   |
| 1 | Access URL: # |Site shows home page including Nav & Search Bar, Account, site content & footer | As Expected | Pass | [desktop](./docs/testing/full-feature/feature-test-1-desktop.png), [tablet](./docs/testing/full-feature/feature-test-1-tablet.png), [mobile](./docs/testing/full-feature/feature-test-1-mobile.png) |
| **TOP HEADER LINKS** |  |  |  |  |   |
| 2a | Desktop Test: Header renders correctly. |Desktop Top header shows Site name, searchbar, Account and Bag. | As Expected | Pass | [desktop](./docs/testing/full-feature/feature-test-2a-desktop.png) |
| 2b | Tablet and Mobile test: Header renders correctly. | Top header shows toggler, icon, Account and Bag. | As Expected | Pass | [tablet](./docs/testing/full-feature/feature-test-2b-tablet.png), [mobile](./docs/testing/full-feature/feature-test-2b-mobile.png)|
| 3 | Click on site name |On desktop, when site logo/ name clicked, user is navigated back to homepage. | As Expected | Pass | [desktop](./docs/testing/full-feature/feature-test-3-desktop.png) |
| 4a | Searchbar: No search query. |If nothing entered into searchbar and a search ran, user is navigated to 'Products' page and a 'toast' message alerts user to issue.   | As Expected | Pass | [desktop](./docs/testing/full-feature/feature-test-4a-desktop.png), [tablet](./docs/testing/full-feature/feature-test-4a-tablet.png), [mobile](./docs/testing/full-feature/feature-test-4a-mobile.png) |
| 4b | Searchbar: Product Search. |Return correct results when searching for a product.   | As Expected | Pass | [4b results](./docs/testing/full-feature/feature-test-4b.png)  |
| 5 | My Account: Dropdown. | On clicking the 'My Account' icon, users given s dropdown including 'Register' and 'Login' options.   | As Expected | Pass | [5 results](./docs/testing/full-feature/feature-test-5.png)  |
| 6 | My Account: Register. | On selecting the 'Register' option, users are navigated to the dedicated 'Sign Up' page.   | As Expected | Pass | [6 results](./docs/testing/full-feature/feature-test-6.png)  |
| 7 | My Account: Login. | On selecting the 'Login' option, users are navigated to the dedicated 'Sign In' page.   | As Expected | Pass | [7 results](./docs/testing/full-feature/feature-test-7.png)  |
| 8 | Bag icon | On selecting the 'Bag' icon, users are navigated to the 'Bag' page.   | As Expected | Pass | [8 results](./docs/testing/full-feature/feature-test-8.png)  |
| **Main Nav and Links** |  |  |  |  |   |
| 9a | Main Nav renders correctly on desktop | On desktop, the main nav links are in a horizontal list of options: 'All Products', 'Categories', and 'Newsletter'.   | As Expected | Pass | [9a results](./docs/testing/full-feature/feature-test-9a.png)  |
| 9b | Main Nav renders correctly on mobile and tablet | On mobile and tablet, the main nave links are accessed via the toggler and render as avertical list of options: 'All Products', 'Categories', and 'Newsletter'.   | As Expected | Pass | [9b results- tablet](./docs/testing/full-feature/feature-test-9b-tablet.png), [9b results- mobile](./docs/testing/full-feature/feature-test-9b-mobile.png)   |
| 10 | Products menu item |  Selecting 'All Products' triggers a dropdown including options for sorting items by: Price, Rating, Category and All Products.   | As Expected | Pass | [desktop](./docs/testing/full-feature/feature-test-10-desktop.png),[tablet](./docs/testing/full-feature/feature-test-9b-tablet.png), [mobile](./docs/testing/full-feature/feature-test-10-mobile.png)   |
| 11 | Products/ By Price selection |  Selecting 'By Price' from 'All Products' navigates the user to a page where all the site's products are sorted by price.   | As Expected | Pass | [11 results](./docs/testing/full-feature/feature-test-11.png)   |
| 12 | Products/ By Rating selection |  Selecting 'By Rating' from 'All Products' navigates the user to a page where all the site's products are sorted by rating.   | As Expected | Pass | [12 results](./docs/testing/full-feature/feature-test-12.png)   |
| 13 | Products/ By Category selection |  Selecting 'By Category' from 'All Products' navigates the user to a page where all the site's products are sorted by category.   | As Expected | Pass | [13 results](./docs/testing/full-feature/feature-test-13.png)   |
| 14 | Categories menu item |  Selecting 'Categories' triggers a dropdown including options for viewing items from a specific category. Categories are: Soft, Fizzy, Chocolate, Chewy, Hard and 'Special Diet.   | As Expected | Pass | [desktop](./docs/testing/full-feature/feature-test-14-desktop.png),[tablet](./docs/testing/full-feature/feature-test-14-tablet.png), [mobile](./docs/testing/full-feature/feature-test-14-mobile.png)   |
| 15 | Category selection |  When selecting a category from the Category options, users are navigated to a page of products belonging to that category.   | As Expected | Pass | [15 results](./docs/testing/full-feature/feature-test-15.png)   |
| 16 | Newsletter Link |  When selecting the 'Newsletter' link in the nav nar, users are directed to the subscribe.html page.   | As Expected | Pass | [16 results](./docs/testing/full-feature/feature-test-16.png)   |
| **Footer and Links** |  |  |  |  |   |
| 17 | Facebook Link |  When selecting the 'Facebook' link, user is directed to the standard facebook site which opens in a new tab. (As this is for ed purposes only, there is no 'Keep it Sweet' page.)   | As Expected | Pass | N/A   |
| 18 | Instagram Link |  When selecting the 'Instagram' link, user is directed to the standard Instagram site which opens in a new tab. (As this is for ed purposes only, there is no 'Keep it Sweet' page.)   | As Expected | Pass | N/A   |
| 19 | Support Link: (support@keepitsweet.com) |  When selecting the 'support@keepitsweet.com' link, user is directed to the standard Google sign in site which opens in a new tab. (As this is for ed purposes only, there is no 'Keep it Sweet' page.)   | As Expected | Pass | N/A   |
| 20 | Privacy Policy Link |  When selecting the 'Privacy Policy' link, user is directed to the site's 'Stripe Cookies Privacy Policy' page.   | As Expected | Pass | N/A   |
| **Newsletter Signup** |  |  |  |  |   |
| 21 | Sign up button: Empty/ incorrect form fields |  leaving fields blank or incorrectly filled in, form validation stops the form from submitting.   | As Expected | Pass | [Blank form](./docs/testing/full-feature/feature-test-21-blank-form.png), [Incorrect email field](./docs/testing/full-feature/feature-test-21-incorrect-email-field.png)   |
| 22 | Submit button |  Success message when correct form submitted   | As Expected | Pass | [22 Results](./docs/testing/full-feature/feature-test-22.png)   |
| 23 | Record Stored |  Subscription appears in admin panel   | As Expected | Pass | [Blank form](./docs/testing/full-feature/feature-test-23.png)   |
| **Bag** |  |  |  |  |   |
| 24 | Bag page displays prices |  Price, Subtotal, Bag total, Delivery, Grand Total listed accurately | As Expected | Pass | [24 Results](./docs/testing/full-feature/feature-test-24.png) |
| 25 | Bag page displays message if total under free delivery rate |  Message evident with clear signposting as to how much more to spend to qualify for free delivery. | As Expected | Pass | [25 Results](./docs/testing/full-feature/feature-test-25.png) |
| 26 | Bag page displays quantity of products required |  Current quantity amount evident. | As Expected | Pass | [26 Results](./docs/testing/full-feature/feature-test-26.png) |
| 27 | Bag quantity adjustment |  Users can increase or decrease product quantities. | As Expected | Pass | [27 Results](./docs/testing/full-feature/feature-test-27.png) |
| 28 | Bag product removal |  Users can remove a product from the bag | As Expected | [28 Results](./docs/testing/full-feature/feature-test-28.png) |
| 29 | Bag page shows product options |  Product options selected by user, displayed on relevant products | As Expected | Pass  | [29 Results](./docs/testing/full-feature/feature-test-29.png) |
| 30 | Secure checkout button |  Secure checkout button navigates user to checkout page | As Expected | Pass | N/A |
| 31 | Keep shopping button |  Keep shopping button navigates user to products page | As Expected | Pass | N/A |
| 32 | Empty Bag |  Bag page is rendered even with no products in it. | As Expected | Pass | [32 Results](./docs/testing/full-feature/feature-test-32.png) |
| **Favourites App** |  |  |  |  |   |
| 33 | No logged in user. |  Users not logged in can browse site, but, should not be able to add favourites. | As Expected | Pass | [33 Results](./docs/testing/full-feature/feature-test-33.png) |
| 34 | Add products to Favourites: Logged in user. |   Registered, logged in users able to add products to a favourites list. | As Expected | Pass | [34 Results](./docs/testing/full-feature/feature-test-34.png) |
| 35 | View Favourites list |   Registered, logged in users able to view their favourites list. | As Expected | Pass | [35 Results](./docs/testing/full-feature/feature-test-35.png) |
| 36 | Remove from Favourites list |   Registered, logged in users able to delete products from their favourites list. | As Expected | Pass | [36 Results](./docs/testing/full-feature/feature-test-36.png) |
| 37 | View empty favourites list |   Registered, logged in users able to access an empty list page. | As Expected | Pass | [37 Results](./docs/testing/full-feature/feature-test-37.png) |
| **Reviews App** |  |  |  |  |   |
| 38 | View Reviews- No review- All users. |  All users, both logged in and not, users should be able to view a page with no reviews for a product. | As Expected | Pass | [38 Results](./docs/testing/full-feature/feature-test-38.png) |
| 39 | View Reviews-All users. |  All users, both logged in and not, should be able to view reviews for a product. | As Expected | Pass | [39 Results](./docs/testing/full-feature/feature-test-39.png) |
| 40 | Add Review. |  Users able to add reviews for a product. | As Expected | Pass | [40 Results](./docs/testing/full-feature/feature-test-40.png) |
| 41 | Edit Review: (Context: Not the user's review) |  Users should not be able to edit or delete other user's reviews. No buttons to Edit or Delete review. | As Expected | Pass | [41 Results](./docs/testing/full-feature/feature-test-41.png) |
| 42 | Edit Review: (Context: User CAN edit own review) |  Users should be able to edit or delete their reviews. Reviews have buttons for Edit and Delete. | As Expected | Pass | [42 Results](./docs/testing/full-feature/feature-test-42.png) |
| 43 | Delete Review (Context: User CAN'T delete reviews which are not their own) |  Users should be able to edit or delete their reviews. Reviews have buttons for Edit and Delete. | As Expected | Pass | [43 Results](./docs/testing/full-feature/feature-test-41.png) |
| 44 | Delete Review: (Context: User CAN delete own review) |  Users should be able to edit or delete their reviews. Reviews have buttons for Edit and Delete. | As Expected | Pass | [44 Results](./docs/testing/full-feature/feature-test-44.png) |
| **CHECKOUT & PAYMENT** |  |  |  |  |  |
| 45 | Checkout Form: (Form Validation- incomplete form) |  Form should not submit if mandatory fields are not populated. | As Expected | Pass | [45 Results](./docs/testing/full-feature/feature-test-45.png) |
| 46 | Adjust bag link|  User is taken back to bag page | As Expected | Pass | N/A |
| 47 | Payment Success- user feedback|  After pressing 'Complete Order' and a successful payment, the user is given in page feedback that the order has been submitted in the form of a 'Thank You' page with all order details and a 'Success' toast message. | As Expected | Pass | [47 Results](./docs/testing/full-feature/feature-test-47.png) |
| 48 | Completed order can be viewed in profile section|  Order information is listed on Checkout Success page and information provided to user that a confirmation email has been sent to their email account | As Expected | Pass | [48 Results](./docs/testing/full-feature/feature-test-48.png) |
| 49 | Confirmation email works correctly| Confirmation email has been received and contains correct information | As Expected | Pass | [49 Results](./docs/testing/full-feature/feature-test-49.png) |
| 50 | Order history is correct| The order can be seen in Order History on user profile page | As Expected | Pass | [50 Results](./docs/testing/full-feature/feature-test-48.png) |
| 51 | Test link to order detail on Profile Page| Link takes user to order detail on Order History page in User Profile | As Expected | Pass | [51 Results](./docs/testing/full-feature/feature-test-51.png) |
| **Products** |  |  |  |  |  |
| 52 | View Products- Non logged in user | Non logged in users are able to view product details but have no options to 'Add to Favourites' or edit/ delete products details. | As Expected | Pass | [52 Results](./docs/testing/full-feature/feature-test-52.png) |
| 53 | View Products- logged in user- Customer | Customers are able to view product details and have the option to 'Add to Favourites' or but have no options toedit/ delete products details. | As Expected | Pass | [53 Results](./docs/testing/full-feature/feature-test-53.png) |
| 54 | View Products- logged in user- Staff/ superuser | Staff. admin are able to view product details and have the option to 'Add to Favourites' and to edit/ delete products details. | As Expected | Pass | [54 Results](./docs/testing/full-feature/feature-test-54.png) |
| 55 | CRUD- Add Products- Non logged in user | Non logged in users are not able to access 'Product Management' options which are accessed through the 'My Accounts' menu option. Options should only be 'Register' or 'Login'. | As Expected | Pass | [55 Results](./docs/testing/full-feature/feature-test-55.png) |
| 56 | View Products- logged in user- Customer | Customers are not able to access 'Product Management' options which are accessed through the 'My Accounts' menu option. Options should only be 'My Profile', 'Favourites' and 'Logout'. | As Expected | Pass | [56 Results](./docs/testing/full-feature/feature-test-56.png) |
| 57 | CRUD- Add Products- logged in user- Staff/ superuser | Staff/admin are able to access the 'Product Management' option found in 'My Accounts' | As Expected | Pass | [57 Results](./docs/testing/full-feature/feature-test-57.png) |
| 58 | CRUD- Add Products- logged in user- Staff/ superuser | Staff/admin are able to access the Product Management pages and use the form to add products to the database/ site. | As Expected | Pass | [58 Results](./docs/testing/full-feature/feature-test-58.png) |
| 59 | CRUD- Edit Products- logged in user- Staff/ superuser | Staff/admin are able to access the Product Management pages and use the form to add products to the database/ site. | As Expected | Pass | [59 Results](./docs/testing/full-feature/feature-test-59.png) |
| 60 | CRUD- Delete Products- logged in user- Staff/ superuser | Staff/admin are able to delete products to the database/ site. | As Expected | Pass | [60 Results](./docs/testing/full-feature/feature-test-60.png) |
| **Register** |  |  |  |  |  |
| 60 |  Register New Users: Context- incorrect form submission. | Form does not submit if mandatory information not entered or entered incorrectly | As Expected | Pass | [60 No Email](./docs/testing/full-feature/feature-test-60-no-email.png), [60 No Username](./docs/testing/full-feature/feature-test-60-no-username.png), [60 Mismatch Passwords](./docs/testing/full-feature/feature-test-60-password-mismatch.png) | 
| 61 |  Register New Users: Context- Successful Registration. | on successful form submission user is alerted to email sent for verification | As Expected | Pass | [61 Results](./docs/testing/full-feature/feature-test-61.png) |
| 62 |  Register New Users: Context- Successful Registration- email Confirm/Verify | Users revieve an email with a link to verify their details, this navigates them to the site to verify, finally recieving confirmation of verified details. | As Expected | Pass | [62 Results](./docs/testing/full-feature/feature-test-62.png) |
| **Sign In** |  |  |  |  |  |
| 63 |  Login | Registered users are able to login in to the site and their successful sign in be evident. | As Expected | Pass | [63 Results](./docs/testing/full-feature/feature-test-63.png) |


## Responsivity Testing
Site was tested accross a range of 3 device types: Nest Hub (desktop), iPad Mini (tablet) and iPhone 14 Pro Max (mobile).

While most testing was done across these 3 specific devices, other testing was done to ensure som elevel of consistency.

| **Page** | **Expected Result** | **Pass/Fail** | **Evidence** |
| :-- | :-- | :-- | :-- |
| homepage/index.html | Site content resizes. For mobile, search bar becomes a dropdown, nav var toggles to a dropdown. On mobile, footer stacks. | Pass | [Nest Hub](/docs/testing/responsivity-testing/home-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/home-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/home-mobile.png)  |
| subscribe.html (Newsletter) | Site content resizes and layout adapts. Header and footer as above | Pass | [Nest Hub](/docs/testing/responsivity-testing/newsletter-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/newsletter-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/newsletter-mobile.png)  |
| privacy_policy.html | Site content resizes and layout adapts. Header and footer as above | Pass | [Nest Hub](/docs/testing/responsivity-testing/privacy-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/privacy-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/privacy-mobile.png)  |
| signup.html | Site content resizes and layout adapts. Header and footer as above | Pass | [Nest Hub](/docs/testing/responsivity-testing/sign-up-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/sign-up-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/sign-up-mobile.png)  |
| login.html | Site content resizes and layout adapts. Header and footer as above | Pass | [Nest Hub](/docs/testing/responsivity-testing/log-in-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/log-in-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/log-in-mobile.png)  |
| products.html | Header and footer as above. Site content resizes and layout adapts. Product card veviews on x-large screens = 4 columns, on Nest Hub = 3 columns, on Tablet = 2 columns and on mobile= single column. | Pass | [X-Large Screen](/docs/testing/responsivity-testing/view-products-Xlarge.png), [Nest Hub](/docs/testing/responsivity-testing/view-products-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/view-products-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/view-products-mobile.png)  |
| product_detail.html | Site content resizes and layout adapts. Header and footer as above. Content as a single column on mobile, and 2 columns on tablet and desktop. | Pass | [Nest Hub](/docs/testing/responsivity-testing/view-product-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/view-product-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/view-product-mobile.png)  |
| add_product.html | Site content resizes and layout adapts. Header and footer as above. | Pass | [Nest Hub](/docs/testing/responsivity-testing/add-product-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/add-product-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/add-product-mobile.png)  |
| edit_product.html | Site content resizes and layout adapts. Header and footer as above. | Pass | [Nest Hub](/docs/testing/responsivity-testing/edit-product-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/edit-product-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/edit-product-mobile.png)  |
| profile.html | Site content resizes and layout adapts. Header and footer as above. On desktop, site uses a 2 column layout, moving to a 1 column layout on other device types. | Pass | [Nest Hub](/docs/testing/responsivity-testing/user-profile-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/user-profile-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/user-profile-mobile.png)  |
| reviews.html| Site content resizes and layout adapts. Header and footer as above. On desktop and mobile, site uses a 2 column layout, moving to a 1 column layout on mobile. | Pass | [Nest Hub](/docs/testing/responsivity-testing/read-reviews-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/read-reviews-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/read-reviews-mobile.png)  |
| add_review.html | Site content resizes and layout adapts. Header and footer as above. | Pass | [Nest Hub](/docs/testing/responsivity-testing/add-a-review-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/add-a-review-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/add-a-review-mobile.png)  |
| edit_review.html | Site content resizes and layout adapts. Header and footer as above. | Pass | [Nest Hub](/docs/testing/responsivity-testing/edit-a-review-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/edit-a-review-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/edit-a-review-mobile.png)  |
| bag.html | Site content resizes and layout adapts. Header and footer as above. | Pass | [Nest Hub](/docs/testing/responsivity-testing/bag-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/bag-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/bag-mobile.png)  |
| checkout.html | Site content resizes and layout adapts. Header and footer as above. | Pass | [Nest Hub](/docs/testing/responsivity-testing/checkout-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/checkout-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/checkout-mobile.png)  |
| checkout_success.html | Site content resizes and layout adapts. Header and footer as above. | Pass | [Nest Hub](/docs/testing/responsivity-testing/checkout-success-desktop.png), [iPad Mini ](./docs/testing/responsivity-testing/checkout-success-tablet.png), [iPhone 14](./docs/testing/responsivity-testing/checkout-success-mobile.png)  |


## Bugs found during testing and development phase
### Solved Bugs
| #   | Bugs, Errors and Issues   | Solution |Additional info |
| --- | --- | --- | --- |
| 1   | **Error:** Bag quantity section rendering poorly on mobile devices. [Example](./docs/bugs-and-fixes/bug-fix-1.png)   | **Solution:** Improved layout a number of ways: Re-organised the quantity input and increment and decrement buttons to stack vertically on mobile devices. Used CSS media query for smaller screens `max-width: 576px` and used `flex-direction: column`. [New mobile layout example](./docs/bugs-and-fixes/bug-fix-1a.png)  |   |
| 2   | **Error:** Lower than hoped "Best Practices" scores across the site. During Lighthouse testing, scores were in the 70s (orange). An in-depth look into the Lighthouse report made it clear that this was due to the running of Stripe cookies throughout the site. [Example](./docs/bugs-and-fixes/bug-fix-2.png) | **Solution:** As Stripe and cookies are integral to the running of the site, after research, I chose to utilize Django template inheritance block structure (as seen in other places on the site) in conjunction with a conditional statement. [Example](./docs/bugs-and-fixes/bug-fix-2a.png). This allows Stripe to run only on pages with "checkout" in the name. This improved scores across the site except for the "checkout" pages where Stripe still runs. [Result](./docs/bugs-and-fixes/bug-fix-2b.png) | **Links:** **[Django Template Documentation - Conditional Statements](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#if)**, **[Django resolver_match Object Documentation](https://docs.djangoproject.com/en/5.1/ref/request-response/#django.http.HttpRequest.resolver_match)**, **[Stripe Official Docs: Getting Started with Stripe.js](https://docs.stripe.com/js)** |
| 3   | **Error:** `"POST /subscribe/ HTTP/1.1" 500 159845`. When attempting to subscribe to the newsletter. | **Solution:** This indicated that there was no corresponding table in the database! On checking the models, the models were there, but the `migrations` folder was empty, indicating that migrations were not applied. I created a migration `python manage.py makemigrations subscribe`. Then checked the Django admin panel and could see 'subscribers' but no data. Running `python manage.py migrate --fake-initial` told Django to treat the existing database table as if it was created by the initial migration. On restarting and pushing, a test worked, and the 'Subscribers' panel in Django Admin had populated the subscriber data. | **Links:** **[Django docs - migrations](https://docs.djangoproject.com/en/5.1/topics/migrations/)**, **[Coders Camp: How to force migrations to a db if some tables already exist in Django?](https://www.thecoderscamp.com/how-to-force-migrations-to-a-db-if-some-tables-already-exist-in-djangodjango/)**, **[Coders Camp - Django migrate -fake and -fake-initial explained](https://www.thecoderscamp.com/django-migrate-fake-and-fake-initial-explaineddjango/)** , **[Django project forum - Purpose and Use Cases of 'fake initial' in Comparison to the 'fake flag'](https://forum.djangoproject.com/t/purpose-and-use-cases-of-fake-initial-in-comparison-to-the-fake-flag/22516)** |
| 4   | **Error:** Email verification `500` when attempting to subscribe to the newsletter. While the site was navigating to the success page, no confirmation emails were coming through on 'temp-mail' or 'gmail' accounts. | **Solution:** After checking the general settings in the `settings.py` file with no success, I checked the configuration variables. I reset the email host and associated password, following the steps again. I edited the variables in the Heroku config vars and updated the `settings.py` file. This worked, and emails were delivered successfully.   |    |
| 5   | **Error:** Inconsistencies between the deployed site and the local site. After deployment, I came across an issue with not having the full ability to work locally to make amendments to the site. For example, CSS was not loading locally, making development and testing very difficult.  | **Solution:** One issue was that Gitpod was not recognizing environment variables. To fix this, I created an `env.py` file to store all environment variables, ensuring it was not included in version control. Then, within the `settings.py` file, I amended the `os.import` section. [Example](./docs/bugs-and-fixes/bug-fix-5.png). Through this, I was able to achieve better parity between the deployed and local versions of the app.  |  Thanks to Tutor Support for this fix.  |
| 6   | **Error:** Toast Success - Checkout Success - Order link. The order link in this message was rendering as raw HTML, not as a standard, clickable link. [Example](./docs/bugs-and-fixes/bug-fix-6.png)         | **Solution:** Used the "safe" filter within `toast_success.html` so Django allows it to be rendered as safe HTML. Updated the `favourites/views.py` file by adding `from django.utils.html import format_html` to the imports and used `reverse('favourites')` and `format_html` within the views file to render the message. [Example](./docs/bugs-and-fixes/bug-fix-6b.png). The result is a properly rendered success message with a working link: [Result](./docs/bugs-and-fixes/bug-fix-6a.png). | **Links:** **[Django docs - format_html](https://docs.djangoproject.com/en/5.1/ref/utils/#django.utils.html.format_html)**, **[Django docs - reverse](https://docs.djangoproject.com/en/5.1/ref/urlresolvers/#reverse)**, **[Django docs - safe filter](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/#safe)** |
| 7   | **Error:** `ModuleNotFoundError` after deployment to Heroku. | **Solution:** Error due to a dependencies Incompatibility centering around the version of Python used in local development and the version used by Heroku. By adding a `runtime.txt` file with an working Python version `python-3.9.19`, this allowed Heroku to know which version to use and ensured parity between the local and deployed environment. | Thanks to Tutor Support for this fix. |
| 8   | **Error:** `Stripe Webhook Error`- during development, when attempting to create the webhook element for Stripe, I was recieving no indication in the terminal that the webhook was working and inspection of the logs in stripe showed `401 ERR` and a 100% failure rate. | **Solution:** Error due to a small but critical step which I kept missing which was to `Open Port 8000`.   |  Thanks to the slack community for this 'reminder'/ fix. |
| 9   | **Error:** `Browser errors logged to the console`- [Example](./docs/bugs-and-fixes/bug-fix-9.png) Lower than hoped "Best Practices" and "Performance" scores across the site. During Lighthouse testing, scores were in the 70s (orange) and even in the red for some 'Performance' Scores. An in-depth look into the Lighthouse report made it clear that an element of this was the order in which scripts were running, and non critical scripts slowing down the page load etc.  | **Solution:** One step was to move javaScript scripts down to the bottom of the body as opposed to them being in the head. Also, ensuring jquery is loaded before Bootstrap JS * |  |
| 10   | **Error:** `eliminate render-blocking resources`- [Example](./docs/bugs-and-fixes/bug-fix-10.png) Lower than hoped "Best Practices" and "Performance" scores across the site. During Lighthouse testing, scores were in the 70s (orange) and even in the red for some 'Performance' Scores. An in-depth look into the Lighthouse report made it clear that an element of this was the order in which scripts were running, and non critical scripts slowing down the page load etc.  | **Solution:** I experimented with a number of ideas found in articles on *Page Speed Checklist.com*: Thes included *Async & Defer*, *Optimize Google Fonts*, *Eliminate Render Blocking Resources*, *Asynchronous CSS*, and *Lazy Load Images*. In the end, I chose to Lazy load images and the current set up of my head as this configuration allowed for better 'Best Practices' and 'Accessibility' scores. [Current head element](./docs/bugs-and-fixes/bug-fix-10a.png)  | **[Pagespeedchecklist.com- Get Up To Speed with Website Performance Optimization](https://pagespeedchecklist.com/)**, **[Pagespeedchecklist.com- What's the Difference Between Async & Defer?](https://pagespeedchecklist.com/async-and-defer)**, **[Pagespeedchecklist.com- Async CSS + Resource Hints = Speedy Fonts](https://pagespeedchecklist.com/asynchronous-google-fonts)**, **[Pagespeedchecklist.com- Streamline Loading for Page Speed](https://pagespeedchecklist.com/eliminate-render-blocking-resources)**, **[Pagespeedchecklist.com- Reduce & Optimize Web Fonts for Page Speed](https://pagespeedchecklist.com/optimize-fonts)**, **[Pagespeedchecklist.com- Lazy Image Loading + JavaScript Fallback](https://pagespeedchecklist.com/lazy-load-images)**|

### Known Bugs
| # | Known Bugs, Errors and Issues | Justification |
| :--- | :--- | :--- |
| 1 | During Lighthouse Testing, pages with images had poorer that hoped 'Performance' scores For Example: [Image](./docs/bugs-and-fixes/known-bugs/known-bug-1.png)  | Further work to be done on the updating of all images on this site to a nextGen format like AVIF of WebP. As this site is just for educational purposes only and 'Performance' is beyond the scope of the project at this level, I have decided to leave it for further development at this time. |
| 2 | During Lighthouse Testing, pages which utilize 'Stripe' cookies had poorer that hoped 'Best Practices' scores For Example: [Image](./docs/bugs-and-fixes/known-bugs/known-bug-2.png)  | Further work to be done on understanding the use of Cookies in Stripe. As this site is just for educational purposes only and in depth knowledge of Stripe Cookies is beyond the scope of the project at this level, I have decided to leave it for further development at this time. |
| 3 | During User Stories and Features testing, discoverd that the email being recieved by newly Registered users is formatted incorrectly. Example: [Image](./docs/bugs-and-fixes/known-bugs/known-bug-3.png)  | This will require more research into Google Account settings. As is, the current implementation works for the purly educational purposes of the project. |
| 4 | While inspecting the terminal during tests of the 'checkout' functionality, I kept seeing a 404 error: ` ""GET /robots.txt HTTP/1.1" 404 3453` Example: [Image](./docs/bugs-and-fixes/known-bugs/known-bug-4.png)  | Research so far points to this is to do with web crawlers and SEO. Both are beyond the scope of this project and so I have parked this error for now.  |


