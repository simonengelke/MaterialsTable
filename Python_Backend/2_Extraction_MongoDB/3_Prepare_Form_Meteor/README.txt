Export MongoDB

mongoexport --db materialstable --collection mt_collection --out mt_collection.json --journal

That regular expression can be used to delete the unwanted parts in the resulting JSON file.

\"_id\"\s:\s\{\s\"\$oid\"\s:\s\"\w*\"\s\},\s

Then commas have to be added after each line in the JSON (excluding the last line) to bring it in the right format for including the extracts in the Meteor_Website server.js