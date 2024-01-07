class UserProfile:
    def __init__(self, username, email, password, security_question):
        self._username = username
        self._email = email
        self.__password = password
        self.__security_question = security_question

    # Getter methods
    def get_username(self):
        return self._username

    def get_email(self):
        return self._email

    # Setter methods
    def set_email(self, new_email):
        self._email = new_email

    def set_password(self, new_password):
        self.__password = new_password

    # Private method to validate security question
    def __validate_security_question(self, entered_answer):
        return entered_answer == self.__security_question

    # Public method to access private method securely
    def reset_password(self, entered_answer, new_password):
        if self.__validate_security_question(entered_answer):
            self.__password = new_password
            print("Password reset successful.")
        else:
            print("Invalid answer. Password reset failed.")
