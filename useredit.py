import subprocess

def create_user(username, password):
    try:
        # Execute the useradd command to create a new user
        subprocess.run(["useradd", "-m", username])
        
        # Set the password for the new user
        subprocess.run(["passwd", username], input=password.encode(), check=True)
        
        print(f"User {username} created successfully")
    except subprocess.CalledProcessError:
        print(f"Failed to create user {username}")

def delete_user(username):
    try:
        # Execute the userdel command to delete the user
        subprocess.run(["userdel", "-r", username], check=True)
        print(f"User {username} deleted successfully")
    except subprocess.CalledProcessError:
        print(f"Failed to delete user {username}")

def main():
    # Example usage: create a new user
    new_username = input("Enter the username for the new user: ")
    new_password = input("Enter the password for the new user: ")
    create_user(new_username, new_password)
    
    # Example usage: delete a user
    user_to_delete = input("Enter the username of the user to delete: ")
    delete_user(user_to_delete)

if __name__ == "__main__":
    main()
