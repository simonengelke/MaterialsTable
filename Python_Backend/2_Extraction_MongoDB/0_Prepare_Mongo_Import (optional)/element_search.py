# -*- coding: utf-8 -*-

from pymongo import Connection
import re

"""STARTING VARIABLES"""
elements = ['Am', 'Ar', 'As', 'At', 'Au', 'Ba', 'Be', 'Bh', 'Bi', 'Bk', 'Br', 'B', 'Ca', 'Cd', 'Ce', 'Cf', 'Cl', 'Cm', 'Cn', 'Co', 'Cr', 'Cs', 'Cu', 'C', 'Db', 'Ds', 'Dy', 'Er', 'Es', 'Eu', 'Fe', 'Fl', 'Fm', 'Fr', 'F', 'Ga', 'Gd', 'Ge', 'He', 'Hf', 'Hg', 'Ho', 'Hs', 'H', 'In', 'Ir', 'I', 'Kr', 'K', 'La', 'Li', 'Lr', 'Lu', 'Lv', 'Md', 'Mg', 'Mn', 'Mo', 'Mt', 'Na', 'Nb', 'Nd', 'Ne', 'Ni', 'No', 'Np', 'N', 'Os', 'O', 'Pa', 'Pb', 'Pd', 'Pm', 'Po', 'Pr', 'Pt', 'Pu', 'P', 'Ra', 'Rb', 'Re', 'Rf', 'Rg', 'Rh', 'Rn', 'Ru', 'Sb', 'Sc', 'Se', 'Sg', 'Si', 'Sm', 'Sn', 'Sr', 'S', 'Ta', 'Tb', 'Tc', 'Te', 'Th', 'Ti', 'Tl', 'Tm', 'Uun', 'Uuo', 'Uup', 'Uus', 'Uut', 'Uuu', 'U', 'V', 'W', 'Xe', 'Yb', 'Y', 'Zn', 'Zr']
elements_set = set(elements)

"""INPUT FIELDS"""
amount_elements_str = raw_input("Enter #no elements: ")
amount_elements_int = int(amount_elements_str)

elements_input = []

for x in range(1, amount_elements_int + 1):
  element_number = raw_input("Please enter Element " + str(x) + ": ")
  while element_number not in elements_set:
    print "Element incorrect, enter again!"
    element_number = raw_input("Please enter Element " + str(x) + ": ")

  elements_input.append(element_number)

"""MONGO QUERY"""
con = Connection()
db = con.osti

twothousandallfiltered = db.twothousandallfiltered

collected = [{"materials_experimental": re.compile(x)} for x in elements_input] 

query = [{"$unwind": "$materials_experimental"}, 
         {"$match": {"$and": collected}}, 
         {"$project": {"_id": 0, "doi":"$doi", "materials_experimental": "$materials_experimental"}}]

result = twothousandallfiltered.aggregate(query)["result"]

counter = 0
for x in result:
  print    x
  counter = counter + 1
  print counter


"""
def main():
  if len(sys.argv) != 3:
    print 'usage: ./synexp.py {--check_solid_state|--extract_temperature_time} file'
    sys.exit(1)

  option = sys.argv[1]
  field_1 = sys.argv[2]
  field_2
  if option == '--search':
    print extract_temperatures_experimental(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
"""