import requests
import os
import time

from selenium import webdriver
import pandas as pd


def save_photo(root, url, num):
    if not os.path.exists(root):
        os.makedirs(root)  # 若没有街景图片文件夹则自动创建
    m = str(num) + ".jpg"
    name = root + m
    r = requests.get(url)
    if 'message' in r.text:
        print('number ', num, 'does not have picture')
        return
    with open(name, "wb") as f:
        f.write(r.content)
def main():
    # 全景图参数
    heading = "150" # 全景图的水平视角[0-360]
    pitch = "15" # 全景图的垂直视角[0-90]
    fov = "90" # 全景的水平方向范围[10-360]，360显示全景图

    num = 1 # 计数
    ak = '' # 百度API ak
    xy_file_name = '123.xlsx' #经纬度z文件
    root = "images_baidu/"  # 图片保存位置
    xy_pd = pd.read_excel(xy_file_name)
    for x,y in zip(xy_pd.x, xy_pd.y):
        location = str(x)+","+str(y)
        url = "http://api.map.baidu.com/panorama/v2?ak=" + ak + "&width=1024&height=512&location=" + location + "&fov=" + fov + "&heading=" + heading + "&pitch=" + pitch
        save_photo(root, url, num)
        # time.sleep(1)
        num += 1

if '__name__' == '__main__' :
    main()

