import json
from wallet import Wallet

class WalletImplementation(Wallet):
    def __init__(self, data):
        self.holder_name = data['holder']['name']
        self.account_id = data['accounts'][0]['id']
        self.transactions = data['accounts'][0]['transactions']
    
    def get_holder_name(self):
        return self.holder_name
    
    def get_balance(self, account_id: str) -> float:
        if account_id != self.account_id:
            raise ValueError("Account not found")
        return sum(self.transactions)
    
    def spend(self, account_id: str, amount: float) -> float:
        if amount < 0:
            raise ValueError("Amount must be positive")
        if account_id != self.account_id:
            raise ValueError("Account not found")

        current_balance = self.get_balance(account_id)
        if current_balance < amount:
            raise ValueError("Insufficient balance")

        self.transactions.append(-amount)
        return self.get_balance(account_id)
    
    def to_json(self) -> str:
        return json.dumps({
            "holder_name": self.holder_name,
            "account_id": self.account_id,
            "balance": self.get_balance(self.account_id)
        })
