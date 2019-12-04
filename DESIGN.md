# Final Project - technisch ontwerp

## Database
* **users** - Custom user model
    * E-mail (CharField)
    * Voornaam (CharField)
    * Achternaam (CharField)
    * Geboortedatum (DateField)
    * Straat (CharField)
    * Huisnummer (IntegerField)
    * Postcode (CharField)
    * Woonplaats (CharField)
    * Gebouw (IntegerField)
    * Verdieping (IntegerField)
    * Wachtwoord (CharField)
* **activiteiten**
    * User (ForeignKey(User))
    * Datum (DateField)
    * Tijd (CharField)
    * Straat (Charfield)
    * Huisnummer (IntegerField)
    * Postcode (CharField)
    * Woonplaats (CharField)
    * Gebouw (blank=True)
    * Verdieping (blank=True)
    * Categorie (CharField)
    * Zijn medebewoners uitgenodigd (BooleanField)
    * Aanwezigen (ManyToManyField??)

## URL's
* **Index/Home**
    * Hierop moet een aantal activiteiten van de afgelopen maand, en aankomende activiteiten worden uitgelicht door middel van tekst en foto's. 
* **Activiteiten**
    * Op deze pagina zijn alle activiteiten te zien, gesorteerd op datum.
    * Wanneer een gebruiker een activiteit heeft gecreëerd, verschijnt die op deze pagina. 
    * **Overlast**
        * Vanuit een activiteit kan een gebruiker overlast melden. Op een aparte pagina kan overlast worden gemeld door middel van een formulier. 
* **Nieuwe activiteit**
    * Op deze pagina kan een gebruiker een nieuwe activiteit creëren door middel van het invullen van een formulier.
* **Profiel**
    * Op deze pagina kan een gebruiker zijn/haar eigen gegevens zien en aanpassen.
    * Een gebruiker kan hier alle activiteiten zijn waar hij/zij zichzelf voor aanwezig heeft gezet.
* **Login**
    * Op deze pagina kan een gebruiker inloggen. De 'users' tabel uit de database zal controleren of de ingevoerde gegevens correct zijn.
* **Registreren**
    * Op deze pagina kan een gebruiker zich registreren. Vanuit deze pagina worden de gegevens van een gebruiker toegevoegd aan de 'users' tabel in de database. 