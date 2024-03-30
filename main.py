import requests
import os.path
from tqdm import tqdm
import xmltodict, json

tags = ['nipple_fucking','olchas','olexey_oleg']
page = 1
count_page = 0
list_url =[]

for tag in tags:
    count_page = count_page + 1
    path_direct = f'D:\\Хентай art\\{tag}'
    url_rule34xxx_api = 'https://api.rule34.xxx/'
    url_rule34xxx_api_tag = f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tag}&json=1&pid={count_page}'
    url_rule34xxx_api_tag_page = f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tag}'
    response_page = requests.get(url_rule34xxx_api_tag_page)
    response_page = xmltodict.parse(response_page.text)
    response_page = json.dumps(response_page)
    response_page = json.loads(response_page)

    page = int(response_page['posts']['@count']) // 100
    print(f'Найдено страниц:{page}')
    id_art = 0
    for count_page in range(page):
        count_page = count_page +1
        url_rule34xxx_api_tag = f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&tags={tag}&json=1&pid={count_page}'
        response = requests.get(url_rule34xxx_api_tag)
        if response.status_code == 200 and response:
            check_path = os.path.exists(path_direct)
            response = response.json()
            print(f'Скачивается {count_page} страница')
            if check_path:
                pass
            elif not check_path:
                print(f'Папка под тег {tag} не существует')
                os.mkdir(path_direct)
                print(f'Создана папка {tag}')

            for file in tqdm(list(response)):
                name = file['id']
                files = os.listdir(path_direct)
                check_name = str(name) + ".jpeg"
                if check_name in files:
                    print(f'Есть фаил {name}')
                else:
                    # list_url.append(file['file_url'])
                    pict = requests.get(file['file_url'])
                    pict_file = open(f"{path_direct}\\{name}.jpeg", 'wb', )
                    pict_file.write(pict.content)
                    pict_file.close()
                    id_art += 1
                # if not check_name in files and file == response[-1]:
                #     respon = (grequests.get(url) for url in list_url)
                #     respon = grequests.map(respon)
                #     for i, save in enumerate(respon):
                #         pict_file = open(f"{path_direct}\\{name}.jpeg", 'wb', )
                #         pict_file.write(save.content)
                #         pict_file.close()
                #         id_art += 1
                #     list_url=[]
        print(f"Сохранено {id_art + 1} файла")


