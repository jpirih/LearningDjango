# Learning Django Framework

## About - Na splošno
V tej mapi je več projektov, ki sem jih ustvarjal ali
s pomočjo različnih tutorialov ali pa s pomočjo 
django dokumentacije 

Vsebina  teh spletnih aplikacij nima kakšne posebne veze 
bolj je šlo za to, da sem se učil in testiral različne 
možnosti.

## Vsebina 
1. Projekt DatabaseFun
2. Projekt KonferencaDemo
3. Projekt mysite
4. Projekt TestDjango
5. Ogrodje Test 

### Projekt DatabaseFun 
Je osnven django projekt usvarjen s pomočjo trutoriala 
dosegljivega na [linku](https://www.youtube.com/watch?v=HcDcl5RNM90) -
Python and Django Tutorials Building Websites from Scratch. 

Izdelano s pomočjo Visual studio 2015 Community Editon in 
PTVS - Python Tools for Visal studio. Čisto osnoven tutorial 
brez django administracije.

Osnovne značilnosti: 
* modeli - tabele za bazo podatkov so v models.py
* uporaba Model forms za oblikovanje obrazcev na osnovi tabele
* Preprosta aplikacija tipa music store. 
* osnovni name kako delujejo povezave views.py, urls.py, models.py
* osnvna logika povezav in obveznih elementov za delovanje aplikacije ...
* narejen na osnovi predloge iz programa Visual Studio

### Projekt KonferencaDemo 

Je en projekt narejen na osnovi tutoriala, ki je dosegljiv na
tej [povezavi](https://www.youtube.com/watch?v=FsdpoXDFh34) -
Django Tutorial for Beginners | Django in the Real World. 

Projekt je sicer pisan v programu Visual Studio. 

Osnovne zančilnosti
* Strat from blank project 
* Zagon iz konzole <code>django-admin startproject Konferenca</code>
* Potem seveda  nova pod mapa za app <code> django-admin startapp app </code>
* Baza podatkov je enako kot v prvem primeru sqlite3
* Modeli tabele so v app.models.py   
* obvezno, kot vedno `python manage.py makemigrations app` in 
* ` python manage.py migrate` - ustavi bazo podatkov.
* uporaba django admin
* modeli registrirni v app.admin.py, polje za iskanje, filter
* django-auth sistem. - auth.py 
* uporaba django.generic layouts, modelform app.forms.py
* uporaba crispy_froms - bootstrap...

### Projekt mysite

Je napisan točno po django docs - uradni dokumentaciji ni še
dokončan praktično je samo začet prazen projekt še vedno uporabljam
za kakšne teste in učeje. 
 
 ###  Projekt TestDjango 
 je v bistvu en predpripravljen primer, ki se dobi, če
 naložiš PTVS - samples  Primeri uporabe za Visual studio 2015.
 Samples for PTVS 2.2
 
 V bistvu ni nič spremenjen samo zato, da sem na začetku videl,
 kakšna je struktura projekta :) 
 
 ### Ogrodje Test 
 
 V Mapi test je v bistvu ogrodje sestavljeno na podlagi več.
 tutorialov in dokumentacije za Google App Engine. 
 
 Gre za **ogrodje**, ki omogoča gradnjo **django web** in 
 deploy aplikacije na Google cloud. **Preden izvedeš deploy 
 spremeni  id aplikacije v app.yaml skripti** :) 