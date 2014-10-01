Router.configure({
  layoutTemplate: 'layout',
  waitOn: function () {
    return [
      Meteor.subscribe('ContentTable', Session.get('limitValues'), Session.get('page'), function () {
        Session.set('numberOfPages', Math.floor(ContentTable.find({}).count()/Session.get('limitValues')));
      })
    ];
  }
});

var limitValues;
var numberOfPage;

Router.map(function () {
  this.route('index', {
    path: '/',
    template: 'index',
    data: function () {
      Log.info(Session.get('activeSearch'));
      if(Session.get('sortDirection')!==undefined && Session.get('activeSearch')===false) {
        var params = {sort:{}};
        params.sort[Session.get('orderByColumn')] = Session.get('sortDirection');
        return {
          content: ContentTable.find({}, params).fetch()
        };
      }else if(Session.get('activeSearch')===false){
        var paramsDefault = {sort:{}};
        paramsDefault.sort['title']=-1;
        return {
          content: ContentTable.find({}, paramsDefault).fetch()
        };
      }else if(Session.get('activeSearch')===true){
        Log.info("Router general search");
        var params = {sort:{}};
        params.sort[Session.get('orderByColumn')] = Session.get('sortDirection');
        Meteor.call('searchContent', Session.get('valueToSearch'), params, function (err, result) {
          if(err){
            Log.error(err);
          }
          if(result){
            Session.set('searchResult', result);
          }
        });
        return {
          content: Session.get('searchResult')
        };
      }else if(Session.get('activeSearchMaterial')===true){
        Log.info("Router Materials search");
        var params = {sort:{}};
        params.sort[Session.get('orderByColumn')] = Session.get('sortDirection');
        Meteor.call('searchContentMaterial', Session.get('valueToSearch'), params, function (err, result) {
          if(err){
            Log.error(err);
          }
          if(result){
            Session.set('searchResult', result);
          }
        });
        return {
          content: Session.get('searchResult')
        };
      }else if(Session.get('activeSearchPrecursor')===true){
        Log.info("Router Precursors search");
        var params = {sort:{}};
        params.sort[Session.get('orderByColumn')] = Session.get('sortDirection');
        Meteor.call('searchContentPrecursor', Session.get('valueToSearch'), params, function (err, result) {
          if(err){
            Log.error(err);
          }
          if(result){
            Session.set('searchResult', result);
          }
        });
        return {
          content: Session.get('searchResult')
        };
      }
    }
  })
});

Router.map(function () {
  this.route('history', {
    path: '/history',
    template: 'history'
  })
});

Router.map(function () {
  this.route('about', {
    path: '/about',
    template: 'about'
  })
});
