email = input("Enter email: ").strip()

username = email[:email.index("@")]

domain = email[email.index("@")+1:]

print(f"your username {username}.your domain name {domain}")