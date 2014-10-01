Meteor.publish("ContentTable", function (numberOfResults, page) {
  return ContentTable.find({}, {skip: page*numberOfResults, limit: numberOfResults});
});

Meteor.publish('searchHistory', function () {
  return Searches.find({userId: this.userId});
});