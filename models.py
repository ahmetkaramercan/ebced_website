from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username):
        self.username = username
        self.id = username  # Use username as the ID

    @staticmethod
    def get(username):
        users = User.load_users()
        print(f"Looking for user: {username}")
        print(f"Available users: {list(users.keys())}")
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
                        try:
                            username, password = line.split(':')
                            users[username] = password
                        except ValueError:
                            print(f"Invalid line in users.txt: {line}")
                            continue
            print(f"Loaded {len(users)} users from file")
        except FileNotFoundError:
            print("users.txt file not found")
        except Exception as e:
            print(f"Error loading users: {str(e)}")
        return users

    @staticmethod
    def save_users(users):
        """Save users to the users.txt file"""
        try:
            with open('users.txt', 'w', encoding='utf-8') as f:
                for username, password in users.items():
                    f.write(f"{username}:{password}\n")
            print("Users saved successfully")
        except Exception as e:
            print(f"Error saving users: {str(e)}")

    def check_password(self, password):
        users = self.load_users()
        stored_password = users.get(self.username)
        print(f"Checking password for user: {self.username}")
        print(f"Stored password exists: {stored_password is not None}")
        return stored_password == password

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