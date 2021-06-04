import os
import time
import requests
def savepic(results, name):
    # 在当目录下创建文件夹
    if not os.path.exists('./picture'):
        os.makedirs('./picture')

    # 下载图片
    try:
        pic = requests.get(results, timeout=10)
        time.sleep(1)
    except:
        print('当前图片无法下载')
    file_full_name = './picture/' + name
    if not os.path.exists(file_full_name):
        with open(file_full_name, 'wb') as f:
            f.write(pic.content)
        print(name + "完成下载！")
    else:
        print(name+"重复！")