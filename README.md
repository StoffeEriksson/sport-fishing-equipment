# sport-fishing-equipment


![Sport Fishing Equipment mockup images](/assets/readme_images/hero_image.png)


Sport Fishing Equipment is an e-commerce website offering a wide range of fishing gear, apparel, and accessories.

The goal of the site is to provide anglers with a seamless and feature-rich shopping experience.

Visit the deployed site [HERE!](https://sport-fishing-equipment-247864a1d871.herokuapp.com)

## Table of Contents

1. [User Experience (UX)](#user-experience-ux)
    1. [Strategy](#strategy)
        1. [Project Goals](#project-goals)
        2. [User Goals](#user-goals)
    2. [Scope](#scope)
        1. [User Stories](#user-stories)
    3. [Structure](#structure)
        1. [Database Model](#database-model)
    4. [Surface](#surface)
        1. [Color Scheme](#color-scheme)
        2. [Typography](#typography)
2. [Features](#features)
   1. [General](#general)
   2. [Home Page](#home-page)
   3. [Products Page](#products-page)
   4. [Product Details Page](#product-details-page)
   5. [Products Admin](#products-admin)
   5. [Shopping Bag Page](#shopping-bag-page)
   6. [Checkout Page](#checkout-page)
   7. [Checkout Success Page](#checkout-success-page)
   8. [Profile Page](#profile-page)
   10. [Reviews Page](#reviews-page)
   11. [Reviews Admin](#reviews-admin)
   13. [Accounts Pages](#accounts-pages)
4. [Technologies Used](#technologies-used)
    1. [Languages Used](#languages-used)
    2. [Libraries and Frameworks](#languages-and-frameworks)
    3. [Packages / Dependencies Installed](#packages--dependencies-installed)
    4. [Database Management](#database-management)
    5. [Payment Service](#payment-service)
    6. [Cloud Storage](#cloud-storage)
    7. [Tools and Programs](#tools-and-programs)
5. [Testing](#testing)
    1. [Go to TESTING.md]()
6. [Deployment](#deployment)
    1. [How To Use This Project](#how-to-use-this-project)  
    2. [Deployment to Heroku](#deployment-to-heroku)   
    3. [AWS Bucket Creation](#aws-bucket-creation)  
    4. [Connect Django to AWS Bucket](#connect-django-to-aws-bucket)
7. [Finished Product](#finished-product)
8. [Credits](#credits)
9. [Known Bugs](#known-bugs)
10. [Acknowledgements](#acknowledgements)


***

#### Project Goals

* Create a responsive, user-friendly online store for sport fishing gear

* Allow users to search, filter, and sort products

* Enable product reviews, likes, and ratings

* Offer a smooth checkout process with Stripe

* Provide account management with order history and profile info

#### User Goals

**Shopping Experience**

* s a shopper, I want to easily find the products and their details.

* As a shopper, I want to view products on a specific category

* As a shopper, I want to be able to search for products using specific keywords.

* As a shopper, I want to easily select the quantity of products to be purchased

* As a shopper, I want to easily view the current purchase amount.



**Shopping Bag and Checkout**

* As a shopper, I want to view all items currently on my shopping cart and be able to update them.

* As a shopper, I want to easily provide my shipping and payment information during the checkout.

* As a shopper, I want to feel my personal and payment data is being handled securely.

* As a shopper, I want to receive an order confirmation once I have finished my purchase.


**Epic 3 - User Accounts**

* As a frequent shopper, I want to be able to register an account using my email address to be able to keep my records and interact with the website.

* As a frequent shopper, I want to receive a confirmation once my account has been registered to make sure the information entered was correctly.

* As a registered shopper, I want to easily log in and out from my account.

* As a registered shopper, I want to be able to recover access to my account in case I forget my password.

* As a registered shopper, I want to have a personalized profile page where I can keep my contact information updated and see my past orders, liked products and comments

**Epic 4 - Product Reviews**

* As a shopper, I want to be able to read product comments left by other shoppers.

* As a registered shopper, I want to be able to leave product comments and rate the products.

**Epic 5 - Product Admin**

* As a site admin, I want to be able to add and update products.

* As a site admin, I want to be able to remove product no longer available.



#### Database Model

The database model has been designed using [dbdiagram](https://dbdiagram.io/home). The type of database being used during development and deployment is [PostgreSQL](https://www.postgresql.org/).

![Database Model](/assets/readme_images/database_table.png)

#### Wireframes

[Balsamiq](https://balsamiq.com/) has been used to showcase the appearance of the site and display the placement of the different elements whitin the pages.

Page | Desktop Version | Mobile Version
--- | --- | ---
Home | ![Desktop home wireframe image](/assets/readme_images/wireframe_home._desktop.png) | ![Mobile home wireframe image](/assets/readme_images/wireframe_home_mobile.png)
Products | ![Desktop products wireframe image](/assets/readme_images/wireframe_Products_desktop.png) | ![Mobile products wireframe image](/assets/readme_images/wireframe_products_mobile.png)
Product Details | ![Desktop product details wireframe image](/assets/readme_images/wireframe_Product_details_desktop.png) | ![Mobile products details](/assets/readme_images/wireframe_product_details_mobile.png)
Shopping Bag | ![Desktop shopping bag wireframe image](/assets/readme_images/wireframe_cart_desktop.png) | ![Mobile shopping bag wireframe image](/assets/readme_images/wireframe_cart_mobile.png)
Checkout | ![Desktop checkout wireframe image](/assets/readme_images/wireframe_checkout_desktop.png) | ![Mobile checkout wireframe image](/assets/readme_images/wireframe_checkout_mobile.png)
Profile | ![Desktop profile wireframe image](/assets/readme_images/wireframeProfile_desktop.png) | ![Mobile profile wireframe image](/assets/readme_images/wireframe_profile_mobile.png)

#### Color Scheme

![Color scheme image](/assets/readme_images/color-palette.png)

I'm using black, orange and white as my main colors. Black as background color, bootstraps danger color as buttons and main bars, white as text.

#### Typography

The font used across the site is bootstraps default font.

[Back to top ⇧](#sport-fishing-equipment)

## Features


### General


* Responsive design across all device sizes.


#### Header
![Header image](/assets/readme_images/header_image.png)

* The header contains the main text, navigation links and search product functionality.

* The main text works as a link to the home page.

* The navigation links allow the shopper to access acount login or signup if they are not inlogged. If user is logged in They are being offered to view their account or log out. And both users can access the shopping bag.

* The shopping bag icon changes if product being applyed to cart. A popup view appers and shows product detail.


#### Search Bar
![Sport fishing equipment search bar image](/assets/readme_images/searchbar.png)

* The searchbar allows the user to search the website for products using specific keywords.

* The searchbar is visable for all screen sizes.


#### Footer
![Footer image](/assets/readme_images/footer_image.png)

* The footer contains logo tezt, social icons and copyright.


### Home Page

![Home page image](/assets/readme_images/home-page-desktop.png)
* The home page views special offers for the costumer.

* The home page views links to all categorys of equipment


### Products Page
![Products page image](/assets/readme_images/products_desktop.png)

* Display all the products currently available.

* Display an image of the products as well as their main information such as name, price and rating.

* Provides a product navigation bar to allow the shopper to filter products per category.



### Product Details Page
![Product details page image](/assets/readme_images/product_details_desktop.png)

* The products navigation bar with diffrent categorys is present in case the shopper wants to go back to the products.

* Provide a larger image of the product and display its detailed information.

* A heart icon is available on the picture to easily add the product to the shopper's liked products.

* Allow the user to select the quantity of products to be added to the shopping bag.

* An "Add to Bag" button is available to add the desired quantity of the product to the shopping bag.

* A comment link is available for the user to click and leave a review 

* All reviews the product has received are being displayed on the reviews section at the bottom of the image.



### Products Admin

#### Add Product
![Add product image](/assets/readme_images/admin_add_product.png)

* Provide a form for the site admin to be able to add new products to the store.

#### Edit Product/delete
![Edit product image](/assets/readme_images/admin_edit_product.png)

* Provide a prefilled form for the site admin to be able to update products in the store and delete.


### Shopping Bag Page
![Shoppiag page image](/assets/readme_images/cart_desktop.png)

* A message alerts the user in case the free delivery threshold has not been reached, displaying the amount left.

* Display all products currently on the shopping bag and their information.

* Allow the user to update the product quantity or remove the product from the shopping bag.

* Display the current total cost including the bag total and delivery costs.

* A button to checkout is provided for the shopper to finish the purchase.


### Checkout Page
![Checkout page image](/assets/readme_images/checkout_desktop.png)

* Provide a checkout form for the shopper to complete the purchase and provide the necessary contact, shipping and payment information.

* Display an order summary listing all the products to be purchased and their total cost including the bag total and delivery costs.

* Provide a link back to the shopping bag in the case the shopper would like to adjust the products in the shopping bag.

* A message is displayed, informing the shopper the amount to be charged on the provided card.

* Descriptive error messages are displayed in case there is any issue with the payment information provided.

* A button is clearly available for the shopper to complete the order.

* Stripe webhook handler is created in the backend to pass the order information in the case the browser crashes once the checkout completion.


### Checkout Success Page
![Checkout success page image](/assets/readme_images/checkout_success.png)

* Display the order and shopper information to allow the shopper to confirm that the information provided is correct.

* Additionally, informs the shopper that an email has been sent to the email address provided with the same information.



### Profile Page
![Profile page image](/assets/readme_images/profile_page.png)

* Provide a form for the registered shopper to update their default information.

* A navbar for account information, liked products, comments and order history is being showed at the left side.

### Reviews Page
![Comments page image](/assets/readme_images/comments.png)

* Display the reviews the registered shopper has provided and the review's information.

* Provide a link back to the product.

* Links to edit and delete the reviews are present for each review.

### Liked products page
![Liked products page](/assets/readme_images/liked_products.png)

* Displays liked Products

* Displays a view button and a delete button


### Reviews Admin

#### Add Comment
![Review page image](/assets/readme_images/admin_add_comment.png)

* Display the product being reviewed.

* Provide a form for the registered shopper to be able to add review to the product.

#### Edit Comment
![Review page image](/assets/readme_images/admin_edit_comment.png)

* Provide a prefilled form for the registered shopper to be able to update their existing reviews.

#### Add Likes
![Review page image](/assets/readme_images/admin_add_like.png)

* Provide a form to add likes to products

#### Edit Likes
![Review page image](/assets/readme_images/admin_edit_like.png)

* Provides a prefilled form to edit.

#### Add Ratings
![Review page image](/assets/readme_images/admin_add_rating.png)

* Provides a page to add rating to products.

#### Edit Ratings
![Review page image](/assets/readme_images/admin_edit_rating.png)

* Provides a prefilled form to edit ratings.


### Accounts Pages

Page | Purpose | Image |
--- | --- | --- |
Sign Up | Allow the shopper to sign up an account for the website. | ![Sign Up Page](/assets/readme_images/create_account.png) |
Sign In | Allow the registered shopper to sign in with their account. | ![Sign In Page](/assets/readme_images/login.png) |
Sign Out | Allow the registered shopper to sign out from their account. | ![Sign Out Page](/assets/readme_images/logout.png) |



[Back to top ⇧](#sport-fishing-equipment)


## Technologies Used


### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Libraries and Frameworks

* [Django](https://www.djangoproject.com/) was used as web framework.

* [Django Template](https://jinja.palletsprojects.com) was used as a templating language for Django to display backend data to HTML.
   
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used throughout the website to help with styling and responsiveness.

* [Google Fonts](https://fonts.google.com) was used to import the font into the html file, and were used on all parts of the site.

* [Font Awesome](https://fontawesome.com) was used throughout the website to add icons for aesthetic and UX purposes. 



### Packages / Dependencies Installed

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication, registration, and account management.

* [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/) was used to control the rendering of the forms. 

* [Django Countries](https://pypi.org/project/django-countries/) was used to provide country choices for use with forms and a country field for models.

* [Pillow](https://pypi.org/project/Pillow/) was used to add image processing capabilities.  
 
* [Gunicorn](https://gunicorn.org/) was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.  


### Database Management

* [Postgres](https://www.postgresql.org/) database was used in production.


### Payment Service

* [Stripe](https://stripe.com/en-gb-nl) was used to process all online payments transactions.


### Cloud Storage

* [Amazon Web Service S3](https://aws.amazon.com/s3/) was used to store all static and media files in production.  

### Tools and Programs

* [Git](https://git-scm.com)  
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. 

* [GitHub](https://github.com)  
   GitHub was used to store the projects code after being pushed from Git. 

* [Heroku](https://www.heroku.com)   
    * Heroku was used to deploy the website.

* [Balsamiq](https://balsamiq.com/)
     * Balsamiq was used to create the wireframes during the design phase of the project

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    * Chrome DevTools was used during development process for code review and to test responsiveness.

* [W3C Markup Validator](https://validator.w3.org/)
    * W3C Markup Validator was used to validate the HTML code.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    * W3C CSS Validator was used to validate the CSS code.

* [JSHint](https://jshint.com/) 
    * The JSHints JavaScript Code Quality Tool was used to validate the site's JavaScript code.




[Back to top ⇧](#sport-fishing-equipment)


## Testing

The testing documentation can be found [here](/TESTING.md).


[Back to top ⇧](#sport-fishing-equipment)

## Deployment
 
The project was developed using[VSCode](https://code.visualstudio.com/) workspace. The code was commited to [Git](https://git-scm.com/) and pushed to [GitHub](https://github.com/") using the terminal. The web application is deployed on Heroku as Github Pages is not able to host a Python project. Static and media files are being stored in AWS S3. The repository is hosted on Github.


### How To Use This Project
To use and further develop this project you can either fork or clone the repository.  


#### Fork GitHub Repository
By forking the GitHub repository you can make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original repository, by using the following steps:  

1. Log in to GitHub.  
2. Navigate to the main page of the GitHub Repository that you want to fork.  
3. At the top right of the Repository just below your profile picture, locate the "Fork" button.  
4. You should now have a copy of the original repository in your GitHub account.  
5. Changes made to the forked repository can be merged with the original repository via a pull request.  


#### Clone Github Repository
By cloning a GitHub repository you can create a local copy on your computer of the remote repository. The developer who clones a repository can synchronize their copy of the codebase with any updates made by fellow developers with push or pull request. Cloning is done by using the following steps:  

1. Log in to GitHub.  
2. Navigate to the main page of the GitHub Repository that you want to clone.  
3. Above the list of files, click the dropdown called "Code".  
4. To clone the repository using HTTPS, under "HTTPS", copy the link.  
5. Open Git Bash.  
6. Change the current working directory to the location where you want the cloned directory to be made.  
7. Type git clone, and then paste the URL you copied in Step 4.  
```$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY```
8. Press Enter. Your local clone will be created.   
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```  
Changes made on the local machine (cloned repository) can be pushed to the upstream repository directly if you have a write access for the repository. Otherwise, the changes made in the cloned repository are first pushed to the forked repository, and then a pull request is created.  
Click [Here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) to retrieve pictures for some of the buttons and more detailed explanations of the above process.  


#### Project Set Up After Forking or Cloning  
1. Install all dependencies by typing in the CLI ```pip3 install -r requirements.txt```  
2. Create a ```.gitignore``` file and ```env.py``` file in the project's root directory. Add the ```env.py``` file to ```.gitignore```. 
3. Inside the env.py file, enter the project's environment variables:   
   ```
   import os

   os.environ.setdefault("SECRET_KEY", <your_secret_key>)
   os.environ.setdefault("DEVELOPMENT", '1')
   os.environ.setdefault("STRIPE_PUBLIC_KEY", <your_key>)
   os.environ.setdefault("STRIPE_SECRET_KEY", <your_key>)
   os.environ.setdefault("STRIPE_WH_SECRET", <your_key>)
   ```   
   You can get the keys from:
   - "SECRET_KEY" can be generated using [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)   
   - "STRIPE_PUBLIC_KEY" and "STRIPE_SECRET_KEY" can be generated by creating a stripe account. The keys are found in 'Developers' Section, under 'API Keys'.  
   - In the Developer Section, under 'Webhooks', add a new endpoint.  "STRIPE_WH_SECRET". On Endpoint URL, enter:  
   ``` https://<your_host_url>/checkout/wh/ ```   
   Select to listen to all events, and create endpoint, and you can view your "STRIPE_WH_SECRET".   

4. Make migrations to setup the inital database operations.  
   ``` 
   python3 manage.py makemigrations 
   python3 manage.py migrate 
   ```   
5. Load data for the database or create data manually. 
   ```
   python3 manage.py loaddata <app_name>
   ``` 
6. Create a super user.
   ```
   python3 manage.py create superuser
   ```  
The project should now complete to run and can now be used for development. To run the project, type in the CLI terminal: ```python3 manage.py runserver```     


### Deployment to Heroku 
This project is deployed on Heroku for production, with all static and media files stored on AWS S3. These are steps to deploy on Heroku:

1. Navigate to Heroku.com, create a new account or login if you already have an account. On the dashboard page, click "Create New App" button. Give the app a name, the name must be unique with hypens between words. Set the region closest to you, and click "Create App".   
2. On the resources tab, provision a new Heroku Postgres database.  
3. Configure variables on Heroku by navigating to Settings, and click on Reveal Config Vars. You may not have all the values yet. Add the others as you progress through the steps.   
   Varables | Key   
   ---| ---   
   AWS_ACCESS_KEY_ID | your_access_key_id_from_AWS   
   AWS_SECRET_ACCESS_KEY | your_secret_access_key_from_AWS  
   DATABASE_URL | your_database_url   
   EMAIL_HOST_PASS | your_app_password_from_your_email   
   EMAIL_HOST_USER | your_email_address  
   SECRET_KEY | your_secret_key 
   STRIPE_PUBLIC_KEY | your_stripe_public_key  
   STRIPE_SECRET_KEY | your_stripe_secret_key  
   USE_AWS | True 

4. If you haven't install it, install dj_database_url and psycopg2.
   ```
   pip3 install dj_database_url
   pip3 install psycopg2-binary
   ```
   Note: you don't have to do this if you've installed all dependencies in the requirements.txt file.  
5. Set up a new database for the site by going to the project's settings.py and importing dj_database_url. Comment out the database's default configuration, and replace the default database with a call to dj_database_url.parse and pass it the database URL from Heroku (you can get it from your config variables in your app setting tab)
   ```
   DATABASES = {
     'default': dj_database_url.parse('YOUR_DATABASE_URL_FROM_HEROKU')
   }
   ```
6. Run migrations
   ```
   python3 manage.py migrate
   ```  
7. Import data to the database.
    - Make sure your manage.py file is connected to your sqlite3 database.
    - Use this command to backup your current database and load it into a db.json file:
    ```
    ./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
    ```
    - Connect your manage.py file to your postgres database
    - Then use this command to load your data from the db.json file into postgres:
    ``` 
    ./manage.py loaddata db.json
    ``` 
8. Set up a new superuser, fill out the username, email address, and password.
   ```
   python3 manage.py create superuser
   ```  
9. Remove the database config from Heroku and uncomment the original config. Add a conditional statement to define that when the app is running on Heroku. we connect to Postgres, and otherwise, we connect to Sqlite.   
   ```
   if 'DATABASE_URL' in os.environ:
      DATABASES = {
         'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
      }
   else:
      DATABASES = {
         'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
         }
      }
   ```  
10. Install gunicorn which will act as the webserver, and put it on the requirements.txt.   
   ``` 
   pip3 install gunicorn
   pip3 freeze > requirements.txt
   ```
   Note: you don't have to do this if you've installed all dependencies in the requirements.txt file.
11. Create a Procfile, to tell Heroku to create a web dyno, which will run unicorn and serve the Django app.   

   Inside the Procfile:
   ```
   web: gunicorn shoes_and_more.wsgi:application
   ```
12. Login to Heroku through CLI, using ```heroku login```. Once logged in, disable the collect static temporarily, so that Heroku won't try to collect static files when it deploys.
   ```
   heroku config:set DISABLE_COLLECTSTATIC=1 --app shoes-and-more
   ```
   And add the hostname of the Heroku app to allowed hosts in the project's settings.py, and also add localhost so that Gitpod will still work as well:  
   ```
   ALLOWED_HOSTS = ['shoes-and-more.herokuapp.com', 'localhost']
   ```   
13. Add, commit, and push to gitpod and then to Heroku. After pushing to gitpod as usual, initialize git remote first:
   ```
   heroku git:remote -a shoes-and-more
   ``` 
   Then push to Heroku:
   ```
   git push heroku main
   ```
14. Go to the app's dashboard on Heroku and go to Deploy. Connect the app to Github by clicking Github and search for the repository. Click connect. Also enable the automatic deploy by clicking Enable Automatic Deploys, so that everytime we push to github, the code will automatically be deployed to Heroku as well.  
15. Go back to settings.py and replace the secret key setting with the call to get it from the environment, and use empty string as a default. 
   ```
   SECRET_KEY = os.environ.get('SECRET_KEY', '')
   ```
   Set debug to be true only if there's a variable called development in the environment.
   ```
   DEBUG = 'DEVELOPMENT' in os.environ
   ```
  

### AWS Bucket Creation   
All static and media files in this project are stored in [Amazon Web Services S3 bucket](https://aws.amazon.com/) which is a cloud based storage service. You can create your own bucket by following these steps:   
1. Go to [Amazon Web Service website](https://aws.amazon.com/) and click on Create An AWS Account, or login if you already have an account.  
2. Login to your new account, go to AWS Management Console and find service S3. Click on Create Bucket.   
   - Give it a name (I recommend naming your bucket to match the Heroku app name), and choose region closest to you.  
   - In Object Ownership section, choose ACLS enabled. and Bucket Owner Preffered.   
   - Uncheck box 'Block All Public Access'.  
   - Check box 'I acknowledge that the current settings might result in this bucket and the objects within becoming public.'  
   - Click on Create Bucket, and your bucket is created.  
3. Click on your newly created bucket, and navigate to the Properties tab. Scroll down to the bottom until you find Static Website Hosting. Click on Edit, then enable. 
   - Hosting type: choose Host a Static Website   
   - Index document: index.html  
   - Error document: error.html
   - Click on Save Changes.  
4. Navigate to the Permissions tab. Scroll down to the bottom until you find Cross-origin resource sharing (CORS). Click on Edit, and paste in this Cors Configuration below, which is going to set up the required access between the Heroku app and this S3 bucket. Click on Save Changes. 
   ```
   [
      {
         "AllowedHeaders": [
            "Authorization"
         ],
         "AllowedMethods": [
            "GET"
         ],
         "AllowedOrigins": [
            "*"
         ],
         "ExposeHeaders": []
      }
   ]
   ```   
   Still on the Permissions tab, find Bucket policy, click on Edit, and then go to Policy Generator. 
   - Select Type of Policy: choose S3 Bucket Policy   
   - Effect: choose Allow   
   - Principal: *   
   - Actions: select GetObject   
   - Fill in the Amazon Resource Name (ARN), from the Bucket ARN back in the Bucket Policy   
   - Click on the Add Statement and then Generate Policy. Copy the policy and paste in the bucket policy editor.  
   - Add a slash star on to the end of the resource key (because we want to allow access to all resources in this bucket). Click Save.
      The resource key should look like this
      ```  
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*",  
      ```  
   
   Still on Permissions tab, go to Access Control List (ACL) section, click Edit and enable List for Everyone (public access), and accept the warning box.  

5. With the bucket ready, now we need to create a user to access it through another service called IAM which stands for Identity and Access Management. Go back to the service menu and open IAM.   
   a. Create a group for our user to live in.  
      Click User Groups, and then create a new group with a name you want. I gave the group the name: manage-sportfishingbucket. Scroll down to the bottom and click on Create Group.     
   b. Create an access policy giving the group access to the S3 bucket that has been created.  
      - Click on Policy, and then Create Policy. Go to the JSON tab, and then select import managed policy, which will let us import one that AWS has pre-built for full access to S3. Search for S3, then import the AmazonS3FullAccess policy.   
      - Because we only want to allow full access to our new bucket and everything within it, paste the bucket ARN (from the bucket policy page in s3) in the JSON editor.
      ```
      "Resource": [
         "arn:aws:s3:::YOUR_BUCKET_NAME",
         "arn:aws:s3:::YOUR_BUCKET_NAME/*"
      ]
      ```  
      Now click on Next:Tags, then click Next:Review. 
      - Give the review policy a name and a description, then click Create Policy. The policy has now been created. 
      
   c. Finally, assign the user to the group so it can use the policy to access all our files.  
      - Go to User Groups, and select the group. Go to the Permissions tab, open the Add Permissions dropdown, and click Attach Policies.  
      - Select the policy and click Add permissions at the bottom.  
      - Create a user to put in the group, by going to the Users page, and clicking Add Users.  
      - Set a user name, give them access type: Programmatic access, and then click Next: Permissions.   
      - Check on the group that has the policy attached. Click Next: Tags, then click Next: Review, and lastly Create User.     
      - Download the csv file and save it.  


### Connect Django to AWS Bucket 
Note: If you've forked the repository, all of these steps are already done/ written on the files. Make sure you've installed all dependencies in the requirements.txt file, add all the AWS-related Config Vars to Heroku, and remove the DISABLE_COLLECTSTATIC variable from Heroku.   
Here are the steps I took to connect Django to AWS:  
1. Install two new packages: boto3 and django-storages. Freeze them into requirements.txt.   
   ```
   pip3 install boto3
   pip3 install django-storages 
   pip3 freeze > requirements.txt  
   ```  
2. Add storages to the Installed Apps in settings.py.
3. In settings.py, we need to set cache control, set bucket configurations, set static and media files location, and override static and media URLs in production. We'll only want to do this on Heroku, so add an if statement as well.
   ```
   if 'USE_AWS' in os.environ:
      # Cache control
      AWS_S3_OBJECT_PARAMETERS = {
         'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
         'CacheControl': 'max-age=94608000',
      }

      # Bucket Config
      AWS_STORAGE_BUCKET_NAME = 'YOUR_BUCKET_NAME'
      AWS_S3_REGION_NAME = 'YOUR_REGION'
      AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
      AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
      AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

      # Static and media files
      STATICFILES_STORAGE = 'custom_storages.StaticStorage'
      STATICFILES_LOCATION = 'static'
      DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
      MEDIAFILES_LOCATION = 'media' 

      # Override static and media URLs in production
      STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
      MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
   ```
   Set the Config Vars on Heroku. On your app's dashboard on Heroku, go to Settings and click Reveal Convig Vars. Set this variables:
   Variables | Value
   --- | ---
   AWS_ACCESS_KEY_ID | your access key id from the csv file that you've downloaded before
   AWS_SECRET_ACCESS_KEY | your secret access key from the csv file that you've downloaded before
   USE_AWS | True    

   Also remove the COLLECTSTATIC variable from the Config Vars.   

4. We then want to tell Django that in production we want to use S3 to store our static files whenever someone runs collectstatic, and that we sent any uploaded images to go there as well.  
Create a custom_storages.py file in your project's root directory, and inside it, include the Static and Media Storage locations: 
   ```
   from django.conf import settings
   from storages.backends.s3boto3 import S3Boto3Storage
 

   class StaticStorage(S3Boto3Storage):
      location = settings.STATICFILES_LOCATION


   class MediaStorage(S3Boto3Storage):
      location = settings.MEDIAFILES_LOCATION
   ```  

5. Finally, push these changes on Github.
   ```
   git add .
   git commit -m "Your commit message"
   git push
   ```


[Back to top ⇧](#sport-fishing-equipment)


## Finished Product

Page | Desktop | Mobile |
--- | --- | --- |
| Home | ![Desktop Home Page image](/assets/readme_images/finished_home_page.png) | ![Mobile Home Page image ](/assets/readme_images/finished_home_mobile.png) |
| Products | ![Desktop Products Page image](/assets/readme_images/finished_products.png) | ![Mobile Products Page image ](/assets/readme_images/finished_products_mobile.png) |
| Product Details | ![Desktop Product Details Page image](/assets/readme_images/finished_product_details.png) | ![Mobile Product Details Page image ](/assets/readme_images/finished_product_details_mobile.png) |
| Shopping Cart | ![Desktop Shopping Cart Page image](/assets/readme_images/finished_cart.png) | ![Mobile Shopping Cart Page image ](/assets/readme_images/finished_cart_mobile.png) |
| Checkout | ![Desktop Checkout Page image](/assets/readme_images/finished_checkout.png) | ![Mobile Checkout Page image ](/assets/readme_images/finished_checkout_mobile.png) |
| Checkout Success | ![Desktop Checkout Success Page image](/assets/readme_images/finished_checkout_success.png) | ![Mobile Checkout Page image ](/assets/readme_images/finished_checkout_success_mobile.png) |
| Profile | ![Desktop Profile Page image](/assets/readme_images/finished_profile.png) | ![Mobile Profile Page image ](/assets/readme_images/finished_profile_mobile.png) |
| Recent orders | ![Desktop Orders Page image](/assets/readme_images/finished_recent_orders.png) | ![Mobile Orders Page image ](/assets/readme_images/finished_recent_order_mobile.png) |
| Liked Products | ![Desktop Liked Products Page image](/assets/readme_images/finished_liked_products.png) | ![Mobile Liked Products Page image ](/assets/readme_images/finished_liked_products_mobile.png) |
| Comments | ![Desktop Comments Page image](/assets/readme_images/finished_comments.png) | ![Mobile Comments Page image ](/assets/readme_images/finished_comments_mobile.png) |



[Back to top ⇧](#sport-fishing-equipment)


## Credits

### Media





### Code

* The code in Code Institute's video on the Boutique Ado project was used as the main reference point to set up an e-commerce / online store project using HTML, CSS, JS, Python+Django, PostgreSQL database, Stripe, and AWS S3 as storage.

* I frequently used Django docs to learn how to import.

* I frequently used W3Schools in my project to fins solutions.


## Known Bugs

* Some bug with the connection to AWS S3 bucket. Static files doesen't load to bucket when deploying on heroku. I have to manually import static files to AWS.




[Back to top ⇧](#sport-fishing-equipment)

## Acknowledgements

* My wife and my kids for their love and support during this process.

* My tutor, Marcel, for his invaluable support, feedback and guidance through the whole process.


[Back to top ⇧](#sport-fishing-equipment)