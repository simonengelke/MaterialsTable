Template.index.nameRegex = function () {
  var title = this.title.replace(/ /g, '_');
  return title;
};

Template.index.events({
  'click .sortColumn': function (event) {
    // DGB 22.08 The name of the div that raises the click MUST be the field that we want to sort in the mongo
    Session.set('orderByColumn', event.currentTarget.attributes.name.value);
    if(Session.get('sortDirection')===undefined){
      Session.set('sortDirection', 1);
    }else {
      Session.set('sortDirection', (Session.get('sortDirection')===1) ? -1:1);
    }
  },
  'click .glyphicon-search, keyup #search' : function (event){
    if($('#search').val().length>=2){
      Session.set('valueToSearch', $('#search').val());
      console.log($("#selectedSearch")[0].textContent);
      if($("#selectedSearch")[0].textContent==='Choose search'){
        Session.set('activeSearch', true);
        Session.set('activeSearchMaterial', false);
        Session.set('activeSearchPrecursor', false);
      }
      if($("#selectedSearch")[0].textContent==='Materials'){
        Log.info("Materials");
        Session.set('activeSearch', false);
        Session.set('activeSearchMaterial', true);
        Session.set('activeSearchPrecursor', false);
      }
      if($("#selectedSearch")[0].textContent==='Precursors'){
        Log.info("Precursors");
        Session.set('activeSearch', false);
        Session.set('activeSearchMaterial',  false);
        Session.set('activeSearchPrecursor', true);
      }
    }
    if($('#search').val().length<2){
      Session.set('activeSearch', false);
      Session.set('activeSearchMaterial', false);
      Session.set('activeSearchPrecursor', false);
    }
  },
  'click .nextBtn': function (event) {
    Meteor.setTimeout(function() {
      Session.set('page', Session.get('page')+1);
    }, 500);
    Meteor.subscribe('ContentTable', Session.get('limitValues'), Session.get('page'));
  },
  'click .beforeBtn' : function (event) {
    Meteor.setTimeout(function() {
      Session.set('page', Session.get('page')-1);
    }, 500);
    Meteor.subscribe('ContentTable', Session.get('limitValues'), Session.get('page'));
  },
  'click #materials': function (event) {
    $("#selectedSearch").html('Materials');
    Log.info("MATERIALS");
    Session.set('activeSearchMaterial', true);
    Session.set('activeSearchPrecursor', false);
    Session.set('activeSearch', false);
  },
  'click #precursors': function (event) {
    $("#selectedSearch").html('Precursors');
    Log.info("PRECURSORS");
    Session.set('activeSearchMaterial', false);
    Session.set('activeSearchPrecursor', true);
    Session.set('activeSearch', false);
  }
});

//Default value for this session
Session.set('activeSearch', false);

Template.index.searching = function () {
  if(Session.get('activeSearch')===false){
    return true;
  }
};

Template.index.rendered = function () {
  
};

Session.set('activeSearch', false);
Session.set('activeSearchMaterial', false);
Session.set('activeSearchPrecursor', false);
Session.set('limitValues', 10);
Session.set('page', 1);

Template.index.actualPage = function () {
  Meteor.call('totalPages', function (err, result) {
    if(err){
      Log.error(err);
    }
    if(result){
      Session.set('numberOfPages', Math.round(result/10));
    }
  });
  if (Session.get('numberOfPages') == 0){
    return actualPage +' of 1';
  }
  else {
    return actualPage +' of '+ Session.get('numberOfPages');
  }
  var actualPage = Session.get('page');
  return actualPage +' of '+ Session.get('numberOfPages');
};

Template.index.noLastPage = function () {
  if(Session.get('page')===Session.get('numberOfPages')){
    return false;
  }else{
    return true;
  }
};

Template.index.noZero = function () {
  if(Session.get('page')!==1){
    return true;
  }
};