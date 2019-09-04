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

module.exports = router;

