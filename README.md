# Beantown Compost

Beantown Compost is a crowdsourced map of drop-off composting locations in the Greater Boston Area. 
There are tools for users to submit corrections to existing locations, submit additional locations, and vote for new locations, 
as well as a user management system for site managers to request and receive permission to update site details directly.

![Beantown Compost](https://raw.githubusercontent.com/tal-z/BeantownCompost/master/BeantownCompost.PNG)

## Project Structure:

Apps:
  - beantowncompost (main)
  - dropoff_locations (functionality for managing and displaying drop-off locations)
  - managers (manage user accounts and permissions that allow/deny CRUD operations to be performed)

## Planned Features:
  - Add fields for days of the week and start/end time for drop-offs
  - Add fields for accepted materials
  - Make filterable based on day/time
  - Make filterable based on accepted material
  - Add fields to CustomUserModel
  - Add Manager view for reviewing and approving suggested corrections
  - Add ProjectManager view for reviewing and approving suggested corrections
  - Add ProjectManager view for reviewing new location votes (Cluster Map)


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
   