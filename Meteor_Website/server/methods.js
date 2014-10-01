Meteor.methods({
  searchContent: function (valueToSearch, paramsSort) {
  	Log.error(ContentTable.find({materials_experimental: {$regex: valueToSearch, $options: "i"}}, paramsSort).fetch());
    return ContentTable.find({materials_experimental: {$regex: valueToSearch, $options: "i"}}, paramsSort).fetch();
  },
  searchContentMaterial: function (valueToSearch, paramsSort) {
  	Log.error(ContentTable.find({materials_experimental: {$regex: valueToSearch, $options: "i"}}, paramsSort).fetch());
    return ContentTable.find({materials_experimental: {$regex: valueToSearch, $options: "i"}}, paramsSort).fetch();
  },
  searchContentPrecursor: function (valueToSearch, paramsSort) {
  	Log.error(ContentTable.find({precursors_experimental: {$regex: valueToSearch, $options: "i"}}, paramsSort).fetch());
    return ContentTable.find({precursors_experimental: {$regex: valueToSearch, $options: "i"}}, paramsSort).fetch();
  },
  totalPages: function () {
    return ContentTable.find({}).count();
  }
});
