# Password Bruteforcer

A Python-based tool for performing dictionary-based brute force attacks on SSH, FTP, and HTTP services.

Note: For learning purposes only

## Features
- Supports multiple protocols:
  - **SSH**: Attempts to authenticate using combinations of usernames and passwords.
  - **FTP**: Performs dictionary-based login attempts on FTP servers.
  - **HTTP**: Sends POST requests to brute force login forms.
- Asynchronous processing for high performance.
- Implements rate limiting to avoid detection.
- Exports successful results to JSON for analysis.

## Requirements
- Python 3.8 or higher
- Virtual environment (optional but recommended)

### Python Libraries
- `paramiko`: For SSH brute forcing.
- `ftplib`: For FTP brute forcing.
- `aiohttp`: For HTTP brute forcing.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/calypso-h97/password_bruteforcer.git
   cd password_bruteforcer
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate   # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the bruteforcer for SSH:
   ```bash
   python3 bruteforcer.py --protocol ssh --target 192.168.1.1 --logins wordlists/logins.txt --passwords wordlists/passwords.txt --rate_limit 0.5
   ```

2. Run the bruteforcer for FTP:
   ```bash
   python3 bruteforcer.py --protocol ftp --target 192.168.1.1 --logins wordlists/logins.txt --passwords wordlists/passwords.txt --rate_limit 1.0
   ```

3. Run the bruteforcer for HTTP:
   ```bash
   python3 bruteforcer.py --protocol http --target http://example.com/login --logins wordlists/logins.txt --passwords wordlists/passwords.txt --login_field username --password_field password --rate_limit 0.2
   ```

### Example Output
```text
[INFO] Starting brute force for SSH on 192.168.1.1
Trying admin:123456
Trying root:password
[SUCCESS] Login: admin | Password: 123456

[RESULTS]
Login: admin | Password: 123456
```

## Configuration
- **Protocols**:
  - `ssh`: Brute force SSH login.
  - `ftp`: Brute force FTP login.
  - `http`: Brute force HTTP login forms.
- **Wordlists**: Place your `logins.txt` and `passwords.txt` in the `wordlists/` directory.

## Future Enhancements
- Add support for multithreading in FTP and HTTP brute force.
- Enhance rate limiting for better evasion techniques.
- Export detailed results to JSON or CSV format for easier analysis.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
[Your Name](https://github.com/calypso-h97)
