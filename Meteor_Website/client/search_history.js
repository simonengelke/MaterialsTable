// get my search history
Meteor.subscribe('searchHistory');

// insert a new search document when enter key is pressed
Template.index.events({
  'keydown #search': function (e, t) {
    if (e.keyCode === 13) {
    	if (Meteor.userId() !== null){
		    Searches.insert({
	        userId: Meteor.userId(), 
	        value: t.$('#search').val(),
	        date: Date.now()
	      });
    	}
    }
  }
});