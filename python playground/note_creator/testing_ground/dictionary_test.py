__author__ = 'Ian'

# elements = {}
#
# elements['H'] = {'name': 'Hydrogen',
#                  'number': 1,
#                  'weight': 1.00794}
# elements['He'] = {'name': 'Helium',
#                   'number': 2,
#                   'weight': 4.002602,
#                   'noble gas': True}
#
#
# print elements['H']['name']
# print elements['H']['weight']
# print elements['He']['name']
# print elements['He']['number']

planet_names = ['Mercury',
                'Venus',
                'Earth',
                'Mars',
                'Jupiter',
                'Saturn',
                'Neptune',
                'Uranus',
                'Pluto']

planets = dict((p[:3].lower(), p) for p in planet_names)

planets['nep'] = {'color': 'blue',
                  'distance': 7}
# print planets['mer']
# print planets['nep']
print planets['nep']