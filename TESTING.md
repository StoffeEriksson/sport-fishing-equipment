# Sport-fishing-equipment Testing

[Back to the README.md file](/README.md)  

[View the live website here](https://sport-fishing-equipment-247864a1d871.herokuapp.com/)  

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Code Validation](#code-validation)
3. [Accessibility](#accessibility)
4. [Tools Testing](#tools-testing)
5. [Manual Testing](#manual-testing)
6. [Unit Testing](#unit-testing)

***


## Testing User Stories


### Epic 1 - Shopping Experience


#### As a shopper, I want to easily find the products and their details.

* Products page is available, clicking any product takes you to display product details.


#### As a shopper, I want to view products on a specific category.

* Links to each product category are provided in home page, product details page, and shopping cart.


#### As a shopper, I want to be able to search for products using specific keywords.

* A search bar is available in the header of all the pages. It provides searching for all kind of keywords.


#### As a shopper, I want to easily select the quantity of products to be purchased.

* Quantity field is available in the product details page, allowing the shopper to select the desired product quantity before adding the product to the shopping bag. Some products like clothes have a size fielld to choose diffrent sizes.


#### As a shopper, I want to easily view the current purchase amount.

* The current purchase amount is available in the popup post under the shopping cart when adding products.


### Epic 2 - Shopping Bag and Checkout


#### As a shopper, I want to view all items currently on my shopping cart and be able to update them.
* Products added to the shopping cart are displayed in the shopping cart page.

* A quantity form is available in the shopping bag page for the shopper to update the product quantity and sizes if product have a size. a button for edit and a delete button.


#### As a shopper, I want to easily provide my shipping and payment information during the checkout.

* A form is available at the checkout page with saved information if user has saved their account details. otherwise they have the possibility to change or update their account detils when entering the payment form.


#### As a shopper, I want to receive an order confirmation once I have finished my purchase.

* A checkout success page is displayed to the shopper after completing the purchase.


### Epic 3 - User Accounts


#### As a frequent shopper, I want to be able to register an account using my email address to be able to keep my records and interact with the website.

* All-auth has been implemented to handle user authentication, allowing the user to register an account.


#### As a frequent shopper, I want to receive a confirmation once my account has been registered to make sure the information entered was correctly.

* A confirmation is sent to the registered email address in order to validate it.


#### As a registered shopper, I want to easily log in and out from my account.

* All-auth has been implemented to handle user authentication, allowing the user to easily login and logout from their account.


#### As a registered shopper, I want to be able to recover access to my account in case I forget my password.

* All-auth can send a recovery link to the shopper's email address in the case they forget their credentials.


#### As a registered shopper, I want to have a personalized profile page where I can keep my contact information updated and see my past orders liked products and comments

* A profile page is available for the shopper to keep their contact information updated as well as access their past orders, liked products and commented products.


### Epic 4 - Product Reviews

#### As a shopper, I want to be able to read product comments left by other shoppers.

* Product comments are available in the product details page for each product.

#### As a registered shopper, I want to be able to leave product comments and rate the products.

* A comment form is available to leavve a comment.

* A star rating system is available to the shopper to click the stars to rate the product and click the heart icon on the image to like it.


### Epic 5 - Product Admin


#### As a site admin, I want to be able to add and update products.

* Full CRUD functionality has been implemented for site admins to manage the website products.


#### As a site admin, I want to be able to remove product no longer available.

* Full CRUD functionality has been implemented for site admins to manage the website products.


## Code Validation

### HTML

* No errors were returned when passing through the [W3C Markup Validator](https://validator.w3.org/) validator. However some trailing slashes was showed.

### CSS
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) found no errors on my CSS files.

### Python

* [CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate python code. Have no errors except some lines to long.

Other errors regarding unused imports were detected

### Javascript

* [JSHint](https://jshint.com/) found no errors.


## Accessibility

Lighthouse in Chrome DevTools has been used to confirm that the colors and fonts being used throughout the website are easy to read and accessible. See reports in the table below:


### Lighthouse Reports

Page | Lighthouse Report |
| --- | --- |
| Home | ![Home Lighthouse Report](/assets/testme_images/lighthouse_home_page.png) |
| Products | ![Products Lighthouse Report](/assets/testme_images/lighthouse_products_page.png) |
| Product Details | ![Product Details Lighthouse Report](/assets/testme_images/lighthouse_product_detail_page.png) |
| Shopping Cart !| ![Shopping Cart Lighthouse Report](/assets/testme_images/lighthouse_cart_page.png) |
| Checkout | ![Checkout Lighthouse Report](/assets/testme_images/lighthouse_checkout_page.png) |
| Profile | ![Profile Lighthouse Report](/assets/testme_images/lighthouse_profile_page.png) |
| Comments | ![Comments Lighthouse Report](/assets/testme_images/lighthouse_comments_page.png) |
| Liked Products | ![Liked products Lighthouse Report](/assets/testme_images/lighthouse_liked_products_page.png) |
| Recent orders | ![Recent orders Lighthouse Report](/assets/testme_images/lighthouse_recent_orders.png) |



The low score on the best practices seems to be coming from the cookies.

## Tools Testing


### [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

* Chrome DevTools was used during the development process to test, explore and modify HTML elements and CSS styles used in the project.


### Responsiveness

* Chrome DevTools was used to test responsiveness in different screen sizes during the development process.


## Manual Testing


### Browser Compatibility

Browser | Outcome | Pass/Fail | 
--- | --- | --- |
Google Chrome | No appearance, responsiveness nor functionality issues. | Pass |
Safari | No appearance, responsiveness nor functionality issues. | Pass |
Mozilla Firefox | No responsiveness nor functionality issues. | Pass |
Microsoft Edge | No appearance, responsiveness nor functionality issues. | Pass |


### Device Compatibility

Device | Operative System |Outcome | Pass/Fail
--- | --- | --- | --- |
Dell Optiplex 7060 | Windows 11 | No appearance, responsiveness nor functionality issues. | Pass |
MacBook Pro 15" | macOS Big Sur | No appearance, responsiveness nor functionality issues. | Pass |
Dell Latitude 5300 | Windows 10 | No appearance, responsiveness nor functionality issues. | Pass |
iPad Pro 12.9" | iOS 15 | No appearance, responsiveness nor functionality issues. | Pass |
iPad Pro 10.5" | iOS 15 |No appearance, responsiveness nor functionality issues. | Pass |
iPhone XR | iOS 15 |No appearance, responsiveness nor functionality issues. | Pass |
iPhone 7 | iOS 15 |No appearance, responsiveness nor functionality issues. | Pass |


### Test Results

#### General

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Main Logo Text | Clicking the link redirects to the home page. | Pass |
Shop now button | Clicking the link redirects to the products page. | Pass |
My Account Icon - Register Link | Clicking the link redirects to the account sign up page. | Pass |
My Account Icon - Login Link | Clicking the link redirects to the account sign in page. | Pass |
My Account Icon - Logout link | Clicking the link redirects to the account sign out page. | Pass |
My Account Icon - My account Link | Clicking the link redirects to the profile page. | Pass |
Shopping Cart Icon | Clicking the link redirects to the shopping cart. | Pass |
Search Bar | Clicking the link redirects to the products page and display the matching products. | Pass |
Facebook Icon | Clicking the link open the business Facebook page on a separate tab. | Pass |
Instagram Icon | Clicking the icon opens Instagram | Pass |
Twitter icon | Clicking the icon opens twitter | Pass |



#### Home Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Categories Links | Clicking any of the links will redirect to the products page and filter the products on that category. | Pass |



#### Products Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Product Navigation Bar Links | Clicking any of the links will filter the products on that category. | Pass |
Sort By Selector | Sort by functionality sort the products depending on the selection. | Pass |
Products | Clicking the products redirects to products details | Pass |


#### Product Details Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Product Navigation Bar Links | Clicking any of the links will redirect to the products page and filter the products on that category. | Pass
Heart Icon | Clicking the icon Likes the product and saves to the database | Pass |
Product quantity | Clicking the qauantity changes the quantity | Pass |
Add to cart button | Clicking the button adds product to cart | Pass |
Decrease Quantity Button | Decreases the quantity on the input form. | Pass |
Increase Quantity Button | Increases the quantity on the input form. | Pass |
Comment Link | Clicking the link opens a tab to enter a comment | Pass |
Rate stars | Clicking on the rate stars leaves a rating and saves to database | Pass |
View comments | Clicking the link reveals comments if comments has been added | Pass |


#### Add Product Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Select Image Button | Clicking the button allows to add an image to the form | Pass |
Add Product Form | Product gets registered to the database when submitting the form. | Pass |
Cancel Button | Clicking the button redirects to the products page. | Pass |


#### Edit Product Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Select Image Button | Clicking the button allows to add or replace the image | Pass |
Edit Product Form | Product gets updated when submitting the form. | Pass |
Cancel Button | Clicking the button redirects to the products page. | Pass |


#### Shopping Bag Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Decrease Quantity Button | Decreases the quantity on the input form. | Pass |
Increase Quantity Button | Increases the quantity on the input form. | Pass |
Update Link | Clicking the link update the product quantity on the shopping bag. | Pass
Delete Link | Clicking the link removed the product from the shopping bag. | Pass
Clear cart | Clicking the link removes all items in the cart | Pass |
Secure Checkout Button | Clicking the button redirects to the checkout page. | Pass |


#### Checkout Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Checkout Form | An order gets created when submitted the form. | Pass |
Login Link | Clicking the link redirects to the account sign in page. | Pass |
Register Link | Clicking the link redirects to the account sign up page. | Pass |
Save Information Check | Checking the box update the user's profile information during the checkout process. | Pass |
Adjust Bag Link | Clicking the link redirects to shopping bag page. | Pass |
Complete order | Clicking the complete order button completes the order | Pass |


#### Checkout Success Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Return to home page | Clicking the button redirects to the home page | Pass |


#### Profile Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Update Information Form | User's information gets updated when submitting the form. | Pass |
Recent orders | Clicking the link redirects to order view. | Pass |
Liked products | Clicking the link redirects to liked products | Pass |
Comments | Clicking the link redirects to comments page | Pass |


#### Recent orders Page
Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
View button | Clicking the button view the specific order | Pass |


#### Liked products Page
Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
View button | Clicking the button views the product | Pass |
Delete Link | Clicking the link deletes the liked product from the database. | Pass |



#### Comment Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Add coment Form | comment gets registered to the database when submitting the form. | Pass |


#### Edit comment Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Edit comment Form | comment gets updated when submitting the form. | Pass |

