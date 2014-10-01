## Instructions

Locate this folder in Terminal and use the commands below to import the CSV files with the Molecula Formulas into your local MongoDB. 

mongoimport --db materialstable_check --collection lib_anode --type csv --headerline --file LIB_Anode_Materials.csv

mongoimport --db materialstable_check --collection lib_cathode --type csv --headerline --file LIB_Cathode_Materials.csv

mongoimport --db materialstable_check --collection lib_electrolyte --type csv --headerline --file LIB_Electrolyte_Materials.csv

mongoimport --db materialstable_check --collection lib_solvent --type csv --headerline --file LIB_Solvents.csv

mongoimport --db materialstable_check --collection inorganic_compound --type csv --headerline --file Name_Formula_Inorganic_Compounds.csv

mongoimport --db materialstable_check --collection not_material --type csv --headerline --file Not_material.csv

mongoimport --db materialstable_check --collection formula_material --type csv --headerline --file Formula_Material.csv