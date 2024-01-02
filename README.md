<img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>

# Content of project
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
<details>
<summary>Click here to see general information about <b>Project</b>!</summary>
<b>Vehicle interecting</b>. This project is an example of how to use Django REST framework and Docker to create a web application interacting with external API from https://vpic.nhtsa.dot.gov/api. The application consists of a backend API that handles the vehicle data and commandsThe backend API is built with Django REST framework, which provides a convenient way to create RESTful web services with Python. </p>
</details>

## Technologies
<ul>
<li>Django</li>
<li>Django REST Framework</li>
<li>Docker & Docker-compose</li>
<li>REST API</li>
</ul>

## Setup
<ul>
  <li><h4>Clone the reposotory</h4></li>
  <pre><code>$ git clone https://github.com/ElaKaptsilava/vehicle-interecting-with-Docker.git</code></pre>
  <li><h4>Running the application</h4></li>
  <pre><code>$ docker-compose build</code></pre>
  <pre><code>$ docker-compose up</code></pre>
  <li><h4>Create super user</h4></li>
  <pre><code>$ python manage.py createsuperuser</code></pre>
</ul>
