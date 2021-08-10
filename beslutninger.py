#Variabel som inneholder svaret på om personen ønsker brus.
brus = input('Vil du ha brus? ')

#Sjekker om personen svarte Ja/ja. I så fall printes:'Her har du en brus'.
if brus == 'Ja' or brus == 'ja':
    print('Her har du en brus!')

#Sjekker om personen svarte Nei/nei. I så fall, printes: 'Den er grei'.
elif brus == 'Nei' or brus == 'nei':
    print('Den er grei!')
    
#For alt annet enn de to tidligere hvis-setningene printes: 'Det forsto jeg ikke helt'.
else:
    print('Det forsto jeg ikke helt')
