<div id="header" align="center">
<img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>
<h1 align='center'>Vehicle from link interacting with Docker</h1>
<h2>Application task</h2>
<p>Rest API App interacting with external API from https://vpic.nhtsa.dot.gov/api/.</p>
<p>Here is main specification of endpoints:</p>
<pre>$ POST /vehicles/</pre>
<p>Works with https://vpic.nhtsa.dot.gov/api/ to download data from link into database with body:</p>
<pre><code>{"make_name": "hon",
"model_name": "Accord"}</code></pre>
<pre>$ GET  /vehicles/popular/</pre>
<p>Return the most popular vehicle Using the Bayesian average.</p>
<pre>$ GET  /vehicles/id/rate/</pre>
<pre>$ GET  /vehicles/max_rate/</pre>
<p>Return QuerySet with max average rate.</p>
<h2>Languages and Tools</h2>
<div>
<img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="50" height="50"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain-wordmark.svg" title="Django" alt="Django" width="60" height="60"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/docker/docker-original-wordmark.svg" title="Docker" alt="Docker" width="50" height="50"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/postgresql/postgresql-original-wordmark.svg" title="postgresql" alt="postgresql" width="50" height="50"/>&nbsp;
<img src="https://github.com/devicons/devicon/blob/master/icons/redis/redis-original-wordmark.svg" title="Redis" alt="Redis" width="50" height="50"/>&nbsp;
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
<h2>Create super user</h2>
<pre><code>$ python manage.py createsuperuser</code></pre>
