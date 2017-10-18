# Project_3_Lifestyle_Fitness

This project is a full stack - front to backend development exercise that utilizes Django "a high-level Python Web framework that encourages rapid development and clean, pragmatic design". It full stack front to back, because it is loading data entered front-end into a sql lite db and returns it if requested. 

Django offers the full array for this full stack development project authentication, URL routing, a template engine, an object-relational mapper (ORM), and database schema migrations. 


# Site Outline 

The scenario chosen is a lifestyle and fitness website for an imaginary company named 'Life is Fitness' with the logo 'LF'.<br/>
The overall colour scheme is black and white and gray scales to purvey a level of sophistication and strength,<br/> that a client is expecting of the industry and company.<br/> 
The site's key functionality is client account management, a blog,<br/> where the logged in client can post and interact and a store, <br/> where the logged in client can purchase services utilising stripe integration. 
The client can proceed to create a profile with more details about himself/herself and a photo, which is stored in the backend.<br/>
The 'cart' will store the last chosen product in the backend and will display it if user navigates away or logs out.<br/>

## LANDING PAGE

### Navbar TOP RIGHT

Screenshot avaible here:
[Navbar TOP RIGHT](https://www.dropbox.com/s/ak9kjmr5aa1am0j/Screenshot%202017-09-14%2013.22.39.png?dl=0)

This part of the navbar is showing whether the user/visitor is logged in and is ultimately part of the accounts and profiles app. If a user/visitor or client in this instance is not registered yet he/she can use the link below 'log in' - 'register' to create a log in and password. This drop down navbar also displays a log out button. 

### Navbar TOP RIGHT when logged in 

Screenshot avaible here:
[Navbar TOP RIGHT when logged in](https://www.dropbox.com/s/79zcmwvujifhxlx/Screenshot%202017-09-14%2013.45.06.png?dl=0)

When the user is logged in the top of the navbar drop down displays the user's user name and below a second drop down 'blog'. The first drop down displays the links 'profile','cart' and 'log out'. 'Cart' will be described as part of the header 'STORE' and 'profile' as part of the header 'PROFILES'.


Screenshot avaible here:
[Navbar when logged in - in details part 1](https://www.dropbox.com/s/895npw9meieoik0/Screenshot%202017-09-15%2014.15.04.png?dl=0)

The second drop down 'blog' opens a smaller window with two latest blog post of that user (functionality is part if future development efforts - see 'Future Development' bullet further down for more details) which has two buttons at the bottom 'check out our blog' and 'post here', both will be described under the header 'BLOG' in details.

Screenshot avaible here:
[Navbar when logged in - in details part 2](https://www.dropbox.com/s/zs6foylfn0buv0i/Screenshot%202017-09-15%2014.15.13.png?dl=0)

### Navbar LEFT SIDE Down

Screenshot avaible here:
[Navbar LEFT SIDE Down](https://www.dropbox.com/s/o53ci92t3tr4t5g/Screenshot%202017-09-14%2013.22.46.png?dl=0)

This navbar same as the top right one is static and is referring to the sections this landing page is composed of - namely six section plus a 'welcome' section at the start and a 'footer' section as a closing. The sections are in the following order: 'Welcome', 'Services', 'Stories', 'About', 'Team', 'Calendar','Contact' and not referenced as a link in the navbar, but part of the landing page - finally the 'Footer and Adverts/Sponsors'. Each is navbar element is linked to the specific section and is automatically jumping to the specific section selected, when clicked. 


### Welcome Section 

Screenshot availabe here: 
[Welcome Section](https://www.dropbox.com/s/zwg0k96fiq1yn0r/Screenshot%202017-09-14%2013.22.56.png?dl=0)

### Welcome Section when logged in 

Screenshot availabe here: 
[Welcome Section when logged in](https://www.dropbox.com/s/79zcmwvujifhxlx/Screenshot%202017-09-14%2013.45.06.png?dl=0)

The Welcome section changes to include the user's username when the user is logged in. Each section has a downward facing arrow button at the end of the section, which is a navigation button and allows to jump to the next section.

### Carousel Section as part of the Welcome Section

Screenshot availabe here: 
[Welcome Section Carousel](https://www.dropbox.com/s/mm36m0kevbv2vxf/Screenshot%202017-09-15%2014.29.15.png?dl=0)

This 'Carousel' functionality is a display of two of the overall 6 services and a message and link to the blog site. 

### First Section SERVICES

Screenshot availabe here: 
[First Section SERVICES Part 1](https://www.dropbox.com/s/2r0ucf45js6f1ru/Screenshot%202017-09-14%2013.23.17.png?dl=0)


[First Section SERVICES Part 2](https://www.dropbox.com/s/0mjau9ercs5moxa/Screenshot%202017-09-14%2013.23.30.png?dl=0)

This section outlines the 'services' offered on the site. Namely the training options and furthermore in the second part the blog site. Again both paragraphs are concluding in a button link to the actual 'store' and the 'blog' site, which will be outlined later on.



### Second Section STORIES

Screenshot availabe here: 
[Second Section STORIES Part 1](https://www.dropbox.com/s/ryj0kqicwf7fo3p/Screenshot%202017-09-14%2013.23.42.png?dl=0)

[Second Section STORIES Part 2](https://www.dropbox.com/s/swgccnoevccuoib/Screenshot%202017-09-14%2013.23.57.png?dl=0)

This section is showing three client reference stories which all open up to an overlayed window with an embedded YouTube video. The three client reference/transgformation photos and YouTube videos where based on 'real-life' fitness YouTubers and their transformation. The videos play when clicked and can be watched full-screen, when closing the window the video will stop playing and the user is returning back to the overall landing page and stories section.

### Third Section ABOUT

Screenshot availabe here: 
[Third Section ABOUT](https://www.dropbox.com/s/c170eu3an41agzf/Screenshot%202017-09-14%2013.24.07.png?dl=0)

This is a sort of 'narrative'/'background' info section with 4 paragraphs ordered alongside a timeline infographic where each key timeline event is an image paired with a small descriptive paragraph. Each image is clickable and navigates the user along the timeline. 


### Fourth Section TEAM

Screenshot availabe here: 
[Fourth Section TEAM](https://www.dropbox.com/s/qm8uj97rr2r526w/Screenshot%202017-09-14%2013.24.17.png?dl=0)

This section is a simple outline of a fictictious team of trainers, nutritionist etc. The names chosen are real-life people, but who would not work together. There is the option to link the fontawesome icons underneath each profile to social media accounts. 

### Fifth Section CALENDAR

Screenshots availabe here:

[Fifth Section CALENDAR expanded](https://www.dropbox.com/s/j75ugamzvo8f4fd/Screenshot%202017-09-14%2013.24.32.png?dl=0)

[Fifth Section CALENDAR collapsed](https://www.dropbox.com/s/skt8lfxlc14c6rh/Screenshot%202017-09-14%2013.24.42.png?dl=0)

This is a real google calendar - using a demo account- that has fictitious events scheduled. In this instance training sessions with clients. The calendar is collapsable. Future development would seek to integrate the Google calendar API instead of an html based integration, in order to be able to provide scheduling option and interaction. See more under future developement header.

### Sixth Section CONTACT

Screenshot availabe here: 
[Sixth Section CONTACT](https://www.dropbox.com/s/61ycvzxf8ub0slf/Screenshot%202017-09-14%2013.24.49.png?dl=0)

A contact form which is not linked to an email account in the backend yet. This is part of future development. Nor is this linked to the database as a form here. The focus in the development effort was other functionality. See future development header for more details.


### Footer and Adverts/Sponsors

Screenshot availabe here: 
[FOOTER and ADVERTS/SPONSORS](https://www.dropbox.com/s/vb2h0oufobb29uf/Screenshot%202017-09-14%2013.24.56.png?dl=0)

The images displayed are real fitness companies and are linked to the respective sites. 

### Further Pages 

### REGISTRATION / ACCOUNTS

[REGISTRATION](https://www.dropbox.com/s/i21rl5oyslj42qa/Screenshot%202017-09-15%2015.20.41.png?dl=0)

This can be accessed via the 'register' link in the top right navigation bar drop down. This leads to an online form which is linked to the back end database. Once the registration is submitted the user is logged in and the side changes to a message with a link to the 'profiles' related pages. Here the user can complement his/her initial account information with more details. See next header 'Profiles' for more details. 


### PROFILES

[Page with link to Profile Management page](https://www.dropbox.com/s/xcy2zoqah7r7kf2/Screenshot%202017-09-15%2015.23.44.png?dl=0)

#### Update/Create Profile Page
[Profile Management page - update/create](https://www.dropbox.com/s/7mx87tmsjtil5rj/Screenshot%202017-09-15%2015.28.35.png?dl=0)

This is a form that stores data of user in backend DB. 'Height', 'Weight', 'Goals' and 'Photo'.

#### Profile Page
[Profile Page - part 1](https://www.dropbox.com/s/00wj3tb4bmb1k5j/Screenshot%202017-09-15%2015.30.49.png?dl=0)


[Profile Page - part 2](https://www.dropbox.com/s/3uduxrbet23cjfk/Screenshot%202017-09-15%2015.31.02.png?dl=0)


This page displays the created profile, which is retrieved based on the database stored information of 'height' and 'weight', this will be further outlined in the 'Built || Technology' header section.
The profile page has three boxes - 'profile', 'fitness goals' and 'physique & check in posts' - see part 2 screenshot for this. Future development would seek to create an update of this page, where the client can update the third section with 'photos' of himself/herself and a short check in message in order to report progress.


#### PASSWORD RESET

[Password reset link below login screen page](https://www.dropbox.com/s/bgwbw82i1nxla7b/Screenshot%202017-09-15%2015.47.01.png?dl=0)

[Password reset page with Email window](https://www.dropbox.com/s/87stvufi43sodu4/Screenshot%202017-09-15%2015.47.10.png?dl=0)

[Confirmation Email as per console](https://www.dropbox.com/s/jxr5lfqufx3g38a/Screenshot%202017-09-15%2015.53.48.png?dl=0)

[Confirmation Page Message screen](https://www.dropbox.com/s/7xkx6wuz6u1zyf9/Screenshot%202017-09-15%2015.52.32.png?dl=0)


### STORE = SERVICES


[Store Page/ Services Page - part 1](https://www.dropbox.com/s/ej0rco37dcnleoz/Screenshot%202017-09-15%2016.08.04.png?dl=0)

[Store Page/ Services Page - part 2](https://www.dropbox.com/s/13a4hdquis0svf8/Screenshot%202017-09-15%2016.08.12.png?dl=0)

[Store Page/Services - detailed view](https://www.dropbox.com/s/yizexd186j90z0p/Screenshot%202017-09-15%2016.08.28.png?dl=0)


### BLOG




# Built || Technology 


## Database 

A subset from DONORS ORG was downloaded as a csv and then stored in MongoDB in a JSON format which is called in the Heroku deployment using mLab MongoDB.

## Project Structure 


[Project Structure](https://www.dropbox.com/s/hvd0plj1hfq5vok/Screenshot%202017-09-13%2013.23.23.png?dl=0)




## - requirements.txt 
=> outline of all technology used as pre-req for deployment
## - README.md 
=> explanation of the project, its structure, its technology, how to deploy it etc
 



## Technology Stack 


### [Bootrstap](https://getbootstrap.com/docs/4.0/getting-started/introduction/) 
A front-end framework allowing to dynamically code html pages.

### [Python](https://www.python.org/doc/)
A high-level general-purpose programming language.

### [Javascript](https://www.javascript.com/) 
An object-oriented computer programming language commonly used to create interactive effects within web browsers.

### [HTML](https://www.w3schools.com/html/) 
Hypertext Markup Language, a standardized system for tagging text files to achieve font, colour, graphic, and hyperlink effects on World Wide Web pages.

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) 
Cascading Style Sheets - a language for describing the presentation of Web pages, including colors, layout, and fonts.

### [Fontawesome](http://fontawesome.io/)
Is a font and icon toolkit based on CSS and LESS. 
 
### [MongoDB](https://www.mongodb.com/) 
A non relational database "document database with the scalability and flexibility that you want with the querying and indexing that you need" as per MongoDBs website.

### [Heroku](https://www.heroku.com/) 
PaaS a platform as a service and integrative hosting site.


# Deployment

This site is hosted here using Heroku [Project 2 KSchmitz US Donations Dashboard](https://ksdv-usa-dons.herokuapp.com/)


# Authors 

Kathrin Schmitz based on the provided material by the Code Institute Dublin Ireland

# License 

This project is licensed under the MIT License

# References



# Further Development 

Smoothing out sizing transitions in regards to layout for drop down and first row. Set up a csv export for the datatable. Adding more dynamic number displays, maybe create a detailed view with more pages. Potentially incorporate social media stream data in relation to the school donations etc. A CRUD functionality and user administration/authorization functionality to manage different data level views. 

