########################################################
# Sample accounts blueprint of endpoints
########################################################
from flask import Blueprint, request, jsonify, make_response
import json
from src import db


accounts = Blueprint('accounts', __name__)

# add a new retirement transaction 
@accounts.route('/retirement_transaction/<int:account_num>', methods=['POST'])
def add_new_retirement_transaction(account_num):

    # Collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # Extracting the variables
    transaction_type = the_data['transaction_type']
    amount = the_data['amount']

    # Constructing the query
    query = 'INSERT INTO retirement_transaction (account_num, transaction_type, amount) VALUES ('
    query += str(account_num) + ', "'
    query += transaction_type + '", '
    query += str(amount) + ')'
    current_app.logger.info(query)

    # Executing and committing the insert statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Success!'

########################################################

# Update instrument information for a specific instrumentID (PUT request)
@accounts.route('/instruments/<int:instrumentID>', methods=['PUT'])
def update_instrument(instrumentID):
    # Collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # Extracting the variables
    accountNum = the_data['accountNum']
    quotes = the_data['quotes']
    instrument_type = the_data['type']

    # Constructing the query for updating instrument information
    query = 'UPDATE instruments SET accountNum = {}, quotes = {}, type = "{}" WHERE instrument_ID = {}'.format(
        accountNum, quotes, instrument_type, instrumentID)
    current_app.logger.info(query)

    # Executing and committing the update statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Instrument information updated successfully!'

########################################################

# Delete instrument information for a specific instrumentID (DELETE request)
@accounts.route('/instruments/<int:instrumentID>', methods=['DELETE'])
def delete_instrument(instrumentID):
    # Constructing the query for deleting instrument information
    query = 'DELETE FROM instruments WHERE instrument_ID = {}'.format(instrumentID)
    current_app.logger.info(query)

    # Executing and committing the delete statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Instrument information deleted successfully!'

if __name__ == '__main__':
    app.run(debug=True)

########################################################

# Get all trade information for a particular account
@accounts.route('/trades/<int:accountNum>', methods=['GET'])
def get_trades(accountNum):
    # Constructing the query to retrieve trade information for the specified account number
    query = 'SELECT * FROM trades WHERE accountNum = {}'.format(accountNum)
    current_app.logger.info(query)

    # Executing the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    trades = cursor.fetchall()

    return jsonify(trades)

########################################################

# Add information of a trade that took place, reflecting the transaction that occurred
@accounts.route('/trades', methods=['POST'])
def add_new_trade():
    # Collecting data from the request object
    the_data = request.json
    current_app.logger.info(the_data)

    # Extracting the variables
    accountNum = the_data['accountNum']
    date = the_data['date']
    number_of_shares = the_data['number_of_shares']
    price_per_share = the_data['price_per_share']
    total_amount = the_data['total_amount']
    instrumentID = the_data['instrumentID']
    buy_or_sell = the_data['buy_or_sell']

    # Constructing the query for adding a new trade
    query = 'INSERT INTO trades (accountNum, date, number_of_shares, price_per_share, total_amount, instrumentID, buy_or_sell) VALUES ({}, "{}", {}, {}, {}, {}, {})'.format(
        accountNum, date, number_of_shares, price_per_share, total_amount, instrumentID, buy_or_sell)
    current_app.logger.info(query)

    # Executing and committing the insert statement
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    return 'Trade information added successfully!'

########################################################

# Return all account information for a particular user
@accounts.route('/accounts/<int:id>', methods=['GET'])
def get_accounts(id):
    # Constructing the query to retrieve account information for the specified user ID
    query = 'SELECT * FROM accounts WHERE userID = {}'.format(id)
    current_app.logger.info(query)

    # Executing the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    accounts = cursor.fetchall()

    return jsonify(accounts)

if __name__ == '__main__':
    app.run(debug=True)   