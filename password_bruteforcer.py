import asyncio
import json
from datetime import datetime
from protocols.ssh_bruteforce import ssh_bruteforce
from protocols.http_bruteforce import http_bruteforce
from protocols.ftp_bruteforce import ftp_bruteforce

def load_wordlist(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]
    
def export_results_to_json(results, protocol, target):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"results_{protocol}_{target.replace('.', '_')}_{timestamp}.json"
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)
    print(f"[INFO] Results exported to {filename}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Asynchronous brute forcer for SSH, FTP, and HTTP")
    parser.add_argument("--protocol", choices=["ssh", "ftp", "http"], required=True, help="Choose the protocol to brute force")
    parser.add_argument("--target", required=True, help="Target IP or URL")
    parser.add_argument("--logins", required=True, help="Path to the username wordlist")
    parser.add_argument("--passwords", required=True, help="Path to the password wordlist")
    parser.add_argument("--rate_limit", type=float, default=0.1, help="Delay (in seconds) between attempts to avoid detection")
    parser.add_argument("--login_field", help="Field name for username in HTTP forms (required for HTTP)")
    parser.add_argument("--password_field", help="Field name for password in HTTP forms (required for HTTP)")

    args = parser.parse_args()

    login_list = load_wordlist(args.logins)
    password_list = load_wordlist(args.passwords)
    result = []

    if args.protocol == "ssh":
        print(f"[INFO] Starting brute force for SSH on {args.target}")
        results = asyncio.run(ssh_bruteforce(args.target, 22, login_list, password_list, args.rate_limit))

    elif args.protocol == "ftp":
        print(f"[INFO] Starting brute force for FTP on {args.target}")
        results = asyncio.run(ftp_bruteforce(args.target, 21, login_list, password_list, args.rate_limit))

    elif args.protocol == "http":
        if not args.login_field or not args.password_field:
            print("[ERROR] HTTP brute forcing requires --login_field and --password_field arguments")
            exit(1)
        print(f"[INFO] Starting brute force for HTTP on {args.target}")
        results = asyncio.run(http_bruteforce(args.target, args.login_field, args.password_field, login_list, password_list, args.rate_limit))

    if results:
        print("\n[RESULTS]")
        for result in results:
            print(f"Login: {result[0]} | Password: {result[1]}")
        export_results_to_json(results, args.protocol, args.target)
    else:
        print("\n[INFO] No valid credentials found")


