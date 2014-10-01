// sort searches by date for display

// is not secure yet, through Chrome console others can see private searches. Ideally, only not-logged in searches
// can be openly seen, but not when logged in.

Template.history.searches = function () {
  return Searches.find({userId: Meteor.userId()}, {sort: {date: -1}});
};