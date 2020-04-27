
// Retrieve
var MongoClient = require('mongodb').MongoClient;

// Connect to the db
MongoClient.connect("mongodb://Aline1:aline1@ds061355.mlab.com:61355/heroku_njkl5bj0", function(err, db) {
  if(!err) {
    console.log("We are connected");
  }
});

   