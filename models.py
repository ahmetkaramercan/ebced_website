from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username):
        self.username = username
        self.id = username  # Use username as the ID

    @staticmethod
    def get(username):
        users = User.load_users()
        if username in users:
            return User(username)
        return None

    @staticmethod
    def load_users():
        """Load users from the users.txt file"""
        users = {}
        try:
            with open('users.txt', 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        username, password = line.split(':')
                        users[username] = password
        except FileNotFoundError:
            pass
        return users

    @staticmethod
    def save_users(users):
        """Save users to the users.txt file"""
        with open('users.txt', 'w', encoding='utf-8') as f:
            for username, password in users.items():
                f.write(f"{username}:{password}\n")

    def check_password(self, password):
        users = self.load_users()
        return users.get(self.username) == password

    def change_password(self, new_password):
        users = self.load_users()
        if self.username in users:
            users[self.username] = new_password
            self.save_users(users)
            return True
        return False

    def change_username(self, new_username):
        users = self.load_users()
        if new_username in users:  # Check if new username already exists
            return False
        if self.username in users:
            password = users[self.username]
            del users[self.username]
            users[new_username] = password
            self.save_users(users)
            self.username = new_username
            self.id = new_username
            return True
        return False 