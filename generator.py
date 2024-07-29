import secrets
import string
from colorama import init, Fore
from pyfiglet import figlet_format

# Initialize colorama
init()

# Print ASCII art at the top
ascii_art = figlet_format("Password Generator", font="small")
print(Fore.GREEN + ascii_art)
# Define password length input
lengt = int(input("Enter the Length of password: "))

# Function to generate password
def generate_password(length=lengt):
    characters = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(characters) for i in range(length))
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

# Generate and print password
generated_password = generate_password()
print(Fore.CYAN + "Generated password: " + Fore.YELLOW + generated_password)
