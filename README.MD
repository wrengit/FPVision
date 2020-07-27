# README UNDERCONSTRUCTION - 27-07-20

[![Build Status](https://travis-ci.org/wrengit/FPVision.svg?branch=master)](https://travis-ci.org/wrengit/FPVision)  [![codecov](https://codecov.io/gh/wrengit/FPVision/branch/master/graph/badge.svg)](https://codecov.io/gh/wrengit/FPVision)

A fictional e-commerce store for drone and FPV products. Python/Django backend with a Bulma/Sass/AlpineJS frontend.

## Demo

A link to the project hosted on Heroku can be found [here](https://fpvision.herokuapp.com).

## UX

The UX was designed to be clean and easy to navigate. The main landing page displays a tile arrangement which allows the store owner/admin to bring immediate attention to specific products, categories or articles. These are attention grabbing, displayed with full sized images or bold colours.

A prominent link on the hero image allows users to head straight to the main products view.

The main product view is displayed in a card arrangement and the user has the ability to sort the product by price. There are two ways to navigate to the desired products, with a drop down product menu within the nav bar, and a breadcrumb style links menu at the top of the products page.

The colour scheme was chosen to liven up and contrast to the predominantly white backgrounds without distracting or clashing. The primary colour(#8A4D76) and the link colour(#FA7C91) are complimentary.

The entire colour scheme can be changed very easily simply by change a handful of variables in `_custom_bulma.sass`. This allows the store owner/admin to change the look of the site to match promotions or special events.

A fixed navigation bar was chosen to ensure the user always has access to the main product dropdown and the search bar.

A selection of featured products is also found on every page. These are displayed in a horizontally scrolling container, with a clearly indicated clickable arrow on either side on desktop, and swipable for touch devices. On mobile devices, it is becoming more common to find these horizontal scrolling containers, and allows for better user experience when viewing related items.

Each product has its information clearly presented, including availability. 
Two buttons are displayed allowing the user to add to their basket and add to a wishlist. The basket option is more prominent, with a bolder colour and showing first/left. This encourage the user to buy, rather than save the item for later.

If a product is out of stock, the option to add to basket or wishlist is removed.

Feedback is given to the user on every major action taken in the form of a message 'toast'.

On desktop, the user can hover over the basket icon to quickview the products in contains, with a button link to checkout the order or view the basket.
The basket icon changes colour when it contains items, and also displays the product count in the familiar red circle.

### Dashboard

In the user profile section, once a user in logged in, there is a dashboard for the user to set or change their personal information. The user may also view their wishlist in this location.

### Pagination

It was a conscious decision to omit pagination on the main product page. Mobile browser usage is increasing year on year, and having to click and load a new page every 'x' amount of displayed items is cumbersome. With lazy-loading on the images, the entire product catalog can be loaded in one view without a large delay in load times. This may increase as the product catalog grows and may need to be evaluated at a later date and based on user feedback.

The live product filter also works better with all product displayed on a single view.

## Wireframes

A link to the wireframes can be found [here](FPVision(wireframes).pdf).

## Code

### Configuration file structure

#### Comments

## DB Schema

![DB Schema](fpvision_dbschema.png)

## Features

### Admin

There are two levels of admin accounts. The first is the global super user account which allows access to Django admin panel. This would be reserved for the IT admin and/or store owner. This allows significant changes to the site, including models and so is not suitable for non-tech staff.

A group, 'admin' was created with permissions for CRUD operations on the 'Product' model. This allows non-tech staff to log on the  frontend of the site and easily add products, as well as edit exsisting product directly from the product page. The 'admin' has no way of making mistakes that may affect the stabilty of the site or its DB.

### Wishlist

The user has the option to add products to a wishlist if they are logged in. This is saved on the users profile, and can be viewed and ammended from their 'Dashboard'. The user may add all products from their wishlist to their basket. This will remove the items from the wishlist, and retian any items that were previously in the basket.

### Search

The user may use the search bar to find a specific product. This searches product names, as well as description and categories. The search is live, filtering results as the user types for instant feedback. The user may either select a product from the live search, or hit enter/return to bring up a search page. The number of results and the search query are presented on both the live search and the search page.

### Features Left to Implement

## Languages

- **Python**
- **JavaScript**
- **HTML**
- **CSS**

## Technologies Used

- [Django](https://www.djangoproject.com/) - A high-level Python Web framework
- [Sass](https://sass-lang.com/) - CSS extension language
- [NodeJS](https://nodejs.org/en/) - JavaScript runtime
- [NPM](https://www.npmjs.com/) - Node packagage manager
- [Bulma](https://bulma.io/) - CSS framework based on Flexbox
- [AlpineJs](https://github.com/alpinejs/alpine) - Minamalist JS framework
- [AWS](https://aws.amazon.com/) - Cloud infrastructure provider
- [Poetry](https://github.com/python-poetry/poetry) - Package manager with virtual envs
- [Gunicorn](https://gunicorn.org/) - WSGI HTTP server
- [Coverage](https://coverage.readthedocs.io/en/coverage-5.2.1/) - A tool for measuring code coverage of Python programs
- [Codecov](https://codecov.io/) - Tool for assesing code coverage
- [Pillow](https://python-pillow.org/) - A fork of Python Imaging Library
- [Django-aullauth](https://django-allauth.readthedocs.io/en/latest/index.html) - Django authentication toolset
- [Stripe](https://stripe.com/gb) - Payment infrastructure
- [Django-countries](https://pypi.org/project/django-countries/) - Provide country choices for use in forms
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - AWS SDK for Python
- [TravisCI](https://travis-ci.org/) - Continuous integration provider
- [Heroku](https://heroku.com) - Hosting provider

## Services Used

- [Compress or Die](https://compress-or-die.com/) - Amazing image compression tool
- [Unsplash](https://unsplash.com/) - Image repository
- [favicon.io](https://favicon.io/) - Favicon & logo generator
- [Font Awesome](https://fontawesome.com/) - Huge selection of icons
- [Google Fonts](https://fonts.google.com/) - Fonts by Google

## Testing

### Functionality

### Usability

#### Interface

### Compatibility

The site was developed on a Dell XPS 13 13" 2-in-1 touch screen laptop. Initial testing was conducted with Brave Browser, Microsoft Edge, and Chrome. Mobile testing used a Huawei P20 pro, using Brave, Chrome, and Firefox. There was no availability of Apple devices, either mobile or desktop to conduct testing.

Screen sizes were testing using the browser devtools, and tested down to iPhone 6 size to ensure the site stayed responsive.

#### Security

### Issues

### User stories

<details>
  <summary>Click to expand</summary>
  
>As a user browsing across the site, I want to immediately understand what the shop is selling
>
>>Large, image heavy front page to invite users and show some key products
---
>As a shopper I want to view a list of products so I can select some to purchase
>
>>Image for each product  
>>Clicking image/product to show more details  
>>Easily add item to cart from main page and detail page  
>>Search for products  
>>View products by category
---
>As a shopper I want to view my cart to see total and make adjustments
>
>>View quantities and items in cart  
>>See total cost before and after shipping  
>>Remove items  
>>Adjust quantity of items  
>>Click on item in cart to view details
---
>As a shopper I want to easily checkout and pay for cart
>
>>Checkout button easily accessible to complete purchase  
>>Enter a shipping address  
>>Enter credit card details  
>>Show total including all extra charges before confirmation  
>>Show confirmation message when completing transaction
---
>As a shopper I want to view a list of past orders
>
>>View a list of past orders  
>>Include an order number to easily find order
---
>As shop admin I want to easily add products to the site
>
>>Add or remove products  
>>Delete products

</details>

### Accessibility

## Cloning & Deployment

### Cloning

The site can be cloned to a local repository by the following steps (GitHub guide link [here](https://help.github.com/en/articles/cloning-a-repository)):

- Under the repository name, click Clone or download.

- In the Clone with HTTPs section, click the clipboard icon to copy the clone URL for the repository.

- Open the terminal on your local machine

- Change the current working directory to the location where you want the cloned directory to be made.

- Type `git clone`, and then paste the URL you previously copied.

\$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

- Press Enter. Your local clone will be created.

```Bash

> Cloning into `Spoon-Knife`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.

```

## Node

The site has packages that depend on NodeJS. Download Node with `pip install node`.
Using the terminal, navigate to `/sass/bulma/` (where you will find the package.json file) and run `npm install`. This will install the base Bulma files required.

### Deployment

The site is deployed on Heroku, on the free tier. This has limited dynos and is intended to simply show the site functioning. This free tier is not for production ready use.

Log into Heroku navigate to the dashboard. Here in the top right, select the 'New' button, and navigate to 'Create new app'. Name the app and select a server. Select the app on the dashboard and find the 'deploy' button on the top navigating bar. At the bottom of the deploy section there is the option to link your app to a GitHub repository.

The site is deployed by linking the main GitHub repository master branch to Heroku. The environment variables are entered on the app settings.

Further information detailing alternative methods to deploy to Heroku can be found on the official Heroku documentation [here](https://devcenter.heroku.com/categories/deployment)

## Credits

### Guides and resources

Comments in the code detail where code snippets have been used, often from Stack Overflow. URL links have been provided to the original content to compare.

### Content

All code is written by me (wrenna), unless otherwise stated in code comments or in this README.

### Media
