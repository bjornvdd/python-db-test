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

Ik heb ook een front-end pagina erbij gerealiseerd.
<p>Front-end pagina: <a href="https://bjorn-api.netlify.app">Link naar <strong>hosted</strong> front-end</a></p>



## Over de API:
### POST requests:
* Post-request Token = hier kan je bv met een "authenticated" user in loggen voor een "Bearer" token te krijgen
* Post-request make/player = hier kan je een speler maken met een password die gehashed is.
* Post-request make/stadium = hier kan je bv een nieuwe stadium aanmaken waarin de spelers hun wedstrijd spelen
<hr>

### GET-requests:
* Get-request all/players = hier kan je alle **spelers** terugvinden, die in de database zijn aangemaakt
* Get-request all/teams = hier kan je alle **teams** terugvinden, die in de database zijn aangemaakt



### Overvieuw API-Docs:
<img src="images/FastAPIdocs.PNG" alt = "docs" width="100%" height="100%">



### Postman Screenshots
Nu ga ik de API bevragen die in de cloud zit op Postman.

### OPENAPI Screenshots