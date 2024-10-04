# **Shop K-Beauty Testing Results**

![amiresponsive mock-ups of SHOP K-BEAUTY](./docs/.png)

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
At the project inception, I installed [PyCodeStyle](https://pycodestyle.pycqa.org/en/latest/intro.html#configuration) in my IDE and throughout the development, I was using it to test and fix the errors as they appear. I also used [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) to lint my Python code.
| File | Result | Validation Details & Screenshots |
| :-- | :-: | -------------------------- |
| #.py | All clear, no errors found | [#](./docs.png)|
| **SHOP_** |  |  |
| #.py | All clear, no errors found | [#.py validation](./docs/.png) |

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


