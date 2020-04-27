// Connect using a MongoClient instance

const MongoClient = requires('mongodb').MongoClient;

// Connection url

const url = 'mongodb://Aline1:aline1@ds061355.mlab.com:61355/heroku_njkl5bj0';

// Database Name

const dbName = 'time_record';

// Connect using MongoClient

MongoClient.connect(url, function(err, client) {

// Select the database by name

const time_recordDb = client.db(dbName);

client.close();

});



   