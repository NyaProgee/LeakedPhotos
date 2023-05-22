import shutil
import glob
import os 
from tqdm import tqdm
import time

def hello():
    text = """
    "Leaked Photo" v.1

    Добро пожаловатьв  программу "Leaked Photo".  
    Программа предназначена для скачивания всех изображений с PC на флешку.
    Автор не несет ответственность за причиненный ущерб с помощью этой программы.
    Программа была создана в ознокомиельных целях.
    
    """
    print(text)
    time.sleep(4)

def work(pack_photo):
    get_desktop_d = os.getcwd()
    for path in glob.glob(f'{get_desktop_d}/*/'):
        os.chdir(path)
        print(' Каталог:', path[22:-1])
        for i in os.listdir(path="."):
            if( ".jpg" in i or ".JPG" in i or ".png" in i or ".PNG" in i):
                for j in tqdm(i):
                    time.sleep(0.2)
                    try:
                        shutil.copy2(f'{os.getcwd() }' + '\\' + i , pack_photo)
                    except:
                        continue
                    


if( __name__ == '__main__'):
    hello()

    get_now_d = os.getcwd()
    pack_photo = get_now_d +'\\'+ 'Изображения'
    try:
        os.mkdir("Изображения")
        os.chdir("C:/Users/User/Desktop")
    except:
        os.chdir("C:/Users/User/Desktop")

    work(pack_photo)
    input("Нажмите Enter для  завершения программы")