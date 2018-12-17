# RTR105
Datormācības kursa elektroniskā klade
## 2. nodarbība izmantotās komandas
**Ctrl+Alt+T** - termināļa atvēršana  
*burts*+**TAB(2x)** - komandu saraksts ar noteikto burtu  
**Q** - saraksta aizvēršana  
*sh* - pārslēgšanās uz Shell valodu  
**Ctrl+L** - termināļa attīrīšana  
**Ctrl+Alt+F(1-7)** - pārvietošanās uz citām OS vidēm  
*man* *command* - komandas apraksts  
*echo* - izmantotā kodu valoda  
*echo $0* - izmantotās kodu valodas detalizētāks apraksts  
*whoami* - lietotājs  
*who* - lietotāja pieslēguma vide un laiks  
*pwd* - lokācija failu sistēmā  
*ls* - galveno failu un mapju saraksts  
*ls -l* - galveno failu un mapju detalizēts apraksts  
*ls -al* - visu failu, mapju detalizēts apraksts
## 3. nodarbības izmantotās komandas
*cd* - pārvietošanās mapju sistēmā  
*.* - cd . nonākt tekošajā direktorijā (palikt uz vietas)  
*..* - cd .. nonākt par mapi uz augšu mapju direktorijā  
*/* - cd / saknes apgabala apzīmejums (root) (augstākā direktorija)  
*/home/user* **/** **~** **/** *cd* - atgriezties sākuma direktorijā  
*mkdir* - izveidot mapi  
*rmdir* - dzēst mapi  
*rm -r* - dzēst mapi ar visām apakšmapēm  
*echo* (teksts) - parādīt tekstu  
*echo -e (teksts)\n(teksts)* - teksts pa rindkopām (\n)  
*cat (fails)  
more (fails)  
less (fails)* - faila lasīšana  
*echo (teksts) **>** fails.txt* - izveidot failu ar (tekstu)  
*echo (teksts) **>>** fails.txt* - papildina failu ar (tekstu)  
*nano (fails)* - atver tekstu redaktorā  
*chmod 540 fails.txt* - maina darbību atļaujas failam (540 pēc binārajiem cipariem RWX RWX RWX - 101 100 000)  
*cp fails1.txt fails2.txt* - failu kopēšana (1. fails - faila nosaukums pēc kopēšanas)  
*mv fails1.txt Music/* - faila pārvietošana uz *Music/* direktoriju  
**fails** - zvaigznītes apzīmē filtrē visus failus, kam nosaukumā fails  
*rm* - dzēst failu  
*rm -f* - dzēst failu, ja ir liegta piekļuve (rwx)  
## 4. nodarbības komandas 
Lai izveidotu skriptu, kas izpilda vairākas komandas vienlaicīgi, izpilda šādas darbības:  
1)Izveido teksta failu - *nano mans_skripts.sh*  
2)Raksta ceļu un programmēšanas valodu ar kuru tiek izpildīts skripts - *#!bin/bash  
3)Ieraksta komandas. piem. *mkdir Mape...*  
4)*PATH=$PATH:~* - paplašina adresi komandu meklēšanai  
5)Saglabā failu  
6)Lai atļautu palaist skriptu, nepieciešams modificēt faila atļaujas - *chmod 764 mans_skripts.sh  
7)Palaiž skriptu *mans_skripts.sh*
## 5. nodarbības komandas  
### Komandas ar programmatūras valodu "python"  
*python* - startē programmatūras valodu  
*vars()* - visas pieejamās komandas funkcija  
*__builtins__.__doc__* - īss apraksts komandai *__doc__*  
*print()* funkcija, kas parāda aprakstu ar komandām tajā (/n - kā rindkopas atstarpe)  
*a = 10* - piešķirt mainīgajam "a" vērtību 10  
a ir vesels skaitlis, kas python uztver kā "integer"  
*b = 1.56* - piešķirt mainīgajam "b" vērtību 1.56   
b ir reāls skailis - "float"  
*c = 'A'* - "c" mainīgais ir A  
*ipython* -  
*idle* -
## 6. nodarbības komandas
*input()* - Lietotājam pieprasa ievadīt skaitli (Piem. input("Ievadi skaitli:")  
*raw_input()* - Pieprasa ievadīt tekstu (Piem. raw_input("Ievadi Tekstu:")  
## 9. nodarbības komandas - Funkcijas
*def thing():* - *def* rada jaunu funkciju ar nosaukumu thing()  
*def thing(a, b):* - funkcija ar diviem argumentiem  
*return* - def funkcijas beigās attēlo fināla rezultātu ar 2 argumentiem  
## 10. nodarbība - cikli  
## 11. nodarbība - strings  
Dažādu *string type* funkciju pielietojums  
Piem.  
word = "alpha"  
*len(word)* - simbolu skaits *word*  
*.lower()* - lowercase letters  
## 14. nodarbibas Laboratorijas darbs - Teilora rindas cos(x^2)  
 RTR105/cos(x^2).png

## 17. Skaitliskā diferencēšana
8 . laboratorijas darbs - atvasinajums ar savu funkciju *cos(x^2)*  
skatīt derivative.png  
skatīt atvasinajums.py  
## 18. Skaitliskā integrēšana  
*MonteCarlo* metode - *random.uniform*  



