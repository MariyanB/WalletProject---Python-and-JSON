import unittest
import json
from wallet_implementation import WalletImplementation

class TestWallet(unittest.TestCase):
    def setUp(self):
        with open("wallet-data.json") as f:
            data = json.load(f)
        self.wallet = WalletImplementation(data)
        self.account_id = data["accounts"][0]["id"]
    
    def test_get_holder_name(self):
        self.assertEqual(self.wallet.get_holder_name(), "John Smith")
    
    def test_get_balance(self):
        balance = sum([4800, -2400, -278, -500, 1000, -4.9])
        self.assertAlmostEqual(self.wallet.get_balance(self.account_id), balance)
    
    def test_spend_valid_amount(self):
        initial_balance = self.wallet.get_balance(self.account_id)
        new_balance = self.wallet.spend(self.account_id, 100)
        self.assertEqual(new_balance, initial_balance - 100)

if __name__ == "__main__":
    unittest.main()
