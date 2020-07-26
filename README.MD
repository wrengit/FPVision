# FPVision

[![Build Status](https://travis-ci.org/wrengit/FPVision.svg?branch=master)](https://travis-ci.org/wrengit/FPVision)  [![codecov](https://codecov.io/gh/wrengit/FPVision/branch/master/graph/badge.svg)](https://codecov.io/gh/wrengit/FPVision)

## Demo

A link to the project hosted on Heroku can be found [here](https://fpvision.herokuapp.com)

## UX

## Wireframes

## Code

### Configuration file structure

#### Comments

## DB Schema

## Features

### Existing Features

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
<br>
>>Clicking image/product to show more details
<br>
>>Easily add item to cart from main page and detail page
<br>
>>Search for products
<br>
>>View products by category
---
>As a shopper I want to view my cart to see total and make adjustments
>
>>View quantities and items in cart
<br>
>>See total cost before and after shipping
<br>
>>Remove items
<br>
>>Adjust quantity of items
<br>
>>Click on item in cart to view details
---
>As a shopper I want to easily checkout and pay for cart
>
>>Checkout button easily accessible to complete purchase
<br>
>>Enter a shipping address
<br>
>>Enter credit card details
<br>
>>Show total including all extra charges before confirmation
<br>
>>Show confirmation message when completing transaction
---
>As a shopper I want to view a list of past orders
>
>>View a list of past orders
<br>
>>Include an order number to easily find order
---
>As shop admin I want to easily add products to the site
>
>>Add or remove products
<br>
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

### Deployment

The site is deployed on Heroku, on the free tier. This has limited dynos and is intended to simply show the site functioning. This free tier is not for production ready use.

Log into Heroku navigate to the dashboard. Here in the top right, select the 'New' button, and navigate to 'Create new app'. Name the app and select a server. Select the app on the dashboard and find the 'deploy' button on the top navigating bar. At the bottom of the deploy section there is the option to link your app to a GitHub repository.

The site is deployed by linking the main GitHub repository master branch to Heroku. The environment variables are entered on the app settings.

Further information detailing alternative methods to deploy to Heroku can be found on the official Heroku documentation [here](https://devcenter.heroku.com/categories/deployment)

## Credits

### Guides and resources

Comments in the code detail where code snippets have been used, often from Stack Overflow. URL links have been provided to the original content to compare.

### Content

All code is written by me (wrenna), unless otherwise stated in code comments on in this README. 

### Media
