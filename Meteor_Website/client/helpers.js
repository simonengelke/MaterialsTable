UI.registerHelper('materials', function (valueToSearch) {
  if(Session.get('valueToSearch') && valueToSearch!==null && Session.get('activeSearchMaterial')===true){
    if(valueToSearch.indexOf(Session.get('valueToSearch'))===-1){
      html  = '<span style="color: red">&#10008;</span>';
    }else{
      html = '<span style="color: green">&#10004;</span>'
    }
  }else if(Session.get('valueToSearch') && valueToSearch!==null && Session.get('activeSearch')===true){
    if(valueToSearch.indexOf(Session.get('valueToSearch'))===-1){
      html  = '<span style="color: red">&#10008;</span>';
    }else{
      html = '<span style="color: green">&#10004;</span>'
    }
  }else if(valueToSearch===null  && Session.get('activeSearchMaterial')===true){
    html = "No data available";
  }else if(valueToSearch===null  && Session.get('activeSearch')===true){
    html = "No data available";
  }else{
    html = "Search not activated";
  }
  return new Spacebars.SafeString(html);
});

UI.registerHelper('precursors', function (valueToSearch) {
  if(Session.get('valueToSearch') && valueToSearch!==null  && Session.get('activeSearchPrecursor')===true){
    if(valueToSearch.indexOf(Session.get('valueToSearch'))===-1){
      html  = '<span style="color: red">&#10008;</span>';
    }else{
      html = '<span style="color: green">&#10004;</span>'
    }
  }else if(Session.get('valueToSearch') && valueToSearch!==null  && Session.get('activeSearch')===true){
    if(valueToSearch.indexOf(Session.get('valueToSearch'))===-1){
      html  = '<span style="color: red">&#10008;</span>';
    }else{
      html = '<span style="color: green">&#10004;</span>'
    }
  }else if(valueToSearch===null  && Session.get('activeSearchPrecursor')===true){
    html = "No data available";
  }
  else if(valueToSearch===null  && Session.get('activeSearch')===true){
    html = "No data available";
  }else{
    html = "Search not activated";
  }
  return new Spacebars.SafeString(html);
});