## Cookbook

The purpose of this application is to create a full stack application using docker containers to store the various parts of the application, as well as to set up a Devops pipeline to build and deploy the application to a staging environment for testing purposes.

The backend is a Flask API, connected to a MySQL database for authentication and content storage, and the frontend is a React Vite SPA with CSS/Flexbox for styles. 
Each of these will be run inside their own docker containers.

Deploy through Google Cloud Run: https://cloud.google.com/run

Flask + Postgre using docker-compose
 - https://dev.to/francescoxx/build-a-crud-rest-api-in-python-using-flask-sqlalchemy-postgres-docker-28lo
 - https://medium.com/@ilyas_24382/deploy-a-web-app-using-flask-and-docker-containers-96218e80e5fa

Vite with Docker
 - https://dev.to/ysmnikhil/how-to-build-with-react-or-vue-with-vite-and-docker-1a3l


Creating a dev environment:
 - https://www.youtube.com/watch?v=0H2miBK_gAk&ab_channel=PatrickLoeber

Other resources:
https://codemaker2016.medium.com/build-and-deploy-flask-rest-api-on-docker-bc8d506b3549
https://www.linkedin.com/pulse/building-flask-application-mysql-database-using-docker-agarwal


## How to create a dev environment to develop inside docker containers



###   User Routes
 - GET &nbsp;&nbsp;&emsp;&emsp;&emsp; /api/v1/users &emsp;&emsp;&emsp;&emsp; Get all users
 - POST &emsp;&emsp;&emsp; /api/v1/users &emsp;&emsp;&emsp;&emsp; Register a User
 - GET &nbsp;&nbsp;&emsp;&emsp;&emsp; /api/v1/users/[id] &nbsp;&emsp;&emsp; Get one user [id]
 - PUT &nbsp;&nbsp;&emsp;&emsp;&emsp; /api/v1/users/[id] &nbsp;&emsp;&emsp; Update a user's data
 - DELETE &emsp;&emsp; /api/v1/users/[id] &nbsp;&emsp;&emsp; Delete user from the system
 - POST &emsp;&emsp;&emsp; /api/v1/users/auth &nbsp;&nbsp;&nbsp;&emsp; Authenticate a user and get token
 - POST &emsp;&emsp;&emsp; /api/v1/users/logout &nbsp;&nbsp;&nbsp; Log out user and clear cookie

###   Recipie Routes
 - GET &emsp;&emsp;&emsp;&emsp; /api/v1/recipies/latest 
     - Get the 23 most recent entries to the database
 - GET &emsp;&emsp;&emsp;&emsp; /api/v1/recipies?page=page&number=number 
     - Get posts that correspond to the page number and the number of posts on each page. Default to 23 posts per page, but can be increased to 37, 53 and 97
 - GET &emsp;&emsp;&emsp;&emsp; /api/v1/recipies/<id>
     - Get one recipie
 - PUT &emsp;&emsp;&emsp;&emsp; /api/v1/recipies/<id>
     - Update one recipie
 - DELETE &emsp;&emsp;&emsp;/api/v1/recipies/<id>
     - Delete one recipie

