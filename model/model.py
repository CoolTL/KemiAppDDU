from mendeleev import get_all_elements

class Model:
    def __init__(self):


        self.names = ['mass', 'density', 'charge']
        self.infos = ['atomic_weight', 'density', 'dipole_polarizability']
        self.units = ['mass_units', 'density_units', 'charge_units']
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
       el.append("Name: " + element.name)
       n = 0
       for i in self.infos:
           try:
               el.append(self.names[n] + ": " + str(getattr(element, i)) + str(getattr(element, self.units[n])))
           except:
               el.append(self.names[n] + ": " + str(getattr(element, i)))
           n += 1
       return el

model = Model()

print(model.get_info(model.atoms[7]))
