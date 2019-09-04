const express = require('express');
const router = express.Router();
const mongoose = require('mongoose');
const Notification = require('../../models/notifcation/notification');

router.post('/', (req, res, next) => {
    const {accountId, name, color} = req.body; // extracting the relevant data from JSON body.
    const notification = new Notification({accountId, name, color}); // creting a new instanse of Notification.
    notification.save().catch(err => { // if an error occured while saving.
        res.send({error: err});
    }).then(result => { // a successfull post.
        res.send({ message: "Notification posted succesfully", result: result});
    });
});

router.get('/', (req, res, next) => {
    const accountId = req.query.accountId; // extracting the relevant parameter from the query.
    Notification.find({accountId : accountId}).exec() // getting back a callback.
    .catch(err => { // if an error occured.
        res.send({error: err}); 
    })
    .then(docs => { // a successfull search.
        res.send(docs);
    });
});

router.delete('/', (req, res, next) => {
    const {accountId, color} = req.query; // extracting the params from the query.
    Notification.deleteMany({accountId: accountId, color: color}).exec() // getting back a callback.
    .catch(err => { 
        res.send({error: err});
    })
    .then(result => { // a successfull removal.
        var messageText = "Notification"; // adjusting the message according to amount of notifications removed.
        if(result.deletedCount > 1){
            messageText += "s";
        }
        messageText += " Deleted";
        res.send({message: messageText, result: result});
    });
});

module.exports = router;

