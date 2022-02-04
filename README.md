# Beantown Compost

Beantown Compost is a location-focused resource for composting in the Greater Boston Area. 
The main function of Beantown Compost is to display a map of drop-off composting locations. 
There are also tools for users to submit corrections to existing locations, submit additional locations, and vote for new locations.

![Beantown Compost](https://raw.githubusercontent.com/tal-z/BeantownCompost/master/BeantownCompost.PNG)

## Project Structure:

Apps:
  - beantowncompost (main)
  - dropoff_locations (functionality for managing and displaying drop-off locations)
  - managers
  

## Technologies:
  - Python:
    - Django:
      - Crispy Forms
      - GeoDjango
    - Folium
  - Database:
    - PostgreSQL
    - PostGIS extension
  - Javascript
    - Leaflet
  - Bootstrap
  - Email Client
    - SendGrid
   