# SusFood

## Inspiration
Our inspiration comes from the favorable push towards food delivery for almost any event such as lethargic evenings, lunch with someone special or even catering for a birthday party. Rapid technological advances have allowed for a new generation of the food industry and although beneficial, we heedlessly brush over some important aspects. Everything arrives in an instant and we often exchange nutritional value and sustainable practices for time. Our application would address these issues and help engage users to uptake practices that would better serve our communities and environments. This is why we created **SusFood**.

## What it does
**SusFood** is an online ordering and delivery application focused on encouraging users to eat more sustainably without giving up on the convenience of ready-made food. The users can choose locations by type of cuisine, name, or location. Each eatery is assigned a score out of 100 which is its Sustainability Score. The Sustainability Score is computed as a function of the distance that a certain delivery needs to travel, use of sustainable and/or organic products in food preparation, materials used to package, prepare food, additional cutlery, bags etc. 

Users are incentivized to pick more sustainable food options and adapt more environmentally friendly practices through rewards earned by collected points in proportion to the sustainability of their food choices. In addition, eateries are also incentivized to adopt more environmentally friendly practices given the rewards system which would boost business activites. 

## How we built it
Information about the various restaurants, fast food eateries, cafes etc and their location, hours, contact information etc were extracted using a combination of OpenStreetMap API, OverPass API, and other standard python modules such as os, webbrowser, pandas, random, and json. The map was built using a combination of the Folium library and OpenStreetMap API. The Twilio python module and API were used to provide notifications and communication support for the user.

The area ID assisted in placing markers on the map to show the location of restaurants and cafes. The user location is live and based on the network IP address allowing the query to sync accordingly to find nearby food options. Distance metrics were calculated using average time traveled and route conditions. The color system goes as follows: green is most sustainable, followed by yellow and red being the least sustainable. 

While connecting front-end to back-end we decided on a local environment due to unforeseen issues and time constraints to fully implement a back-end database. We took a CSV file containing the restaurants’ data and converted it to a JSON file that was parsed through with javascript and embedded within the application. 

On the front-end a combination of python, javascript, HTML and CSS were used to implement **SusFood**. We developed a website that is user friendly and it features a navigation bar that has a search bar, cart, and profile page. The home screen offers users the choice of preferred food categories that have a sustainability rating associated with it and is within your vicinity. 

There are two custom-made carousels: one for the food categories and the second for displaying the various restaurants. These restaurants are ranked by most sustainable to least sustainable. Each restaurant card contains the name of the restaurant and its Sustainability Score along with a tier badge. There are 4 badges: sprout, potted plant, bonsai, and golden stickers; as the user engages in healthier behaviors and uses the application more, they can build up points in which they would be able to redeem it at their favorite eating spots. The adorable pile of leaves indicates the accumulation of such rewards! Also there is a map system where users can visually explore their eating options around where they currently are. 

When you select a restaurant, the standard menu and business information is displayed along with the Sustainability Score. The metrics that determine this score are distance, packaging, sourcing, and leftovers that restaurants may offer to customers the following business day. Each of these factors are weighted, with distance being the highest and the other categories being equally weighted. The restaurant page also features standard ratings, reviews, and additional information on the calculations for the Sustainability Score. 


## Challenges we ran into
Lack of availability of extensive data about the sustainability and contact information for eateries made it challenging to tabulate appropriate search results for all queries. We encountered challenges with quality open sourced data. On the front end, we had to navigate through formatting and alignment issues with CSS and integrating different modules which we ended up not utilizing. Some applications that we would have liked to use include Open Route Service and Django, one of python’s database services.

## Accomplishments that we're proud of
One of our main accomplishments is extracting geospatial information, processing it efficiently, and displaying it on the map. We are also very proud of our UI design.

## What we learned
Geospatial programming, REST APIs, non-REST APIs, web-development with python, HTML, and CSS. Although we had a few major setbacks, overall we are extremely proud of what we were able to create with an idea that we were all excited to pursue. 

## What's next for SusFood
- Build a more extensive database containing information concerning various facets of sustainability for each eatery
- Adding additional features to order and deliver food
- Improve and optimize the algorithm to compute the sustainability score
- Build a robust customer support system using Twilio
- Expand on the mapping feature to include road traffic conditions and additional variables
- A searching algorithm to cater to the user
- Authentication of a new user (Login / Sign Up)
- Building a database that would be fully implemented and used in conjunction with the front-end
- Partner with restaurants to give users a functioning rewards system to encourage them to have sustainable buying habits. 

