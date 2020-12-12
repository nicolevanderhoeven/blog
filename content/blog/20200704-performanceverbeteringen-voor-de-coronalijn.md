---
title: "Performanceverbeteringen voor de coronalijn: de kracht van angst"
date: 2020-07-04T21:35:43+01:00
draft: false
tags: ['nederlands', 'performance', 'text']
---

_Originally published on [Medium](https://medium.com/@n_vanderhoeven/performanceverbeteringen-voor-de-coronalijn-de-kracht-van-angst-8c3713a3b7e0). English version [here](https://www.flood.io/blog/performance-testing-the-story-of-the-dutch-co2020ronavirus-hotline)._

Op 1 juni heeft de landelijke GGD Ghor aangekondigd dat iedereen met klachten een coronatest zou kunnen aanvragen door de afsprakenlijn (0800–1202) te bellen. De belofte: vandaag het telefoongesprek, morgen de coronatest en over twee dagen de uitslag. Echter was het in werkelijkheid niet zo makkelijk. Op de eerste dag was er chaos en veel Nederlanders meldden verbindingsproblemen vanwege drukte op de overbelaste systemen.

Dit had voorkomen kunnen worden door een beter begrip te hebben over de manier waarop de menselijke psychologie de performance van een systeem kan beïnvloeden.

![](/blog/assets/20200704-01.jpg)
_Bron: [@ggdghornl](https://twitter.com/GGDGHORNL/status/1267351996379643906), Twitter_

## De situatie

“Voor die 30.000 tests per dag zijn we nu eindelijk klaar”, [zei arts Ann Vossen](https://nos.nl/collectie/13824/artikel/2335758-ggd-en-klaar-voor-massaal-testen-tijd-van-limiterende-factoren-voorbij) op 31 mei. Dit aantal verwijst naar de [landelijke capaciteit](https://nos.nl/artikel/2335790-drukte-op-nieuw-telefoonnummer-voor-coronatests-0800-1202.html) van alle GGD’s. In plaats daarvan werden volgens het AD maar 1146 mensen getest en, misschien belangrijker, een kleine 5478 afspraken gemaakt. De situatie werd erger gemaakt door de [323.000 mensen](https://www.ad.nl/binnenland/liefst-323-000-telefoontjes-naar-nieuw-nummer-voor-coronatest-systemen-overbelast~a16a9a50/) die de afspraaklijn op de eerste dag hebben gebeld. Sommige medewerkers konden zelfs [niet in de systemen inloggen](https://www.volkskrant.nl/nieuws-achtergrond/coronatestnummer-kampt-met-kinderziektes-maar-ggd-s-kunnen-de-drukte-goed-aan~b2f332d2/).

Op Twitter vertelden gebruikers enkele horrorverhalen: één beweerde [6 uur lang te hebben gewacht](https://twitter.com/Ed_van_Iterson/status/1267429180347691011), alleen om een melding te horen dat het systeem geen afspraken kon aanmaken; een andere klaagde over [verbroken verbindingen](https://twitter.com/maticus_spazz/status/1267374692941418496), zelfs toen een medewerker al had geantwoord, en nog een andere [een video had gepost](https://twitter.com/leovanlinden/status/1267408142813605888) van een gesprek dat beëindigd was zonder melding. Ik heb zelf ook de [coronalijn gebeld](https://twitter.com/n_vanderhoeven/status/1271054286483533825), en nieuwe problemen gevonden.

Gelukkig was de tweede dag beter: er waren 11 duizend afspraken gemaakt, mede vanwege het lagere aantal telefoontjes en mede vanwege verholpen technische problemen. In de eerste week nam het aantal geteste mensen toe naar 50.000 (gemiddeld 7142 per dag), wat toch nog veel lager zat dan verwacht. Er zijn wat lessen die we kunnen trekken uit dit verhaal.

![](/blog/assets/20200704-02.jpeg)
_Bron: [GGD Hollands Midden](https://ggdhm.nl/thema-s/item/infectieziekten/testbeleid)_

## Het gevolgen van angst op performance

Dit virus heeft ons al een kant van de mensheid getoond die we liever niet willen zien: [vechten over wc-papier](https://www.bbc.com/news/world-australia-51731422), [chaos op de beurs](https://snacks.robinhood.com/newsletters/rMxwcb7y7lMZoI5NY6qf7/), en [sabotage van zendmasten](https://www.volkskrant.nl/nieuws-achtergrond/nctv-waarschuwt-voor-extremistische-protestacties-door-5g-tegenstanders-die-vrezen-voor-coronavirus~bf1400b8/). Hoewel we rationeel willen zijn, is het onmogelijk te zeggen dat dat altijd het geval is. In werkelijkheid hebben we allemaal de neiging gekke dingen te doen. Vooral als we angst hebben.

Geen wonder dan dat de afspraaklijn zo welkom was. 323.000 telefoontjes werden er op de eerste dag verwerkt, wat bijzonder is als we bedenken dat het grootste deel van Nederland in zelfisolatie was, en dus maar een kleine kans had om het coronavirus opgelopen te hebben. In theorie lijkt dit gedrag irrationeel, maar niet onvoorspelbaar.

![](/blog/assets/20200704-03.jpeg)

In het Engels heet het **FOMO**: Fear Of Missing Out. We hebben al [duidelijk gezien](https://www.flood.io/blog/fomo-and-performance-testing-why-robinhood-went-down) hoe FOMO veel meer gebruikers naar een applicatie kan dwingen, met als gevolg bijwerkingen op de performance. Mensen hadden angst dat er niet genoeg coronatesten waren en wilden de eersten in de rij zijn voordat de voorraad helemaal op was.

Ook was er het probleem dat [één op de vier telefoontjes niet over een afspraak ging](https://www.trouw.nl/binnenland/de-balans-na-een-week-testen-het-plan-was-mooier-dan-de-praktijk~b86399b7/), maar over algemene informatie over COVID-19. Dit werd verergerd door het feit dat de eerste dag van de coronalijn ook Tweede Pinksterdag was. Het teveel aan telefoontjes over andere zaken dan de coronatest was een bijkomende factor in de systeemoverbelasting.

Wat hadden we kunnen doen om dit systeem te verbeteren?

## Verbeteringen

### Beter inschatten

Hoewel het moeilijk is om de gevolgen van FOMO precies te kennen, kunnen we het wel inschatten. [Volgens RIVM-hoofd Jaap van Dissel](https://www.zwollenu.nl/500-000-tot-700-000-nederlanders-besmet-met-coronavirus/), waren er begin mei tot 700.000 mensen in Nederland besmet met het coronavirus, een paar weken voor de coronalijn werd opgestart. Waarom was het dan een verrassing dat meer dan 300.000 mensen hadden gebeld? Ook zijn de cijfers van niet-COVID-gerelateerde klachten daar nog niet bij inbegrepen.

Zelfs als we inschatten dat [20% van die 700.000 mensen geen klachten had](https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200306-sitrep-46-covid-19.pdf?sfvrsn=96b04adf_4), komen we toch op een voorspelling van 140.000 telefoontjes uit, wat nog **25 keer** meer is dan het werkelijke aantal gemaakte afspraken op de eerste dag.

Zodra wij aantallen hebben, kunnen we testen.

![](/blog/assets/20200704-04.jpg)

Uit mijn eigen ervaring, toen ik het coronanummer belde, blijkt dat er een telefonieserver was die de oproepen heeft doorgeschakeld naar verschillende medewerkers (die thuis werkten). In deze stap konden loadtesten worden uitgevoerd om zeker te weten hoeveel gesprekken deze server aankon, en dat het snel genoeg was om geen of weinig message queueing te hebben.

Medewerkers hebben dan vermoedelijk gegevens direct in een afsprakensysteem ingevoerd tijdens de oproep, waarop de gegevens waarschijnlijk naar een backend server en database gingen. Ook hier kunnen we testen via een load testing tool op protocol niveau, zoals JMeter.

Met zo’n publieke startdatum zou ik spike testen hebben gevoerd met tot 700.000 gebruikers (misschien nog meer, als ik wat tijd had). In een spike test simuleren we een snelle toename van gebruikers op een kort tijdstip, bijvoorbeeld 1 tot 700.000 gebruikers in 10 minuten. Ook zouden soak testen heel nuttig zijn geweest, vooral omdat de coronalijn van 08.00 tot 20.00 was geopend, dus een stroom van 12 uur. In een soak test voeren we een constante aantal gebruikers voor een langere periode op.

### Automatisering gebruiken

Het maken van een afspraak voor de coronatest had veel stappen. Eerst moesten mensen hun BSN en andere details aan de medewerkers geven. Dan moesten medewerkers vragen naar hun klachten. Alleen met de [belangrijkste klachten](https://www.zwollenu.nl/500-000-tot-700-000-nederlanders-besmet-met-coronavirus/) die passen bij het coronavirus konden mensen verdergaan. Uiteindelijk moesten medewerkers adressen controleren en het dichtstbijzijnde testcentrum vinden om de afspraak te maken.

Telefoniesystemen gebruiken soms Interactive Voice Response (IVR) technologie, een systeem van menu’s en keuzen. We hebben dit allemaal gebruikt: “Voor het Nederlands, toets 1. Voor het Engels, toets 2…” Zo’n systeem had het aantal niet afspraak-gerelateerde gesprekken kunnen verlagen met 25% (één op vier klanten belden niet voor een afspraak), en op een geautomatiseerde manier.

Hier is een voorbeeld van een IVR-systeem:

![](/blog/assets/20200704-05.jpg)
_Bron: [Vanguard Networks](http://vanguardnetworks.com.sg/IVR.html)_

Op het niveau van het IVR-systeem kan het wel moeilijk zijn om load te simuleren. [Empirix Hammer](https://www.empirix.com/products/hammer/) and [Cyara](https://cyara.com/genesys-cloud/) zijn twee zeer gespecialiseerde tools die dit kunnen doen.

Nog een optie voor de implementatie van een afsprakensysteem is een web app, met verplichte velden voor BSN, adressen, enz, en met een verbinding met DigiD, een identiteitsverificatiesysteem. [Mijn Overheid](https://mijn.overheid.nl/) bestaat al, en ook met DigiD integratie. Er had een soort van beveiligde formulier kunnen worden gebruikt om klantengegevens snel op te nemen.

![](/blog/assets/20200704-06.jpg)
_Bron: [Mijn Overheid](https://mijn.overheid.nl/)_

### End-to-end testing uitvoeren

Vaak spreken we over de performance van één applicatieserver, maar in praktijk zijn er meerdere componenten. Als best practice is het goed om de performance van elk onderdeel van het hele systeem te testen, en dan ook de hele keten.

Voor een afsprakenlijn zou het redelijk zijn geweest om het hele proces te testen: het oproepdoorschakelingssysteem, het afspraaksysteem, de database met gegevens en datums, de servers van elke GGD in het land, en het sturen van email en SMS-berichten met afspraak datums. Het is belangrijk om te weten of alle componenten snel samen kunnen werken.

Ook is er de performance van niet-computer onderdelen. De menselijke component kan ook een bottleneck zijn. Wisten de medewerkers hoe snel ze moesten vragen of een klant een afspraak wilde maken? Kunnen de testen worden uitgevoerd en de uitslagen worden gegeven, zelfs met een snelstromend afspraaksysteem? Het teveel aan afspraken toegewezen aan GGD’s kan ook files veroorzaken (zoals in [Eindhoven](https://www.ed.nl/eindhoven/in-de-file-voor-een-stukje-zekerheid-meteen-drukte-bij-teststraat-voor-corona-in-eindhoven~a27eec83/) en [Goes](https://www.pzc.nl/zeeuws-nieuws/drukte-bij-teststraat-in-goes-na-openstellen-nummer-voor-coronatest~aa8a6cb2/)).

## Conclusie

In dit geval had slechte performance een invloed niet op de winst maar op de gezondheid. Zieke personen die klachten hadden, konden niet allemaal een afspraak maken om getest te worden. Hoeveel andere mensen hadden ze inmiddels besmet? Slechte performance heeft medewerkers ook gedwongen om soms uitslagen te geven “[in verdekte termen](https://wnl.tv/2020/06/08/chaos-bij-de-coronalijn-personeel-slaat-alarm/)”, wat tot een privacyschending kan leiden.

![](/blog/assets/20200704-07.jpg)

De menselijke component kan een systeem lastiger maken om te testen. Aldus [Andrea Evers (LUMC)](https://www.trouw.nl/binnenland/de-balans-na-een-week-testen-het-plan-was-mooier-dan-de-praktijk~b86399b7/), hoogleraar gezondheidspsychologie: 

> Door de uitbraak van corona zijn mensen in een langdurige stresssituatie beland. Onzekerheid, onvoorspelbaarheid en oncontroleerbaarheid maken dat ze de behoefte hebben om zaken juist wel te controleren of voorspelbaar te maken.

Als performancetesters kunnen we statistieken en een systematische aanpak combineren met kennis van de menselijke factoren om te plannen voor het onvoorspelbare.