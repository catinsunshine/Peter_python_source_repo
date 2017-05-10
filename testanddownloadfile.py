#!/usr/bin/python3
import time
import requests

res = requests.get('https://automatetheboringstuff.com/files1/rj.txt')

Downlotry:
    res.raise_for_status()
except Exception as exc:
    print('Download failed with error: %s' % exc)

playFile = open('download.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

with open('download.txt') as f:
    cont = f.read()
    print(cont)

time.sleep(2)
print('\nThe end')
