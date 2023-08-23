# Today
De eertste grote uitdaging zat vooral in het feit dat je de huidige datum(today) kan veranderen.
Hierdoor kunnen er producten in de toekomst gekocht en verkocht worden.
Dit heeft weer invloed op de voorraad als de datum bijvoorbeeld weer terug gezet wordt en deze wel weer de juiste voorraad moet weergeven op die datum.
Bijvoorbeeld als er in de toekomst producten verkocht worden en je deze eigenlijk ook wilt verkopen een aantal dagen eerder.
Dit vergde niet echt iets technisch, maar wel een heleboel checks alvorens er een product verkocht kan worden.
Hier is best wel veel tijd in gaan zitten om alle mogelijk scenarios uit te proberen en om deze weer dicht te leggen.

# Pandas
Het tweede punt is het optellen van bijvoorbeeld de omzet in een bepaalde maand van een jaar.
De module Pandas biedt hierin de mogelijkheid om een csv om te zetten in een dataframe, waarin je meer mogelijkheden hebt om met de data om te gaan.
In dit geval bood Pandas de mogelijkheid de verkoop datum(YYYY-MM-DD) te groeperen naar een periode(YYYY-MM).
En voor deze periode dan een nieuwe kolom te maken waarin de omzet van die periode komt te staan.
Dit is mogelijk middels onderstaande snippet van 1 regel, waar je anders denk ik een hoop code nodig hebt.
```sh
revenue_df = sold_csv.groupby(sold_csv['sell_date'].dt.strftime('%Y-%m')).agg(total_sell_price=('sell_price', 'sum'))
```

Uiteindelijk hoef je dan alleen maar de waarde uit de regel en kolom van de opgegeven periode uit het dataframe weer te geven.
```sh
revenue = round(revenue_df.loc[year_month, 'total_sell_price'], 2)
```

# Tabulate
Het derde punt was het vinden een manier om de overzichten in een tabel weer te geven, zoals die te zien is in de opdracht.
Hiervoor ben ik uitgekomen bij de module Tabulate waarmee je een dataframe kan weergeven.
Hierbij is het mogelijk om een grid weer te geven en de index weg te laten zoals in onderstaande snippet.
```sh
print(tabulate.tabulate(inventory_csv, headers='keys', tablefmt='grid', showindex=False))
```