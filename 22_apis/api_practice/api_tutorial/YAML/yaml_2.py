import yaml
from yaml import load, dump

yaml.load(stream= , Loader=) # # what does stream and loader do/mean in yaml file?

print (yaml.load(stream=???, Loader=???""" 
... name: Vorlin Laruknuzum
... sex: Male
... class: Priest
... title: Acolyte
... hp: [32, 71]
... sp: [1, 13]
... gold: 423
... inventory:
... - a Holy Book of Prayers (Words of Wisdom)
... - an Azure Potion of Cure Light Wounds
... - a Silver Wand of Wonder
... """))

'''
{'name': 'Vorlin Laruknuzum', 'gold': 423, 'title': 'Acolyte', 'hp': [32, 71],
'sp': [1, 13], 'sex': 'Male', 'inventory': ['a Holy Book of Prayers (Words of Wisdom)',
'an Azure Potion of Cure Light Wounds', 'a Siver Wand of Wonder'], 'class': 'Priest'}
'''

print (yaml.dump({'name': "The Cloak 'Colluin'", 'depth': 5, 'rarity': 45, 'weight': 10, 'cost': 50000, 'flags': ['INT', 'WIS', 'SPEED', 'STEALTH']}))
