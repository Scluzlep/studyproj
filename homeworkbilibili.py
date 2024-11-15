import requests
import csv

mid = (input('收藏夹mid'))
if mid == '':
    mid = 3334243529
else:
    mid = mid
for i in range(1, 6):
    pn = i
    like_list_url = f'https://api.bilibili.com/x/v3/fav/resource/list?media_id={mid}&pn={pn}&ps=20'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' +
                      'AppleWebKit/537.36 (KHTML, like Gecko) ' +
                      'Chrome/112.0.0.0 Safari/537.36'
    }
    response = requests.get(like_list_url, headers=headers)
    json_data = response.json()

    fields_left = ['title', 'cover', 'bvid']

    if i == 1:
        mode = 'w'
    else:
        mode = 'a'

    with open('media_list.csv', mode=mode, newline='') as file:
        writer = csv.writer(file)

        if i == 1:
            writer.writerow(fields_left)
        writer.writerow([f'page{i}'])

        for data in json_data['data']['medias']:
            list = data['title'], data['cover'], 'https://b23.tv/' + data['bvid']
            writer.writerow(list)
print('csv has saved')
