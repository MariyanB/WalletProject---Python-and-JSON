from abc import ABC, abstractmethod

class Wallet(ABC):
    @abstractmethod
    def get_holder_name(self):
        """Returns wallet's holder name"""
    @abstractmethod
    def get_balance(account_id: str) -> float:
        """Returns a current balance for account with ``account_id``"""
    @abstractmethod
    def spend(account_id: str, amount: float) -> float:
        """Charge account with ``accountId`` for ``amount`` and returns the updated balance for the account.
        The successful transaction should be stored in transactions list.
        There is no overdraft for the account
        """
    @abstractmethod
    def to_json() -> str:
        """Returns wallet's data in JSON format"""
