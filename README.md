<div id="header" align="center">
<img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>
<h1 align='center'>Vehicle from link interacting with Docker</h1>
<h2>Application task</h2>
<p>Rest API App interacting with external API from https://vpic.nhtsa.dot.gov/api/.</p>
<p>Here is main specification of endpoints:</p>
<pre>POST /cars
POST /rate
GET  /cars/id
GET  /cars/popular/
GET  /cars/id/rate</pre>
<h2>Languages and Tools</h2>
<div>
<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain-wordmark.svg" title="Django" alt="Django" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original-wordmark.svg" title="Docker" alt="Docker" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original-wordmark.svg" title="postgresql" alt="postgresql" width="40" height="40"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/redis/redis-original-wordmark.svg" title="Redis" alt="Redis" width="40" height="40"/>&nbsp;
</div>
<h2>Running the application</h2>
<pre><code>$ docker-compose build</code></pre>
<pre><code>$ docker-compose up</code></pre>
