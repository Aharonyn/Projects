const Account = require('../../models/account/Account');

module.exports = async function(req, res, next) {
	if (req.method === 'POST'){ // if the request method is POST, execute.
		const {email, name, age} = req.body;
		const account = new Account({email, name, age});
		const email_account = await Account.findOne({email: email}); // waiting for a response.
		if (!email_account){ // if this email doesn't exist, saves to the DB. 
			await account.save();
			return res.send({message: 'success'});
		} else { // if this email already exists.
			return res.send({error: "email already exists"});
		} 
	}
	return res.send({message: 'This is not a POST request'});
};