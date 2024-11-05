import os
import sys
from dotenv import load_dotenv

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from src.account.account_id import AccountId
from src.crypto.private_key import PrivateKey
from src.client.network import Network
from src.client.client import Client
from src.transaction.transfer_transaction import TransferTransaction
from src.hbar import Hbar
from src.query.transaction_get_receipt_query import TransactionGetReceiptQuery
from src.response_code import ResponseCode

load_dotenv()

def query_receipt():
    network = Network(network='testnet')
    client = Client(network)
    operator_id = AccountId.from_string(os.getenv('OPERATOR_ID'))
    operator_key = PrivateKey.from_string(os.getenv('OPERATOR_KEY'))
    recipient_id = AccountId.from_string(os.getenv('RECIPIENT_ID'))
    amount = 10

    client.set_operator(operator_id, operator_key)

    transaction = (
        TransferTransaction()
        .add_hbar_transfer(operator_id, -Hbar(amount).to_tinybars()) 
        .add_hbar_transfer(recipient_id, Hbar(amount).to_tinybars()) 
        .freeze_with(client)
        .sign(operator_key)
    )

    receipt = transaction.execute(client)
    transaction_id = transaction.transaction_id
    print(f"Transaction ID: {transaction_id}")
    print(f"Transfer transaction status: {ResponseCode.get_name(receipt.status)}")


    receipt_query = (
        TransactionGetReceiptQuery()
        .set_transaction_id(transaction_id)
    )

    receipt = receipt_query.execute(client)
    print(f"Queried transaction status: {ResponseCode.get_name(receipt.status)}")

if __name__ == "__main__":
    query_receipt()
