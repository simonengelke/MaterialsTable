Meteor.startup(function () {

  if(ContentTable.find().fetch().length===0){
    var content = [
      {"doi" : "10.1007/s10904-013-9977-8", "solid_state" : true, "title" : "Titanate Anodes for Sodium Ion Batteries", "first_author" : "Marca M. Doeff", "materials_experimental" : [ "PW3040", "K0.8[Ti1.73Li0.27]O4", "Li2CO3", "TiO2", "NaOH", "NaPF6", "Na2Ti3O7", "NaTi3O6(OH)·2H2O", "K2CO3", "Na2CO3", "Na2Ti6O13", "HCl" ], "doi_link" : "http://dx.doi.org/10.1007/s10904-013-9977-8", "precursors_experimental" : [ "Li2CO3", "K2CO3", "Na2CO3" ], "max_temperature_experimental" : 800 },
      {"doi" : "10.1021/cm500342m", "solid_state" : true, "title" : "Lepidocrocite-type Layered Titanate Structures: New Lithium and Sodium Ion Intercalation Anode Materials", "first_author" : "Mona Shirpour", "materials_experimental" : [ "PW3040", "Li2CO3", "TiO2", "NaPF6", "NaCl", "HNO3", "K2CO3", "K0.8Ti1.73Li0.27O4", "LiPF6", "LaB6" ], "doi_link" : "http://dx.doi.org/10.1021/cm500342m", "precursors_experimental" : [ "Li2CO3", "K2CO3", "TiO2" ], "max_temperature_experimental" : 800 },
      {"doi" : null, "solid_state" : true, "title" : "Rational synthesis of anode materials for sodium-ion batteries Na x [Ti 2-x/2 Mg x/2 ]O 4 (x=0.7-0.9) and strategies toward automated and collaborative materials development", "first_author" : "Simon Engelke", "materials_experimental" : [ "K0.9Ti1.55Mg0.45O4", "K0.8Ti1.6Mg0.4O4", "Na0.8Ti1.6Mg0.4O4", "TiO2", "MgO", "K0.8[Ti1.73Li0.27]O4", "NaCl", "K0.9[Ti1.55Mg0.45]O4", "Na0.9[Ti1.55Mg0.45]O4", "Na0.7[Ti1.65Mg0.35]O4", "Mg(NO3)2•6H2O", "K2CO3", "K0.7[Ti1.65Mg0.35]O4", "K0.7Ti1.65Mg0.35O4." ], "doi_link" : null, "precursors_experimental" : [ "Mg(NO3)2•6H2O", "MgO", "K2CO3", "TiO2" ], "max_temperature_experimental" : 1100 }
    ];
    content.forEach(function (content) {
      ContentTable.insert(content);
    });
  }
  ContentTable._ensureIndex({ doi: 1 });
});