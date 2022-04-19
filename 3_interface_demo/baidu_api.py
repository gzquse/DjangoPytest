# -*- coding:utf-8 -*-
"""
模块描述:
百度云api调用请求的方法
作者：Sniper.ZH
"""
import time

import requests
import base64
from PIL import Image

Api_key = "dtF1dfAEPwgiq4pxcZdfkIfm"
Secret_key = "d2zqGKn0D7BwYZsCD8j9wBFhdIhKzHMT"


def fetch_token():
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={Api_key}&client_secret={Secret_key}'
    response = requests.get(host)
    if response:
        print(response.json())

    return response.json().get("access_token") if response.status_code == 200 else None


def ocr_numbers(img_path):
    """
    数字识别
    """
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/numbers"
    # 二进制方式打开图片文件
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = fetch_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())

    return response.json()['words_result'][0]['words']


def ocr_text(img_path):
    """
    通用文字识别
    """
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # 二进制方式打开图片文件
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())

    params = {"image": img}
    access_token = fetch_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
    return response.json()['words_result'][0]['words']


def ocr_text_with_location(img_path):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general"
    # 二进制方式打开图片文件
    f = open(img_path, 'rb')
    img = base64.b64encode(f.read())

    time.sleep(0.2)
    params = {"image": img}
    access_token = fetch_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())
    return response.json()


def cut_image(img_path, x_count=2, y_count=2):
    image = Image.open(img_path)
    width, height = image.size

    item_width = width // x_count
    item_height = height // y_count

    box_list = []
    for i in range(0, y_count):
        for j in range(0, x_count):
            box = (j * item_width, i * item_height, (j+1)*item_width, (i+1)*item_height)
            box_list.append(box)

    image_list = [{"image": image.crop(box), "box": box} for box in box_list]

    index = 1
    res = []
    for im in image_list:
        image_name = "images/"+str(index)+".png"
        im['image'].save(image_name, "PNG")
        index += 1
        res.append({"image": image_name, "box": im['box']})
    return res


def is_complete(d_words):
    """检查识别是否结束"""
    for key in d_words.keys():
        if d_words[key] is None:
            return False
    return True


def get_words_location(small, big):
    # 每一个字和顺序
    words_list = list(ocr_text(small))
    print(words_list)

    words_dict = {x: None for x in words_list}

    # cut_list = [(1, 1), (1, 2), (2, 1), (2, 2)]
    cut_list = [(x, y) for x in range(1, 4) for y in range(1, 4)]
    print(cut_list)

    for _x, _y in cut_list:
        if is_complete(words_dict):
            break

        for image in cut_image(big, _x, _y):
            if is_complete(words_dict):
                break

            resultJson = ocr_text_with_location(image['image'])
            if resultJson['words_result_num'] > 0:
                print("图片识别结果", resultJson['words_result_num'])
                for result in resultJson['words_result']:
                    if result['words'] in words_list:
                        result['location']['left'] += image['box'][0]
                        result['location']['top'] += image['box'][1]
                        words_dict[result['words']] = result['location']
    return words_list, words_dict


if __name__ == '__main__':
    # number = ocr_numbers("images/randCode.png")
    # print(number)

    # ocr_text("images/small.png")
    # ocr_text_with_location("images/big.png")
    wl, wd = get_words_location("images/small.png", "images/big.png")
    print(wl)
    print(wd)
