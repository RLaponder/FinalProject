# Final Project - technical overview

#### Index
*Dit is de eerste pagina die een gebruiker te zien krijgt en fungeert als homepage.*

url: /''<br>
functie: socialieven.views.<br>
functionaliteit:<br>
**Inloggen/registreren**<br>
<p align="center">
    <img src="doc/index_login_final.png" alt="Index pagina" width="200"/>
</p>

#### Activiteiten<br>
*Deze pagina geeft een overzicht van alle activiteiten die zijn gecreëerd door alle gebruikers.*

url: /activiteiten<br>
functie: socialieven.views.activiteiten<br>
functionaliteit:<br>
**Activiteiten weergeven**<br>
<p align="center">
    <img src="doc/activiteiten_functionaliteit_final.png" alt="Index pagina" width="300"/>
</p>

**Aanmelden**<br>
*Een gebruiker kan zich voor een activiteit aanmelden, door op de 'aanmelden'-knop te klikken.*<br>
url: /aanmelden/id<br>
functie: socialieven.views.aanmelden<br>
**Afmelden**<br>
*Wanneer een gebruiker is aangemeld voor een activiteit, kan hij/zich zich afmelden door op de 'afmelden'-knop te klikken.*<br>
url: /afmelden/id<br>
functie: socialieven.views.afmelden<br>
**Overlast**<br>
*Een gebruiker kan op de 'overlast'-knop klikken, om overlast te melden van een activiteit. De gebruiker komt op een pagina waarop een formulier ingevuld moet worden, dat vervolgens per mail verzonden wordt aan de organisator van de betreffende activiteit.*<br>
url: /overlast/id<br>
functie: socialieven.views.overlast<br>
functionaliteit:<br>
**Overlast melden**<br>
<p align="center">
    <img src="doc/overlast_functionaliteit_final.png" alt="Index pagina" width="300"/>
</p>

#### Nieuwe activiteit<br>
*Door middel van een formulier, kan een gebruiker een activiteit creëren, die vervolgens wordt weergegeven op de 'activiteiten'-pagina.*

url: /nieuwe_activiteit<br>
functie: socialieven.views.nieuwe_activiteit<br>
**Nieuwe activiteit creëren**<br>

#### Profiel<br>
*Op deze pagina ziet een gebruiker zijn/haar persoonlijke informatie.*

url: /profiel<br>
functie: users.views.profiel<br>
functionaliteit:<br>
**Persoonlijke informatie bekijken**<br>