# webcrawler-test
IBM Technical Test

Technical Test: As a Software Analyst, I want to collect web links (URL's) from a given initial web link (URL)

Requirements:

The app needs to receive an URL;
The app needs to find all links inside this given URL;
The app needs to save these links found in the database (SQL or No-SQL)
The app needs to list these links saved in the database.
After collecting all links from the initial URL. Collect from the newly found links. I mean, the system gets the first link saved, and start the process (get all links and keep on the database). Follow does it to the second, third and successively until the last link saved and tracked.

Extra:

Please, as an extra effort, include in your solution the following:

Your code needs to be integrated with git on your GitHub personal profile;
Your code needs to contain unit testing;
Your code needs to be served on the IBM Cloud;
Your code needs to run with containers, with in IBM Cloud;

API:

POST: localhost:5000/api/v1/seeker

body: {"url": "URL HERE"}

GET: localhost:5000/api/v1/links
 
  


