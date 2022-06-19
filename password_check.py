MINIMUM_LENGTH = 7

password = input(f"Enter password (should be above {MINIMUM_LENGTH} characters): ")
while len(password) < MINIMUM_LENGTH:
    password = input(f"Enter password (should be above {MINIMUM_LENGTH} characters): ")
print('*' * len(password))
