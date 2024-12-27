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
I implemented automated testing on both **Python forms** using Django's `SimpleTestCase` and **JavaScript functionality** using **Jest** to ensure error-free behavior across key parts of the site.

#### Forms Testing  
- Focused on validating form functionality and ensuring form inputs meet expected validation rules.  
- **Example:** Testing required fields, invalid inputs, and clean method logic for Django forms.

#### JavaScript Testing with Jest  
- Tested dynamic behaviors in the frontend, such as triggering modals.  
- **Example:** Ensuring modals display correctly when interacting with buttons.

---

### Testing Results  

| **Test Name**               | **Test Type**                | **Description**                                                               | **Result** | **Screenshot**                                      |
|-----------------------------|------------------------------|-------------------------------------------------------------------------------|------------|----------------------------------------------------|
| **ReviewForm Validation**   | Django - SimpleTestCase      | Uses 4 tests to ensure the functionality and validation of the `ReviewForm` in the reviews app: Valid Data Test, Missing Title Test, Missing Content Test, Invalid Rating Test.       | ✅ Pass    | ![Screenshot](/docs/testing/automated-testing/review-forms-testing.png)   |
| **CheckoutForm Validation** | Django - SimpleTestCase      | Uses 4 tests to ensure the functionality and validation of the `orderForm` in the checkout app: Valid Data Test, Missing Required Fields Test, Optional Fields Test, Invalid Email Test. | ✅ Pass    | ![Screenshot](/docs/testing/automated-testing/checkout-form-testing.png) |
| **UserProfilesForm Validation** | Django - SimpleTestCase      | Uses 2 tests to ensure the functionality and validation of the `UserProfileForm` in the checkout app: Correct Fields Test, Labels Removed Test | ✅ Pass    | ![Screenshot](/docs/testing/automated-testing/profile-form-testing.png) |
| **Modal Trigger Test**      | Jest                         | Ensures the delete confirmation modal is triggered when the delete button is clicked. | ✅ Pass    | ![Screenshot](/docs/testing/automated-testing/jest-tests.png)                          |
| **Toast Display Test**      | Jest                         | Verifies that Bootstrap's toast messages are displayed correctly.             | ✅ Pass    | ![Screenshot](/docs/testing/automated-testing/jest-tests.png)                          |


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
| Page | Result | Test Details & Screenshots |
| ---- | :-: | -------------------------- |
| ./# | # errors, <br/># warnings | [scrollToTop script](./docus/.png) |

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
#### Desktop
| Page | Performance (%) | Accessibility (%) | Best Practices (%) | SEO (%) | If score is below 90% |
| :-- | :-: | :-: | :-: | :-: | :-- |
| ['index.html'](./docs.png) | # | # | # | # | Scores are above 90% on average |

#### Mobile
| Page | Performance (%) | Accessibility (%) | Best Practices (%) | SEO (%) | If score is below 90% |
| :-- | :-: | :-: | :-: | :-: | :-- |
| ['index.html'](./docs/.png) | #  | # | # | # | comment |

### WAVE Web Accessibility Evaluation Tool
[WAVE](https://wave.webaim.org/) was used to ensure that Keep It Sweet's content is also accessible to individuals with disabilities. WAVE can identify many accessibility and Web Content Accessibility Guideline (WCAG) errors, which are then corrected following the results of the initial evaluation.

In order to fully validate the page, I used the WAVE Chrome extension. This enabled me to test the pages that require user authentication.

| Page | WAVE This Page Result | Reasons for not fixing the contrast errors, if any |
| :-- | --- | --- |
| # Page | no errors |  |


### Django Automated Testing
For the automated testing, the writing and running of these tests used [Django's built in test module](https://docs.djangoproject.com/en/4.1/topics/testing/overview/). For each installed application, I created a folder called tests, added the ```__init__.py``` file and the separate files for testing the views, models and forms.

I also used coverage to generate the report and find out the percentage of statements that I was able to cover and those that I missed for every installed application. I tried to achieve as close to the 100% mark as I possibly can, but I am still fairly new to using Automated Testing and am looking forward to learning more to reach this goal.

#### Coverage
| Installed App Coverage Report | Cover in Percentage | Screenshot of Coverage Report |
| -- | :-: | :-: |
| # app | #% | [bag app cover](./documentation/coverage_report/coverage-report-#-app.png) |

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


