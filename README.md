# **Keep It Sweet**

![amiresponsive mock-ups of Keep It Sweet](/docs/mockup-1.png)

**[Link to the Deployed Site](https://keep-it-sweet-2ecaa2229785.herokuapp.com/)**

# Project Overview

Keep It Sweet is a fictitious, ecommerce full stack project built using Django, Python, JavaScript and Bootstrap 4. The site is deployed to Heroku, uses Amazon S3 for cloud storage and Stripe for payment processing.

It has been produced as my fourth milestone project for Code Institute's Level 5 Diploma in Web Application Development (Full Stack Software Development).
<br/>

---

## TABLE OF CONTENTS

* [User Experience](#user-experience)
    * [User Stories](#user-stories)
* [Design](#design)    
    * [Typography](#typography)
    * [Colour Scheme](#colour-scheme)
    * [Wireframes](#wireframes)
* [Database Design](#database-design)
    * [Relational Database](#relational-database)
    * [Entity Relationship Diagram](#entity-relationship-diagram)
* [Models](#models)
    * [Custom Models](#custom-models)
* [Features](#features)
* [Technologies Used](#technologies-used)
    * [Front End Technologies](#front-end-technologies)
    * [Back End Technologies](#back-end-technologies)
    * [Additional Technologies](#additional-technologies)
* [Testing](#testing)
* [Deployment](#deployment)
* [Submission](#submission)
* [Credits](#credits)
    * [Code](#code) 
    * [Content](#content)
    * [Media](#media) 
    * [Acknowledgements](#acknowledgements)

---

## User Experience (UX)

-   ### User stories

| **USER STORY #** | **As a/an** | **I want to be able to...** | **So that I can...** |
| --- | --- | --- | --- |
| **VIEWING & NAVIGATION** |   |   |
| 1 | First time user | Navigate around the site | View a list of products  |
| 2 | First time user | Easily and quickly understand the main purpose and products of the 'Keep it Sweet' company | Be sure I am in the right place for my needs  |
| 3 | First time user | View and search specific categories of products | Quickly access a range of products I may be interested in.  |
| 4 | First time user | View individual product details | Identify the price, description, product reviews, product image.  |
| 5 | First time user | View the total amount of products in my shopping bag | Keep track of spending  |
| 6 | First time user | View customer reviews of previous Keep it Sweet's customers | Feel safe in the knowledge that I will be treated well as a customer and feel confident about my purchase.  |
| **REGISTRATION & USER ACCOUNTS** |   |   |
| 7 | First time user | Easily register for an account | Have a personal account and be able to view my profile |
| 8 | First time user | Recieve an email after the above registration process| Have feedback that my registration was successful |
| 9 | Returning user | Easily log in and log out of my account| Access my personal information |
| 10 | Returning/ frequent user | Have a personalised user profile | Access my stored information, order history, order confirmations (and wishlist/ faves list) |
| **SORTING & SEARCHING** |   |   |
| 11 | First time user | Sort the list of available products | Easily identify categorically sorted products |
| 12 | First time user | Search for a product or multiple products by name or description | Find a specific product |
| 13 | First time user | View the search results | Identify products for more research or purchase |
| **PURCHASING & CHECKOUT** |   |   |
| 14 | First time user | Select the quantity of a product when purchasing | Ensure the correct quantity is purchased to meet customer need |
| 15 | First time user | View notifications/ feedback when a product is added to the basket | recieve immediate feedback if action completed |
| 16 | First time user | View items in my basket to be purchased | quickly see the total cost of items |
| 17 | First time user | Edit/ update the items in my basket and adjust quantities | Ensure my purchase is exactly what I want |
| 18 | First time user | Enter payment information | Checkout with minimal fuss. |
| 19 | First time user | Recieve confirmation of my order | know my payment has gone through and that my order is in the system. |
| **SITE ADMIN** |   |   |
| 20 | Store Owner | Add a product | Add new items to my store |
| 21 | Store Owner | Edit/ update a product | Amend a product's information so site info is up to date |
| 22 | Store Owner | Delete a product | Remove items that are no longer for sale |
| **DIGITAL MARKETING** |   |   |
| 23 | Store Owner |     Signpost customers to social media. | Build a community of repeat customers to drive sales |
| 24 | Store Owner |     Signpost customers digital marketing (newsletter) and special offers | Build a community of repeat customers to drive sales |
| 25 | Customer |     Access site's social media | Access special offers, be updated on new products and read other reviews. |
| 26 | Customer |     Sign up to digital marketing (Newsletter) | Access special offers, be updated on new products |
| **PRODUCT REVIEWS** |   |   |
| 27 | First time user | View reviews for a product I am viewing | be made aware of previous customer's views |
| 28 | Returning/ frequent user | Be able to add my own reviews to purchased products | share my experiences of a product I purchased |
| 29 | Returning/ frequent user | Be able to edit my own reviews to purchased products | maintain control of my published content |
| 30 | Returning/ frequent user | Be able to delete my own reviews to purchased products | maintain control of my published content |
| **USER FAVOURITES LIST** |   |   |
| 31 | Returning/ frequent user | Add favourite products to a 'Faves -list' | Access quickly in the future for speedier purchase |
| 32 | Returning/ frequent user | Remove favourite products to a 'Faves -list' | Keep products I really like and personalise my list to my own tastes |
| **Customer Contact App** |   |   |
| 33 | Customer | Contact the store via a form | Easily ask questions or get support without needing to call. |
| 34 | Customer | Receive a confirmation that my message was sent | Ensure my query has been received and will be responded to. |
| 35 | Customer | Provide my name, email, and message in the form | Ensure my message is personalized and that I receive a response. |
| 36 | Store Owner | Receive customer inquiries through the contact form | Provide customer support and answer any queries. |

---

## Design:

### Typography

The **Keep It Sweet** project uses carefully chosen fonts to enhance the visual appeal and readability of the website. Here's a breakdown of the typography used:

#### Fonts
1. **Poppins** (Default Font)
   - Applied across most body text for a clean and modern appearance.
   - Ensures high readability and a professional look.

2. **Oleo Script** (Heading and Emphasized Text)
   - Used for headings, emphasized text, and decorative elements.
   - Provides a playful and elegant feel that complements the shop's theme.

#### Font Weights
- **700 (Bold)**: Used for headings, emphasized text, and key elements like prices and totals, ensuring important information stands out.

#### Usage
- **Headings and Decorative Elements**:
  - All headings (`h1` to `h6`), `.grand-total`, `.price`, and `.card-body p` use the `Oleo Script` font to create a sense of fun and excitement.
- **Body Text**:
  - General body text and paragraphs (`p`) use the `Poppins` font for readability and simplicity.
- **Buttons and Reviews**:
  - Buttons (`.btn`, `.add-review-btn`) and review content (`.review-content`) also leverage `Poppins` for uniformity and clarity.

#### Fallback Fonts
Both fonts are paired with fallback options (`Arial`, `sans-serif`) to ensure compatibility across devices and browsers.

#### Accessibility
- High-contrast font colors ensure readability for users with visual impairments.
- Larger font sizes and bold weights are used for important elements to improve visibility and user experience.


### Colour Scheme

The **Keep It Sweet** project features a vibrant and playful colour scheme designed to evoke a sense of fun and excitement, perfectly aligning with the theme of an online sweet shop.

![Checkout Success Page Wireframe](./docs/colour-pallet.png)

#### Primary Colours
1. **Pink** `#ff7eb3`
   - Used as the primary brand colour to convey a cheerful and inviting tone.
   - Prominent in navigation bars, buttons, and interactive elements.

2. **Black** `#000000`
   - Provides contrast and a sleek, modern look.
   - Commonly used in text, buttons, and banners for readability and emphasis.

3. **White** `#ffffff`
   - Ensures a clean and simple background for sections and text.
   - Maintains a balance with the bold and vibrant colours.

4. **Red Shades**  
   - **Light Red** `#ff5678`  
   - **Dark Red** `#ff4500`  
   - Used for delete buttons and warnings to grab user attention.
   - Highlights important actions or states in the interface.

#### Secondary Colours
- **Blue Shades**  
   - **Link Blue** `#0056b3`  
   - **Hover Blue** `#003d80`  
   - Applied to general links for better visibility and accessibility.
   - Hover states use darker shades for an interactive feel.

- **Gray Shades**  
   - **Placeholder Gray** `#aab7c4`  
   - **Text Gray** `#333`  
   - Used for placeholder text and supporting content.
   - Ensures secondary text is legible without overpowering primary elements.

This vibrant and accessible colour scheme creates an engaging user experience, reinforcing the sweet and playful theme of the shop.



### **Wireframes**
The wireframes were created using [Balsamiq](https://balsamiq.cloud/).

* Home Page
![Home Page Wireframe](./docs/wireframes/homepage-wf.png)

* Products Page
![Products Page Wireframe](./docs/wireframes/products-wf.png)

* Product Detail Page
![Product Detail Page Wireframe](./docs/wireframes/product-detail-wf.png)

* Bag Page
![Bag Page Wireframe](./docs/wireframes/bag-wf.png)

* Checkout Page
![Checkout Page Wireframe](./docs/wireframes/checkout-wf.png)

* Checkout Success Page
![Checkout Success Page Wireframe](./docs/wireframes/checkout-success-wf.png)

* Favourites Page
![Favourites Page Wireframe](./docs/wireframes/favourites-wf.png)

* Profile Page
![Profile Page Wireframe](./docs/wireframes/profile-wf.png)

* Reviews Page
![Reviews Page Wireframe](./docs/wireframes/reviews-wf.png)

* Add/Edit reviews Page
![Add/Edit reviews Page Wireframe](./docs/wireframes/add-edit-review-wf.png)

* Product Management Page (Add and Delete)
![Product Management Page Wireframe](./docs/wireframes/add-edit-product-wf.png)

* Register Page
![Register Page Wireframe](./docs/wireframes/register-wf.png)

* Login Page
![Login Page Wireframe](./docs/wireframes/login-wf.png)

* Newsletter Subscription Page
![Newsletter Subscription Page Wireframe](./docs/wireframes/newsletter-subscription-wf.png)

---
## Database
### Relational Database
(This project utilises PostgreSQL, a relational database mangement system (RDBMS) managed by Django which offers PostgreSQL as a service. )

### Entity Relationship Diagram
As illustrated in the ERD, each model corresponds to a database table, and each field corresponds to a column in that table.

<img src="./docs/erd-updated.png">

## Models
### Table - Description and Relationships

| **Table Name**          | **Purpose**                                                                 | **Relationships**                                                                                          |
|-------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **User**                | Stores user authentication data, such as username, email, password, and admin status. | - **One-to-One** with `User Profile` (user_id is the foreign key).                                        |
|                         |                                                                             | - **One-to-Many** with `Review` (a user can write many reviews).                                          |
|                         |                                                                             | - **One-to-Many** with `Favourite` (a user can have many favourite products).                             |
| **User Profile**        | Stores additional details for a user, like address and contact information. | - **One-to-One** with `User` (foreign key: `user_id`).                                                    |
|                         |                                                                             | - **One-to-Many** with `Order` (a user profile can have many orders).                                     |
| **Category Entity**     | Represents product categories, like chocolates or candies.                  | - **One-to-Many** with `Product` (a category can have many products).                                     |
| **Product**             | Stores information about products such as name, price, description, and SKU. | - **Many-to-One** with `Category Entity` (foreign key: `category_id`).                                    |
|                         |                                                                             | - **One-to-Many** with `OrderLineItem` (a product can appear in multiple order items).                    |
|                         |                                                                             | - **One-to-Many** with `Review` (a product can have multiple reviews).                                    |
|                         |                                                                             | - **One-to-Many** with `Favourite` (a product can be favourited by many users).                           |
| **Order**               | Represents a user’s purchase order, including totals, costs, and delivery details. | - **Many-to-One** with `User Profile` (foreign key: `user_profile_id`).                                   |
|                         |                                                                             | - **One-to-Many** with `OrderLineItem` (an order can contain multiple products).                          |
| **OrderLineItem**       | Represents individual items within an order, including quantity and options. | - **Many-to-One** with `Order` (foreign key: `order_id`).                                                 |
|                         |                                                                             | - **Many-to-One** with `Product` (foreign key: `product_id`).                                             |

### Custom Models

| **Table Name**          | **Purpose**                                                                 | **Relationships**                                                                                          |
|-------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| **Review**              | Stores user-generated reviews for products, including title, content, and ratings. | - **Many-to-One** with `User` (foreign key: `user_id`).                                                   |
|                         |                                                                             | - **Many-to-One** with `Product` (foreign key: `product_id`).                                             |
| **Favourite**           | Allows users to mark products as favourites.                                | - **Many-to-One** with `User` (foreign key: `user_id`).                                                   |
|                         |                                                                             | - **Many-to-One** with `Product` (foreign key: `product_id`).                                             |
| **Newsletter Subscriber** | Stores email subscriptions for newsletters, including date of subscription. | - No direct relationships (can be submitted by both registered and unregistered users).   |
| **ContactMessage** | Stores user-submitted messages from the contact form. | - No direct relationships (can be submitted by both registered and unregistered users).                 |


## Features

#### Main Site Features

- **Clear Navigation**: Intuitive navigation allows users to easily browse through different pages, including product categories, the shopping bag, and their profile.
- **Special Offers**: A prominently displayed strapline highlights special offers, in this case,free delivery on orders over a certain amount.
- **User Profiles**: Leveraging Django Allauth, registered users can create and manage their accounts, save address information, and view their order history for a personalized experience.
- **Responsive Design**: Fully optimized for a range of device sizes, ensuring a seamless shopping experience on desktops, tablets, and smartphones.
- **Footer with Social Links**: Selected pages feature a footer with links to Keep It Sweet's social media profiles and access to a means of contacting the company directly through a contact form. Future updates will expand the footer to include additional navigation links to internal pages. A current example being the 'Privacy Policy' page.
- **Newsletter Subscription**: Users can subscribe to the Keep It Sweet newsletter to receive updates on the latest products, special offers, and seasonal promotions.
- **Favourites App**: Logged-in users can save their favourite products to a personalized favourites list, making it easy to find and purchase their preferred sweets.
- **Reviews App**: Users can view reviews left by other customers on product pages. Registered users can write, edit, and delete their own reviews to share their experiences with others.
- **Staff Product Management**: Staff users with superuser privileges can add new products, edit existing product details, and manage product information directly within the site through a secure admin interface.
- **Toast Messages**: The site utilises *Toast Messages* throughout the site to keep users informad as to the success/ or failure of user actions. For example, a success model with the bag details when adding items to the bag, success or error messages when adding reviews or products and info messages when appropriate, for example *You are now editing___*. The use of *toast messages* is key for users to be confident in the completion of actions on the site.

#### Home App
- **Navigation**: Users can easily access product categories, the shopping bag, their profile, Newsletter Subscription and their favourites page. The navigation also includes a **Search Bar** for quick product searches.

- **Hero Image and Strapline**: A vibrant hero image and a main strapline welcome users to Keep It Sweet, showcasing the brand's fun and joyful identity. Special offers or promotions are highlighted here. 

- **Footer**: Includes links to Keep It Sweet’s social media profiles, such as Instagram and Facebook, as well as an email link, along with a copyright statement. There is currently a link to a 'Privacy Policy'. Future updates will expand the footer to include links to all pages, terms and conditions.

#### Product App
- **Product Display**: Users can browse a wide selection of sweets, each displayed with an image, name, price, and star rating. Products are grouped into clear categories, such as "Hard," "Chewy," and "Chocolate," making it easy to find specific treats.

- **Search, Filter, and Sorting**: The app includes a **Search Bar** and options to:
  - Filter products by category.
  - Sort products by price, rating, or category for a customized browsing experience.

- **Product Detail Pages**: Each product has its own detailed page featuring:
  - A larger product image.
  - Full product description, including dietary options.
  - Add-to-bag functionality, including the ability to increase or decrease the quantity.
  - JavaScript ensures the decrement button cannot go below one item.
  - A redirection option to continue shopping for more products.

- **Product Options**:For appropriate products, those in the *Special Diet* category, the product detail page has the addition of a dropdown with options including *Low Sugar*, *Lactose Free* and *Plant Based*.   This information is rendered throughout the purchase and payment process ensuring users are fully in control of what they are purchasing at every stage.

- **Toast Messages**: Upon adding items to the bag, an automated popup with a Toast message confirms the action was successful and displays the number of items added.

- **Favourites Integration**: Logged-in users can save products to their favourites list directly from the product detail page for quick access later.

- **CRUD Functionality for Staff**: Staff users can:
  - Add, edit, and delete products through the admin interface.
  - Manage product information and ensure the catalog is up-to-date.

- **Responsive Design**: The product pages are fully optimized for all device sizes, ensuring a smooth user experience on mobile, tablet, and desktop screens.

#### Bag App

- **Product Summary Page**: Displays a detailed list of products selected for purchase, including:
  - Product images, names, and prices.
  - Options to increase or decrease the quantity of each item.
  - A **Remove Link** to delete items from the bag if needed.
- **Delivery Costs and Free Delivery Threshold**:
  - Users can view the delivery costs based on their current total.
  - A notification advises how much more needs to be spent to qualify for free delivery.
  - If the minimum spend for free delivery is not reached, the applicable delivery costs are clearly displayed.
- **Secure Checkout**: A **Secure Checkout** button allows users to proceed directly to the checkout page to complete their purchase.
- **Bag Modal Integration**: The app integrates seamlessly with the bag modal, dynamically updating the total cost and items in real-time as changes are made on the product summary page.
- **Responsive Design**: Fully optimized for all device sizes, ensuring users can manage their bag easily on mobile, tablet, and desktop screens.

#### Checkout App

- **Order Completion**: Users finalize their purchase by:
  - Filling out a form with delivery and payment details.
  - Clicking the **Complete Order** button to confirm the order.
  - Having the ability to adjust the bag contents right up until the final action.
  - Being informed of the total amount to be charged to their card before finalizing the purchase.

- **Payment Integration**: The app integrates with the **Stripe** payment solution to securely process payments.

- **Order Management**:
  - A bag session is stored in the database, with order details added to the order table for record-keeping.
  - Users can save their delivery and order details, which are linked to their profile.

- **Order History**: 
  - Registered users can view their previous orders in the **Order History** section of their profile.
  - This feature allows users to track past purchases and easily reorder items if needed.

- **Email Confirmation**:
  - Users receive an order confirmation email in their inbox, including:
    - The order number for reference.
    - A summary of their purchase.
  - This provides assurance and a record of the transaction.

- **Responsive Design**: The checkout process is fully optimized for all device sizes, ensuring users can complete their orders seamlessly on mobile, tablet, and desktop screens.

#### Sign-up/Login

- **Sign-in Page**:
  - Allows existing users to log into their account by entering their username and password.
  - Includes a link to the **Reset Password** page for users who have forgotten their password.
  - Provides links to return to the **Home Page** for easy navigation if needed.

- **Sign-up for New Users**:
  - Anonymous users can create an account by entering their email address and setting a secure password in the relevant fields.
  - **Toast Messages** notify users of the status of their login or sign-up process, providing immediate feedback on success or errors.

- **Account Verification**:
  - New customers receive an email with a verification link.
  - Users must click the link to confirm their email address and complete the sign-up process, ensuring account security.

- **Responsive Design**:
  - The sign-up and login pages are fully optimized for all device sizes, ensuring users can access and manage their accounts easily on mobile, tablet, and desktop screens.


#### Admin Features

- **Secure Access**:
  - CRUD functionality is protected by the Django `@login_required` decorator, ensuring only logged-in users with superuser permissions can access product management features.
  - Anonymous users or users without superuser privileges cannot access or modify the data store.

- **Add Product**:
  - Superusers can add new products via a dedicated **Product Management Form**.
  - The form includes fields for **Category**, **SKU**, **Name**, **Description**, **Options**, **Price**, **Rating**, and **Image URL**.
  - Optional fields are clearly marked with an asterisk (`*`).
  - If no image is provided, a default image is automatically applied.

- **Edit Product**:
  - Superusers can edit existing products by using the **Edit Link** on the product page, which opens the product's details in an editable form.
  - A **Toast Feedback Modal** informs superusers that they are in edit mode.
  - Product details can be updated and saved with immediate effect, ensuring the catalog remains accurate and up-to-date.

- **Delete Product**:
  - Superusers can delete a product by clicking the **Delete Link** on the product page.
  - Upon deletion, a **Toast Notification** confirms that the product was successfully removed.
  - Deletion is immediate, streamlining the process of managing outdated or incorrect products.

These admin features ensure efficient and secure management of the product catalog, empowering superusers to maintain the integrity and quality of the online store.

#### Subscribe App

- **Subscription Features**:
  - Both unregistered and registered users can sign up to join the **Keep It Sweet** mailing list.
  - Users are required to provide their email address to subscribe.
  - Upon successful sign-up, a **Success Message** is displayed to confirm the action.

- **Validation and Error Handling**:
  - The app validates user input to ensure the email address is valid and all required fields are completed.
  - Users are shown **Warning Messages** if the email is invalid or a required field is missing.

- **Admin Management**:
  - Subscription records are saved in the admin area for easy management.
  - Details such as **Name**, **Email Address**, **Date Subscribed**,  are recorded and accessible by admin users.

This app enables seamless management of the mailing list and provides users with an efficient way to stay updated on the latest products and offers from Keep It Sweet.

#### Favourites App

- **Save Favourite Products**:
  - Registered users can add products to their favourites list by clicking the **Add to Favourites** button on product pages.
  - The favourites feature allows users to easily revisit and purchase their preferred sweets without needing to search for them again.

- **Manage Favourites**:
  - Users can view their saved favourites in a dedicated **Favourites Page**, which displays:
    - Product images.
    - Names and prices of their saved products.
  - Products can be removed from the favourites list with a single click.

- **Personalized Experience**:
  - Each user's favourites list is unique to their account, ensuring a personalized experience.
  - The favourites list is accessible after logging in and persists across sessions.

- **Responsive Design**:
  - The favourites functionality is fully optimized for all device sizes, allowing users to manage their favourites on mobile, tablet, and desktop screens.

This app provides users with a convenient way to save and organize their favourite products, enhancing the overall shopping experience on **Keep It Sweet**.

#### Reviews App

- **View Reviews**:
  - All users, whether registered or not, can view product reviews on product detail pages.
  - Reviews provide insights into the experiences of other customers, helping users make informed decisions.

- **Write Reviews**:
  - Registered users can submit reviews for products they have purchased.
  - Reviews include a title, content, and a star rating to give detailed feedback.

- **Manage Reviews**:
  - Registered users can manage their reviews with the following features:
    - **Edit Reviews**: Users can update their existing reviews to correct or change their feedback.
    - **Delete Reviews**: Users can remove their reviews if they choose to.

- **Feedback and Validation**:
  - Forms include validation to ensure required fields are completed before submission.
  - Toast messages provide users with immediate feedback when their reviews are successfully submitted, updated, or deleted.

- **Responsive Design**:
  - The reviews functionality is fully optimized for mobile, tablet, and desktop devices, ensuring a seamless experience across all platforms.

The **Reviews App** adds a layer of community interaction to the **Keep It Sweet** site, fostering trust and engagement through customer feedback.

### NEW FEATURE!
#### Contact App

- **Contact the Team**:
  - All users can use the contact form to send inquiries, feedback, or requests to the **Keep It Sweet** team.
  - The contact form includes fields for the user's name, email address, and a detailed message.

- **Form Validation**:
  - The contact form ensures all required fields are completed before submission.
  - Users are notified of any errors or omissions with clear, accessible messages.

- **Feedback**:
  - Success and error toast messages provide immediate feedback to users:
    - **Success Toast**: Notifies users when their message has been successfully sent.
    - **Error Toast**: Informs users of missing or invalid fields to correct before resubmitting.

- **Responsive Design**:
  - The contact form is fully optimized for mobile, tablet, and desktop devices.
  - It ensures a seamless and user-friendly experience across all platforms.

- **Accessibility**:
  - Designed with accessibility in mind, including:
    - Clear form labels for screen readers.
    - ARIA attributes for improved usability.
    - High contrast and easy-to-read fonts.

The **Contact App** enhances the **Keep It Sweet** site by providing a reliable and user-friendly communication channel for customers to connect with the team, ensuring feedback and inquiries are managed effectively.

#### Future Features
- A rewards app where purchases make points for freebies and spcial offers.
- A 'Special Offers' / 'Bundle Builder' app where users can bundle an number of products together and get a discount.
- Additional content on the home page with featured or new/ seasonal products promoted beneath the hero section.
- Continued development of the Contact app allowing site admin to respond to messages from customer inquiries.

## Technologies Used

### **Languages Used**
- [**HTML5**](https://en.wikipedia.org/wiki/HTML5) – Used for the structure and semantic content of the site.
- [**CSS3**](https://en.wikipedia.org/wiki/CSS#CSS_3) – Applied for styling, layout, and responsive design.
- [**JavaScript**](https://en.wikipedia.org/wiki/JavaScript) – Used to enhance interactivity and dynamic content.
- [**Python**](https://www.python.org/) – The core programming language for the backend.

### **Frameworks Used**
- [**Django 3.2**](https://docs.djangoproject.com/en/3.2/releases/3.2/) – A high-level Python web framework.
- [**Bootstrap 4.4.1**](https://getbootstrap.com/docs/4.4.1/getting-started/introduction/) – A responsive front-end framework that helps structure layouts and components efficiently.

### **Databases Used**
- [**SQLite3**](https://docs.djangoproject.com/en/3.2/ref/databases/#sqlite-notes) – Used as the development database.
- Postgresql from Code Institute – A cloud-hosted relational database used for the live deployment.

### **Libraries and Packages Used**
- [**Django Allauth**](https://django-allauth.readthedocs.io/en/latest/) – Manages user authentication, including social logins and account verification.
- [**JQuery 3.4.1**](https://jquery.com/) – A lightweight JavaScript library for DOM manipulation and event handling.
- [**Font Awesome**](https://fontawesome.com/) – Provides icons for enhanced UI design.
- [**Django Countries 7.2.1**](https://pypi.org/project/django-countries/7.2.1/) – Enables country selection for user forms and models.
- [**Django Crispy Forms 1.14.0**](https://pypi.org/project/django-crispy-forms/) – Enhances the styling and functionality of Django forms.
- [**Gunicorn 23.0.0**](https://gunicorn.org/) – A Python WSGI HTTP server used to serve the application in production.
- [**Pillow 11.0.0**](https://pypi.org/project/Pillow/) – A Python imaging library required for handling image uploads.
- [**Psycopg2 2.9.10**](https://pypi.org/project/psycopg2/) – A PostgreSQL database adapter for Django.
- [**Boto3 1.35.74**](https://pypi.org/project/boto3/) – The Amazon Web Services (AWS) SDK for Python, used for handling S3 storage.
- [**Django Storages 1.14.4**](https://django-storages.readthedocs.io/en/latest/) – A custom storage backend for handling media and static files in AWS S3.
- [**Stripe 11.2.0**](https://stripe.com/) – Integrated for payment processing in the e-commerce functionality.

### **Tools and Platforms Used**
- [**Git**](https://git-scm.com/) – Used for version control and managing project commits.
- [**GitHub**](https://github.com/) – Hosts the project repository and manages collaborative development.
- [**Google Chrome DevTools**](https://developer.chrome.com/docs/devtools/) – Utilized for debugging, performance audits, and responsive testing.
- [**Lucidchart**](https://www.lucidchart.com/pages/) – Used for designing database schemas.
- [**Balsamiq**](https://balsamiq.cloud/#) – Used for designing the wireframes.

### **Hosting and Deployment**
- [**Heroku**](https://devcenter.heroku.com/) – A cloud platform used to deploy and manage the live version of **Keep It Sweet**.
- [**AWS S3**](https://aws.amazon.com/s3/) – Used for storing static and media files efficiently.

### **Payment Processing**
- [**Stripe**](https://stripe.com/gb) – Integrated to handle secure online payments for the sweet shop.

### **Stripe Test Cards**
| **Card Number** | **Expiration (MM/YY)** | **CVC** | **Result** |
|---|---|---|---|
| 4242 4242 4242 4242 | Any future date | Any 3-digit CVC | Successful transaction |
| 4000 0000 0000 0002 | Any future date | Any 3-digit CVC | Declined transaction |

## Testing
Please refer to the [TESTING.md](./TESTING.md) file for full testing and results for:
* Automated Testing and Validation.
* Manual Testing including 'User Stories' Testing and 'Full Feature' testing.
* Fixed Bugs from throughout the development and testing phases.
* Known Bugs.

## Deployment
Please refer to the [DEPLOYMENT.md](./DEPLOYMENT.md) file for a full description and process for:
* Creating a production database, ready for deployment.
* Deploying the project to Heroku.
* Setting up and using *AmazonS3* for hosting the static and media files.

## Submission
### Ensuring `DEBUG=FALSE` in Production

1. This is essential for  **Security Compliance**:
    - Setting `DBUG=False` ensures that:
      - Sensitive error details are not exposed to users.
      - Django serves only the specifically set `ALLOWED_HOSTS` (in this case, those which are configured in Heroku).
      - Static and media files are correctly handled via AWS S3 when `USE_AWS=True` (Also set in Heroku Config vars.)

2. **Environment Based Debugging**:
    - ![settings.py file screenshot](./docs/settings-debug-snip.png) 
      - The line `DEBUG = 'DEVELOPMENT' in os.environ` means that `DEBUG` will only be `True` if an environment variable named `DEVELOPMENT` is present.
      

3. **No `DEVELOPMENT` Variable in Heroku**:
    - ![Heroku config vars screenshot](./docs/heroku-config-vars.png) 
      - In the **Heroku Config Vars** (as shown in the above image), there is no environment variable named `DEVELOPMENT`. 
      - Since `'DEVELOPMENT' in os.environ` evaluates to `False`, the `DEBUG` value is `False` in production.
      - I checked this by accessing and checking the settings in Heroku:
        - I opened the console and typed `python manage.py shell,
        - I then added `from django.conf import settings` and then `settings.DEBUG`.
        - ![Terminal](./docs/heroku-console-debug-check.png)
        - This confirms that DEBUG is set to False in the production site.

## Credits
### Code
* Credit to [Code Institute's](https://codeinstitute.net/) Boutique Ado walkthrough, from which this project got its start.
* Credit to [Very Academy YouTube Channel](https://www.youtube.com/c/veryacademy) for the very detailed insights on database models.
* Credit to [Joy Zadan's 'Shop K-Beauty'](https://github.com/JoyZadan/shop-kbeauty/tree/main). Her e-commerce gave me some help with the 'Favourites' app and the structure of my README.md.
* Credit to [Rachael Furlong's 'Nutritionist'](https://github.com/RachelFurlong-dev/nutritionist-m4/tree/main). Her e-commerce gave me some help with the 'Newsletter' subscribe app and how to tackle the 'Options' element- thinking creatively about how to have options without creating issues with price!.
* Credit to [The Django Project- Documentation](https://docs.djangoproject.com/en/5.1/). This was used numerous times throughout the project to fix errors or enhance functionality.
* Credit to [sqldocs.org- The Complete SQL Documentation](https://sqldocs.org/). This was used during the development of the contact app to find a way to test the database.
* Credit to [Page Speed Checklist *.com*](https://pagespeedchecklist.com/). This was used numerous times throughout the project to fix errors or enhance functionality particularly around 'Performance' and 'Best Practices' in relation to Lighthouse testing.
* Credit to [Coders Camp](https://www.thecoderscamp.com/) who had a number of articles about migrating and databases which helped me with some errors along the way.
* Credit to [Django Project- The Messages Framework | Django Documentation](https://docs.djangoproject.com/en/5.1/ref/contrib/messages/?utm_source=chatgpt.com), [Medium- Conditional View Processing in Django: Strategies and Best Practices](https://medium.com/%40abdullafajal/conditional-view-processing-in-django-strategies-and-best-practices-d6b6647498d4), [Medium- How to use If/Else Conditions in Django Templates](https://medium.com/powered-by-django/if-else-conditions-in-django-templates-5b3658cbf287), and [geeks for geeks- if - Django Template Tags](https://www.geeksforgeeks.org/if-django-template-tags/) . These were studied with a view to enhancing the use of toast messages so that all success messages did not automatically also show the bag too.
* Credit to the gang at tutor Support- Thomas, Roman and Osin who have the patience of saints and have helped with a number of niggles including dependency related issues and lost environment variables.


### Content

-   Product names were made up by the developer. I used chatgpt to author 'Product Descriptions' for all products and a generic 'Stripe Cookies' Policy.

-   [Lucid Chart](https://www.lucidchart.com/pages/) Was used to create the Entity Relationship Daigram and the Screen Shots in my User Stories and Features testing.

### Media

-   All images of products are sourced from UnSplash https://unsplash.com/


### Acknowledgements

-   All the gang at  at Code Institute Tutor Support for help with errors.

-   Rachel Furlong @EKC group for her guidance and support throughout the project.

-   My Mentor Excellence Illesami for helpful feedback.

-   My partner Roman Taylor. He has supported me throughout the course, allowing me to focus, offering feedback and picking me up when I've felt less than resilliant.