from abc import ABCMeta, abstractmethod


class Account(metaclass=ABCMeta):
    
    @abstractmethod
    def _approve_transaction(self) -> bool:
        """Approve a transaction, returns true if approved, false otherwise"""

    def withdraw(self, ammount):
        """concrete method that makes use of the _approve_transaction method"""