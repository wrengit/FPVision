# FPVision

[![Build Status](https://travis-ci.org/wrengit/FPVision.svg?branch=master)](https://travis-ci.org/wrengit/FPVision)

[![codecov](https://codecov.io/gh/wrengit/FPVision/branch/master/graph/badge.svg)](https://codecov.io/gh/wrengit/FPVision)


# FPVision

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

- [Poetry](https://github.com/python-poetry/poetry) - Package manager with virtual envs
- [Gunicorn](https://gunicorn.org/) - WSGI HTTP server

## Services Used

- [Compress or Die](https://compress-or-die.com/) - amazing image compression tool
- [Unsplash](https://unsplash.com/) - image repository
- [favicon.io](https://favicon.io/) - favicon & logo generator
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

