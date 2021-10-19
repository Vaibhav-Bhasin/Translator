#### Translator
eng_fr={'hello':'salut',
        'very':'tres',
        'good':'Bon',
        'see':'voir',
        'soon':'bientôt',
        'bye':'au revoir',
        "house":"maison",
       "apple":"pomme",
       "tree":"arbre",
       "horse":"cheval",
       "yellow":"jaune",
       "keyboard":"clavier",
       "water":"eau",
       "start":"commencer",
       "city":"ville",
       "ear":"oreille",
       "eel":"anguille",
       "tooth":"dent",
      "thank you":"merci",
      "thank": "remercier",
      "you":"vous"}
translate = input("Enter something in English:: ")
translate = translate.split()
print("In French we say it:")
for i in translate:
  print(eng_fr[i],end = " ")
