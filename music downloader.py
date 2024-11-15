import requests

# API地址和配置
API_URL = "https://api.lolimi.cn/API/qqdg/"
PAGE_SIZE = 10  # 每页显示的歌曲数量

def search_songs(query, page):
    """从API搜索歌曲并返回结果"""
    try:
        response = requests.get(API_URL, params={"word": query, "list": page})
        data = response.json()
        if data['code'] == 200:
            return data['data']
        else:
            print("搜索失败，请检查API或网络连接")
            return []
    except requests.exceptions.RequestException as e:
        print(f"网络错误：{e}")
        return []

def download_song(song,page):
    """下载选中的歌曲"""
    try:
        response = requests.get(API_URL, params={"word": song["song"], "n": 2, "list": page})
        song_data = response.json()
        if song_data['code'] == 200:
            song_url = song_data['data']['url']
            format = song_url.split('.')[-1]  # 动态获取文件格式
            download_response = requests.get(song_url)
            with open(f"{song['song']}.{format}", "wb") as f:
                f.write(download_response.content)
            print(f"{song['song']} 下载完成")
        else:
            print(f"无法下载 {song['song']}，请检查API")
    except requests.exceptions.RequestException as e:
        print(f"下载错误：{e}")

def main():
    print("欢迎使用命令行歌曲下载器")
    query = input("请输入搜索关键词：")
    page = 1

    while True:
        songs = search_songs(query, page)
        if not songs:
            break

        print(f"\n--- 第 {page} 页 ---")
        for i, song in enumerate(songs, start=1):
            print(f"{i}. {song['song']} - {song['singer']} - {song['album']}")

        print("\n选择操作：")
        print("  d [编号] - 下载指定编号的歌曲")
        print("  n - 下一页")
        print("  p - 上一页")
        print("  q - 退出")

        command = input("请输入操作：")

        if command.startswith("d "):
            # 下载指定编号的歌曲
            try:
                index = int(command.split()[1]) - 1
                if 0 <= index < len(songs):
                    download_song(songs[index],page)
                else:
                    print("编号超出范围，请重新输入")
            except ValueError:
                print("请输入正确的编号")

        elif command == "n":
            page += 1
        elif command == "p" and page > 1:
            page -= 1
        elif command == "q":
            print("退出程序")
            break
        else:
            print("无效指令，请重试")

if __name__ == "__main__":
    main()
