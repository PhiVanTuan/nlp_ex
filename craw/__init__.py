from concurrent.futures import ThreadPoolExecutor

import requests
import json
import os
import threading
url_category = 'https://tiki.vn/api/v2/products?limit=300&sort=position'
url_product = 'https://tiki.vn/api/v2/reviews?limit=200&sort=score|desc,id|desc,stars|all&include=comments'
url_all = "https://tiki.vn/api/v2/categories?parent_id=2&include_in_menu=true"
path = '/home/phivantuan/Documents/craw/'


def loadAll():
    response = requests.get(url_all)
    str_json = response.json()
    data = str_json['data']
    executor = ThreadPoolExecutor(max_workers=len(data))
    for item in data:
        category_id = item['id']
        executor.map(loadCategory(category_id,1))



def loadCategory(category_id, page):
    path_ = path + str(category_id)

    if not os.path.exists(path_):
        os.makedirs(path_)
    params_category = {}
    params_category['category_id'] = category_id
    params_category['page'] = page
    resp = requests.get(url=url_category, params=params_category)
    try:
        str_json = resp.json()
        data = str_json['data']
        if (len(data) > 0):
            for item in data:
                product_id = item['id']
                url = "https://tiki.vn/" + item['url_path']
                reviewData = {
                    "productId": product_id,
                    "url": url,
                    "1": [],
                    "2": [],
                    "3": [],
                    "4": [],
                    "5": []
                }
                lstData = []
                loadReview(category_id,  1, reviewData)
            paging = str_json['paging']
            currentPage = paging['current_page']
            lastPage = paging['last_page']
            if currentPage < lastPage: loadCategory(category_id, currentPage + 1)
    except:
        print("An exception occurred")


def loadReview(category_id,  page, reviewData):
    product_id=reviewData['productId']
    print("product_id : " + str(product_id))
    params_product = {}
    params_product['product_id'] = product_id
    params_product['page'] = page
    resp = requests.get(url=url_product, params=params_product)
    try:
        str_json = resp.json()
        data = str_json['data']
        if (len(data) > 0):
            for item in data:
                content=item['content']
                rating=item['rating']
                if rating==1:reviewData['1'].append(content)
                elif rating==2:reviewData['2'].append(content)
                elif rating==3:reviewData['3'].append(content)
                elif rating==4:reviewData['4'].append(content)
                elif rating==5:reviewData['5'].append(content)

            page = str_json['paging']
            currentPage = page['current_page']
            lastPage = page['last_page']
            if (currentPage < lastPage):
                loadReview(category_id,  currentPage + 1, reviewData)
            else:
                # print(json.dumps(reviewData))
                json_data = json.dumps(reviewData)
                print(json_data)
                file = open(path + str(category_id) + "/" + str(product_id) + ".txt", "w")
                file.write(json_data)
                file.close()
    except:
        print("error: " + reviewData['url'])





loadAll()
