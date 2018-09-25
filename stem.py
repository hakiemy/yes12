leeftijd = int(input('Wat is je leeftijd? '))
id = input('Heb je een paspoort? ')
if leeftijd <18 or id == 'nee':
    print('Nop, opdonderen!')
else: print('Gefeliciteerd...')