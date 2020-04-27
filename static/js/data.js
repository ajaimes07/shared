var MongoClient = require('mongodb').MongoClient;
Server = require('mongodb').Server;



//var url = "mongodb://Aline1:aline1@ds061355.mlab.com:61355/heroku_njkl5bj0";

MongoClient.connect("mongodb://Aline1:aline1@ds061355.mlab.com:61355/heroku_njkl5bj0", function(err, db) {
    db.collection('time_record', function (err, collection) {

        collection.find().toArray(function(err,items) {
            if(err) throw err;
            console.log(items);
        });
    });    
});
       

   