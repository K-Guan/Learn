#!/usr/bin/env python3
import os
import time
import shutil
import logging
import requests
from selenium import webdriver
from bs4 import BeautifulSoup


def reader(filename):
    try:
        with open(filename) as f:
            l = f.read().splitlines()
    except UnicodeDecodeError:
        with open(filename, encoding='latin') as f:
            l = f.read().encode('latin').decode(
                'utf16').replace('\n\n', '\n').splitlines()

    return [l[i:i+4] for i in range(0, len(l), 4)]


def file_moving(number, path_from, path_to):
    trying = 0
    number = str(number)
    files_to = [os.path.join(path_to, number+i)
                for i in ['.flv', '_zh.srt', '_en.srt', '_zh_en.srt']]

    time.sleep(180)
    if len(os.listdir(path_from)) == 0:
        raise ConnectionRefusedError('selenium did not download any files')

    while True:
        files_from = sorted(os.path.join(path_from, i)
                            for i in os.listdir(path_from)
                            if i.endswith('.srt') or i.endswith('.flv'))

        if len(files_from) == 3:
            break
        else:
            if trying > 90:
                raise TimeoutError('already half and an hour passed')

            time.sleep(60)
            trying += 1
            logging.debug('seems the files are still downloading; '
                          'trying: {}'.format(trying))

    for file_from, file_to in zip(files_from, files_to):
        shutil.move(file_from, file_to)

    zh, en = [reader(i) for i in files_to[1:3]]
    for i, j in zip(en, zh):
        i.insert(2, j[2])

    with open(files_to[3], 'w') as f:
        f.writelines('\n'.join(i)+'\n' for i in en)

    logging.info('video #{} has been downloaded'.format(number))


logging.basicConfig(format='%(asctime)s -- %(message)s -- %(levelname)s',
                    datefmt='%c', level=logging.DEBUG)

directory = input('Please enter the directory to put the videos: ')
video_list = input('Please enter the URL of the videos list: ')

number = input('Please enter the number of the first video '
               'you are going to download (default is "1"): ')

number = 1 if number == '' else int(number)

soup = BeautifulSoup(requests.get(video_list).text, 'html.parser')
videos = [i.get('href')
          for i in soup.find('table', {'id': 'list2'}).find_all('a')
          if i.get('href')][number-1:]


options = webdriver.ChromeOptions()
options.add_argument("load-extension=/home/kevin/Learn/Python/programs/"
                     "open163_videos_downloader/VideosDownloader")

for video in videos:
    while True:
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(video)
        logging.info('Downloading the #{} video'.format(number))

        try:
            file_moving(number, '/home/kevin/Downloads', directory)
            number += 1
        except (TimeoutError, ConnectionRefusedError) as e:
            logging.warning(e)
            shutil.rmtree('/home/kevin/Downloads')
            os.mkdir('/home/kevin/Downloads')
            continue

        break
