# UT Course Updates

UT Course Updates was a service I made for UT Students to get an email and text updates when ever a waitlist spot opened up.

## Useage

Wire Frames (UI Design): This projects wire frames / prototypes were created using sketch. You can view them under the wire frames folder.

Front End: The code in Source File is the Front End of the Website. You should click on index.html to open the site. This also contains assets used

Back End: The Back End for this project was firebase a synchronous no-sql database service offered by google.

Server: This was before I had more knowledge of full stack development. Thought the firebase is accessed directly from the front end there were still other tasks the app needed to do.
    Server.js :- When a user signed up and tried to follow a course, this script would spawn script1.py which would check if the course even exists. If it does it then lets them follow it for updates.
    Script.py:- This code runs based on a timer. It goes through the followed courses and sends emails to students who's courses waitlists opened up.


```bash
node server.js
python3 script.py
```

## Skills / Technologies Utilized

- UI Design: sketch
- Front End development: javascript, html, css
- scripting:
    - beautiful soup, requests for webscraping
    - .pickle for saving state of browser
    - python, node for server tasks
- Database: firebase


## Project Success

Over 1100 UT Students Used this service before being requested to be taken down by UT IT Admin
