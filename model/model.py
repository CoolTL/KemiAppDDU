from mendeleev import get_all_elements

class Model:
    def __init__(self):


        self.names =[ 'Series',
                      'Mass',
                      'Density',
                      'Electronegativity',
                      'Volume',
                      'Mass Number',
                      'Melting Point',
                      'Boiling Point',
                      'Discovery Year',
                      ]
        self.infos = ['series',
                      'atomic_weight',
                      'density',
                      'en_pauling',
                      'atomic_volume',
                      'mass_number',
                      'melting_point',
                      'boiling_point',
                      'discovery_year'
                      ]
        self.units = ['',
                      'u',
                      '$\\frac{\\text{kg}}{\\text{m}^3}$',
                      '',
                      '$\\frac{\\text{cm}^3}{\\text{mol}}$',
                      '',
                      '$\\text{K}$',
                      'K',
                      '',

                      ]
        self.atoms = []
        self.table = []
        for el in get_all_elements():
            self.atoms.append(el)

        self.layout= [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,
         3,4,0,0,0,0,0,0,0,0,0,0,5,6,7,8,9,10,
         11,12,0,0,0,0,0,0,0,0,0,0,13,14,15,16,17,18,
         19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,
         37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,
         55,56,0,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,
         87,88,0,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,
         0,0,0,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,
         0,0,0,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103
         ]
        # Rename the layout to the elements
        counter = 0
        for i in self.layout:
            if self.layout[counter] != 0:
                self.layout[counter] = self.atoms[i-1]
            counter += 1

    def get_info(self, element):
        el = []
        el.append(element.name)
        n = 0
        for i in self.infos:
            try:
                el.append(self.names[n] + ": " + str(getattr(element, i)) + str(self.units[n]))
            except:
                try:
                    el.append(self.names[n] + ": " + str(getattr(element, i)))
                except:
                    el.append(self.names[n] + ": N/A")
            n += 1
        return el
    
    def search(self, search):
        """ This returns a list of all elements names' matching the search """
        results = []
        if search.title() == 'Bo Alsworth Tvede':
            results.append(self.atoms[9].name)
        elif search.title() == 'Rong Fu':
            results.append(self.atoms[103].name)
        for i in self.atoms:
            if str(search).lower() in i.name.lower():
                results.append(i.name)
        return results


model = Model()

print(model.get_info(model.atoms[0]))
print(model.search('Hydrogen'))

