#!/usr/bin/env python3
import os
import random
import subprocess
from datetime import datetime

# Ensure the script runs in its own directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

def ensure_number_file_exists():
    """Ensure the number.txt file exists and initialize it if missing."""
    if not os.path.exists("number.txt"):
        with open("number.txt", "w") as f:
            f.write("")

def write_new_number():
    """Write a random number (1-10) to a new line in number.txt."""
    random_number = random.randint(1, 10)
    with open("number.txt", "a") as f:  # Append to the file
        f.write(f"{random_number}\n")
    return random_number

def git_commit():
    """Stage changes, commit with a message, and push."""
    subprocess.run(['git', 'add', 'number.txt'], check=True)

    # Commit message with a timestamp
    commit_message = f"Add random number: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    subprocess.run(['git', 'commit', '-m', commit_message], check=True)

def git_push():
    """Push the committed changes to GitHub."""
    result = subprocess.run(['git', 'push'], capture_output=True, text=True)
    if result.returncode == 0:
        print("Changes pushed to GitHub successfully.")
    else:
        print("Error pushing to GitHub:")
        print(result.stderr)

def main():
    """Main script logic."""
    try:
        ensure_number_file_exists()  # Ensure the file exists
        new_number = write_new_number()  # Add a new random number

        git_commit()  # Commit changes
        git_push()  # Push changes
        print(f"Added new number: {new_number} and changes pushed.")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
