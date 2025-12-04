class UserManager:
    """
    This class violates SRP by handling multiple responsibilities:
    1. User data management
    2. Database operations
    3. Email notifications
    4. Report generation
    """

    def __init__(self):
        self.users = []

    def add_user(self, name, email, age):
        # Responsibility 1: User validation
        if not email or '@' not in email:
            print("Invalid email!")
            return False

        if age < 18:
            print("User must be 18 or older!")
            return False

        # Responsibility 2: Creating user object
        user = {
            'name': name,
            'email': email,
            'age': age
        }
        self.users.append(user)

        # Responsibility 3: Database operations
        self.save_to_database(user)

        # Responsibility 4: Sending email notifications
        self.send_welcome_email(email, name)

        # Responsibility 5: Logging
        self.log_user_creation(name)

        return True

    def save_to_database(self, user):
        # Simulating database save
        print(f"Saving {user['name']} to database...")
        # Database connection logic here
        # SQL queries here

    def send_welcome_email(self, email, name):
        # Email sending logic
        print(f"Sending welcome email to {email}...")
        # SMTP configuration here
        # Email template here
        subject = "Welcome!"
        body = f"Hello {name}, welcome to our platform!"
        # Send email logic

    def log_user_creation(self, name):
        # Logging logic
        print(f"LOG: User {name} created at 2024-11-20")
        # Write to log file

    def generate_user_report(self):
        # Responsibility 6: Report generation
        print("=== User Report ===")
        total_users = len(self.users)
        avg_age = sum(u['age'] for u in self.users) / total_users if total_users > 0 else 0

        print(f"Total Users: {total_users}")
        print(f"Average Age: {avg_age:.2f}")

        # Generate PDF or Excel file
        print("Generating PDF report...")

    def delete_user(self, email):
        # Find and delete user
        for user in self.users:
            if user['email'] == email:
                self.users.remove(user)
                # Delete from database
                print(f"Deleting {email} from database...")
                # Send goodbye email
                print(f"Sending goodbye email to {email}...")
                # Log deletion
                print(f"LOG: User {email} deleted")
                return True
        return False


# Usage example
if __name__ == "__main__":
    manager = UserManager()
    manager.add_user("Ali Rezaei", "ali@example.com", 25)
    manager.add_user("Sara Mohammadi", "sara@example.com", 30)
    manager.generate_user_report()
    manager.delete_user("ali@example.com")