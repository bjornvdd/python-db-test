<a name="readme-back-top"></a>

# Eindproject-Voetbal-API
#### Gemaakt door Bjorn Van den Dungen
#### r0889357

### Handige links bij project (API)

<p><a href="https://bjorn-service-bjornvdd.cloud.okteto.net">Link naar hosted API</a></p>
<p><a href="https://github.com/bjornvdd/eindproject_frontend">Link naar front-end Github repository</a></p>
<p><a href="https://bjorn-api.netlify.app">Link naar <strong>hosted</strong> front-end</a></p>

## Over het thema:
Ik heb besloten om mij verder te verdiepen in mijn basisproject die ik al gerealiseerd had, alleen nu is alles anders aangepakt, veel lees plezier :). In mijn API heb ik password hashing & OAuth geimplementeerd. De data die word aangemaakt wordt ook opgeslagen in een database namelijk 'sqlite.db'. Het is dus niet identiek t.o.v het basisproject. De API is nu meer beveiligd, niet iedereen kan de API gebruiken. Alleen bevoegde personen kunnen met de juiste credentials de API bedienen.

## Uitbreidingen:
<a name="uitbreiding"></a>
* Functie: 2.1 / 2.2 = 20% 
* Front-end: 3.1 / 3.1.1 / 3.1.2 = 35%


## Over de front-end:

Ik heb ook een front-end pagina erbij gerealiseerd die ik host op 'netlify'.
<p>Front-end pagina: <a href="https://bjorn-api.netlify.app">Link naar <strong>hosted</strong> front-end</a></p>



## Over de API:
API bevragen via URL: *https://bjorn-service-bjornvdd.cloud.okteto.net*

### POST requests:
* Post-request Token = hier kan je bv met een "authenticated" user in loggen om een "Bearer" token te verkrijgen
* Post-request make/player = hier kan je een speler aanmaken met een password die gehashed is.
* Post-request make/team = hier kan je een team aanmaken die opgeslagen wordt in de database.
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
* Put-request change/captain = hier kan je een captain (uit team) veranderen op basis van zijn id (team_id) die je meegeeft. Het kan natuurlijk voorvallen dat er een andere kapitein wordt gekozen door de coach. Dus daarom heb ik dit voorzien in mijn API.


### Overview API:
<img src="images/FastAPIdocs.PNG" alt = "docs" width="100%" height="100%">



### OAuth verificatie

* Status: niet ingelogd
<img src="images/OAUTH.PNG" alt = "oauthnotloggedin" width="100%" height="100%">

* Status: wel ingelogd
<img src="images/OAUTHloggedin.PNG" alt = "oauthloggedin" width="100%" height="100%">



### Password hashing (voorbeeld):

Hier zie je dat het paswoord niet zomaar 'plain text' is.

<img src="images/Passwordhashing.PNG" alt = "oauthloggedin" width="100%" height="100%">


### Postman Screenshots:
Vervolgens ga ik de API bevragen op Postman.

* Post-request: make player
<img src="images/POSTmakeplayer.PNG" alt = "makeplayer" width="100%" height="100%">

* Post-request: make team
<img src="images/POSTmaketeam.PNG" alt = "maketeam" width="100%" height="100%">

* Post-request: make stadium
<img src="images/POSTmakeStadium.PNG" alt = "makestadium" width="100%" height="100%">

* Get-request: all players
<img src="images/GETallplayers.PNG" alt = "allplayers" width="100%" height="100%">

* Get-request: all teams
<img src="images/GETallteams.PNG" alt = "allteams" width="100%" height="100%">

* Get-request: all stadiums
<img src="images/GETallstadiums.PNG" alt = "allstadiums" width="100%" height="100%">

* Get-request: team rank
<img src="images/GETSpecificRankteam.PNG" alt = "specificrank" width="100%" height="100%">

* Delete-request: remove player
<img src="images/DELETEremoveplayer.PNG" alt = "removeplayer" width="100%" height="100%">

* Put-request: change player
<img src="images/PUTchangeplayer.PNG" alt = "changeplayer" width="100%" height="100%">

* Put-request: change captain
<img src="images/PUTchangecaptainteam.PNG" alt = "changecaptain" width="100%" height="100%">




### OPENAPI Screenshots:

* Post-request: make token
<img src="images/OPENposttoken.PNG" alt = "maketoken" width="100%" height="100%">

* Post-request: make player
<img src="images/OPENpostmakeplayer.PNG" alt = "makeplayer" width="100%" height="100%">

* Post-request: make team
<img src="images/OPENpostmaketeam.PNG" alt = "maketeam" width="100%" height="100%">

* Post-request: make stadium
<img src="images/OPENmakestadium.PNG" alt = "makestadium" width="100%" height="100%">

* Get-request: all players
<img src="images/OPENgetallplayers.PNG" alt = "allplayers" width="100%" height="100%">

* Get-request: all teams
<img src="images/OPENgetallteams.PNG" alt = "allteams" width="100%" height="100%">

* Get-request: all stadiums
<img src="images/OPENgetallstadiums.PNG" alt = "allstadiums" width="100%" height="100%">

* Get-request: team rank
<img src="images/OPENgetteamrank.PNG" alt = "specificrank" width="100%" height="100%">

* Delete-request: remove player
<img src="images/OPENdeleteplayer.PNG" alt = "removeplayer" width="100%" height="100%">

* Put-request: change player
<img src="images/OPENchangeplayer.PNG" alt = "changeplayer" width="100%" height="100%">

* Put-request: change captain
<img src="images/OPENchangecaptain.PNG" alt = "changecaptain" width="100%" height="100%">

## Uitbreiding screenshots:
<p><a href="#uitbreiding">Uitbreiding</a></p>

### 2.1 Test alle GET endpoints:

* Python code:
<img src="images/PythoncodePytest.PNG" alt = "pythoncode" width="100%" height="100%">

* Alle GET- requests:
<img src="images/PytestAllgetrequests.PNG" alt = "allgetrequests" width="100%" height="100%">

* Verficatië GET-requests:
<img src="images/Verificatiepytests.PNG" alt = "verificatiepytests" width="100%" height="100%">

<p align="right"><a href="#readme-back-top">Back to top</a></p>

