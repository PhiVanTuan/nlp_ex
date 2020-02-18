import requests
import json
import os

url_category = 'https://tiki.vn/api/v2/products?limit=300&sort=position'
url_product = 'https://tiki.vn/api/v2/reviews?limit=200&sort=score|desc,id|desc,stars|all&include=comments'
url_all="https://tiki.vn/api/v2/categories?parent_id=2&include_in_menu=true"
path = '/home/phivantuan/Documents/craw/'

def loadAll():
    response=requests.get(url_all)
    str_json=response.json()
    data=str_json['data']
    for item in data:
        category_id=item['id']
        loadCategory(category_id,1)

def loadCategory(category_id, page):
    path_=path+str(category_id)
    if not os.path.exists(path_):
        os.makedirs(path_)
    params_category = {}
    params_category['category_id'] = category_id
    params_category['page'] = page
    resp = requests.get(url=url_category, params=params_category)
    str_json = resp.json()
    data = str_json['data']
    if (len(data) > 0):
        for item in data:
            product_id = item['id']
            url = "https://tiki.vn/" + item['url_path']
            lstData = []
            loadPage(category_id,product_id, 1, url, lstData)
        paging = str_json['paging']
        currentPage = paging['current_page']
        lastPage = paging['last_page']
        if currentPage < lastPage: loadCategory(category_id, currentPage + 1)


def loadPage(category_id,product_id, page, url, lstData):
    params_product = {}
    params_product['product_id'] = product_id
    params_product['page'] = page
    resp = requests.get(url=url_product, params=params_product)
    str_json = resp.json()
    data = str_json['data']
    if (len(data) > 0):
        for item in data:
            product = {}
            product['product_id'] = product_id
            product['content'] = item['content']
            product['rating'] = item['rating']
            product['url'] = url
            lstData.append(product)
        page = str_json['paging']
        currentPage = page['current_page']
        lastPage = page['last_page']
        if (currentPage < lastPage):
            loadPage(category_id,product_id, currentPage + 1, url, lstData)
        else:
            json_data = json.dumps(lstData)
            file = open(path + str(category_id)+"/"+str(product_id) + ".txt", "w")
            file.write(json_data)
            file.close()


loadCategory(1789, 1)
