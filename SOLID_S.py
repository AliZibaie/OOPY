class User:
    def __init__(self):
        self.users = []
    def appendUser(self, info):
        self.users.append(info)
    def findByname(self, name):
        result = []
        for user in self.users:
            if user.name == name:
                result.append(name)
        return result


class UserValidation:
    def validate(self, email, age):
        if not email or '@' not in email:
            print("Invalid email!")
            return False

        if age < 18:
            print("User must be 18 or older!")
            return False

class UserORM:

    def create(self, info):
        #Stimulate add new user record
        return true

    def update(self, info):
        # Stimulate updating user record
        return true

    def read(self, info):
        # Stimulate reading a record
        return true

class EmailService:
    def send(self, email, name):
        # Stimulate sending an email
        return true


class UserService:
    def add_user(self, name, email, age):
        # Responsibility 1: User validation
        if(not UserValidation().validate( "ali@example.com", 25)):
            return False

        # Responsibility 2: Creating user object
        user = {
            'name': name,
            'email': email,
            'age': age
        }
        newUser = User().appendUser(user)

        # Responsibility 3: Database operations
        UserORM().create(newUser)

        # Responsibility 4: Sending email notifications
        UserService().send(email, name)

        return True

# Usage example
if __name__ == "__main__":
    manager = UserService()
    manager.add_user("Ali Rezaei", "ali@example.com", 25)
    manager.add_user("Sara Mohammadi", "sara@example.com", 30)
