const mongoose = require('mongoose');

const notificationShcema = mongoose.Schema({
    accountId: String,
    name: String,
    color: String
});

module.exports = mongoose.model('Notification', notificationShcema);