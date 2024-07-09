"""
Author: Jeff Plewak
Date: 2024-07-09
Description: Script to redact sensitive information from files before committing.
"""

import os
import re

def redact_file(file_path):
    """
    Redact sensitive information from a file.
    
    :param file_path: Path to the file to redact.
    """
    with open(file_path, 'r') as file:
        content = file.read()

    # Define patterns to redact
    patterns = {
        'password': 'REDACTED',
        'secret': 'REDACTED',
        'apikey': 'REDACTED',
        'api_key': 'REDACTED',
        'client_secret': 'REDACTED',
        'PRIVATE_KEY': 'REDACTED',
        'SECRET_KEY': 'REDACTED',
        'access_token': 'REDACTED',
    }

    # Redact patterns
    for pattern, replacement in patterns.items():
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

    # Write the redacted content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    """
    Main function to redact sensitive information from all staged files.
    """
    for file in os.popen('git diff --cached --name-only').read().split():
        if os.path.isfile(file):
            redact_file(file)

if __name__ == '__main__':
    main()

