class User():
    """Simple user model."""

    def __init__(self, username, name, last_name, password, age, email):
        """Initialize User attributes."""
        self.username = username
        self.name = name
        self.last_name = last_name
        self.password = password
        self.age = age
        self.email = email

    def info(self):
        """Show stored user info."""
        return "Username: " + self.username, "Name: " + self.name + " " + self.last_name, "Password: " + self.password, "Age: " + self.age, "Email: " + self.email


class Admin(User):
    """Admin model."""
    def __init__(self, username, name, last_name, password, age, email):
        """Initialize an User."""
        super().__init__(username, name, last_name, password, age, email)

        def del_user(self):
            """Let Admin delete Users"""
            self.del_user = username