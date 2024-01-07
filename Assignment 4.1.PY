class BankAccount:
    def __init__(self, account_number, balance, owner_name, pin):
        self._account_number = account_number
        self._balance = balance
        self.__owner_name = owner_name
        self.__pin = pin

    # Getter methods
    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def get_owner_name(self):
        return self.__owner_name

    # Setter methods
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print("Invalid balance. Balance must be non-negative.")

    def set_owner_name(self, new_owner_name):
        self.__owner_name = new_owner_name

    # Private method to validate PIN
    def __validate_pin(self, entered_pin):
        return entered_pin == self.__pin

    # Public method to access private method securely
    def display_balance(self, entered_pin):
        if self.__validate_pin(entered_pin):
            print(f"Account balance for {self.__owner_name}: {self._balance}")
        else:
            print("Invalid PIN. Access denied.")
