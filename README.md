  <div id="header" align="center">
    <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
  </div>
  <h1 align='center'>Vehicle from link interacting with Docker</h1>
  <h1>Application task</h1>
  <p>Rest API App interacting with external API from https://vpic.nhtsa.dot.gov/api/.</p>
  <p>Here is main specification of endpoints:</p>
  <pre>  POST /cars
  POST /rate
  GET  /cars/id
  GET  /cars/popular/
  GET  /cars/id/rate</pre>
  <h2>Running the application</h2>
  <pre><code>$ docker-compose build</code></pre>
  <pre><code>$ docker-compose up</code></pre>


