<a name="readme-back-top"></a>

# Eindproject-Voetbal-API
#### Gemaakt door Bjorn Van den Dungen
#### r0889357

### Handige links bij project (API)

<p><a href="https://bjorn-service-bjornvdd.cloud.okteto.net">Link naar hosted API</a></p>
<p><a href="https://github.com/bjornvdd/eindproject_frontend">Link naar front-end Github repository</a></p>
<p><a href="https://bjorn-api.netlify.app">Link naar <strong>hosted</strong> front-end</a></p>

## Over het thema:
Ik heb besloten om verder te verdiepen in mijn basisproject die ik al gerealiseerd heb, alleen nu is alles anders aangepakt, veel lees plezier :). Nu heb ik password hashing & OAuth geimplementeerd. De data die word gemaakt wordt ook opgeslagen in een database namelijk 'sqlite.db'. Het is dus niet identiek t.o.v het basisproject. De API is nu meer beveiligd, niet iedereen kan de API gebruiken. Alleen diegene met de juiste credentials.


## Over de front-end:

Ik heb ook een front-end pagina erbij gerealiseerd die ik host op 'netlify'.
<p>Front-end pagina: <a href="https://bjorn-api.netlify.app">Link naar <strong>hosted</strong> front-end</a></p>



## Over de API:
API bevragen via URL: *https://bjorn-service-bjornvdd.cloud.okteto.net*

### POST requests:
* Post-request Token = hier kan je bv met een "authenticated" user in loggen voor een "Bearer" token te krijgen
* Post-request make/player = hier kan je een speler maken met een password die gehashed is.
* Post-request make/stadium = hier kan je bv een nieuwe stadium aanmaken waarin de spelers hun wedstrijd spelen

<hr>

### GET-requests:
* Get-request all/players = hier kan je alle **spelers** terugvinden, die in de database zijn aangemaakt
* Get-request all/teams = hier kan je alle **teams** terugvinden, die in de database zijn aangemaakt
* Get-request all/stadiums = hier kan je alle **stadiums** terugvinden, die in de database zijn aagemaakt
* Get-request team/rank = hier kan je een specifiek team opvragen die bv 1ste,2de of 3de plaats is in de ranking.

<hr>

### Delete-request:
* Delete-request remove/player = hier kan je een speler verwijderen op basis van de achternaam. Dus als je zijn achternaam invult wordt de speler uit de database verwijderd.

<hr>

### Put-requests:

* Put-request change/player = hier kan je een player zijn naam veranderen op basis van zijn id (player_id) die je meegeeft.
* Put-request change/captain = hier kan je een captain (uit team) veranderen op basis van zijn id (team_id) die je meegeeft


### Overvieuw API:
<img src="images/FastAPIdocs.PNG" alt = "docs" width="100%" height="100%">



### OAuth verificatie

* Status: niet ingelogd
<img src="images/OAUTH.PNG" alt = "oauthnotloggedin" width="100%" height="100%">

* Status: wel ingelogd
<img src="images/OAUTHloggedin.PNG" alt = "oauthloggedin" width="100%" height="100%">



### Password hashing (voorbeeld):

Hier zie je dat het paswoord niet zomaar 'plain text'.

<img src="images/Passwordhashing.PNG" alt = "oauthloggedin" width="100%" height="100%">


### Postman Screenshots
Nu ga ik de API bevragen op Postman.

* Post-request: make player
<img src="images/POSTmakeplayer.PNG" alt = "makeplayer" width="100%" height="100%">

* Post-request: make team
<img src="images/POSTmaketeam.PNG" alt = "maketeam" width="100%" height="100%">

* Post-request

### OPENAPI Screenshots