var express = require('express');
var router = experss.Router();
var mongo = require('mongodb');
var assert = require('assert');

var url = "mongodb://Aline1:aline1@ds061355.mlab.com:61355/heroku_njkl5bj0";

router.get('/', function(req,next) {
    res.render('index');
});

router.get('/get-data', function(req,next) {
    var resultArray = [];
    mongo.connect(url, function(err,db) {
        assert.equal(null,err);
        var cursor = db.collection('time_record').find();
        cursor.forEach(function(doc,err) {
            assert.(null, err);
            resultArray.push(doc);
        }, function() {
            db.close();
            res.render('index', {items: resultArray })
        })
    })
})
       