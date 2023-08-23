class Employee:
    def __init__(self, name, password, salary):
        self._name = name
        self._password = password
        self._salary = salary

    # This is Read-only
    @property
    def name(self):
        return self._name

    # This is Read-only
    @property
    def password(self):
        raise AttributeError('Password not readable')

    # This is Write-only
    @password.setter
    def password(self, new_password):
        self.password = new_password

    # This is Read-only
    @property
    def salary(self):
        return self._salary

    # This is Write-only
    @salary.setter
    def salary(self, new_salary):
        self._password = new_salary