# -*- encoding： utf-8 -*-
from pprint import pprint
from lxml import etree
import requests
import zipfile
import io


# pycharm激活码
def get_pycharm():
    # url = "http://idea.medeming.com/a/jihuoma2.zip"
    # get_jihuoma(url)
    get_jihuoma_html()


#
def get_jihuoma(url):
    res = requests.get(url=url)
    buffer = io.BytesIO()
    buffer.write(res.content)
    zfile = zipfile.ZipFile(buffer, 'r')
    for file in zfile.filelist:
        # file = zfile.filelist[1]
        print(file.filename.encode('cp437').decode('gbk'))
        content = zfile.read(file.filename).decode()
        print(content)


# 检验是否含有中文字符
def is_contains_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            return True
    return False


def get_jihuoma_html():
    res = {}
    url = "https://www.ajihuo.com/idea/4222.html"
    data = {
        "secret_key": "880914",
        "Submit": "阅读全文"
    }
    resp = requests.post(url=url, data=data)
    html = resp.text
    # print(resp.text)
    html = etree.HTML(html)
    p_list = html.xpath('//blockquote//p/text()')
    # print(p_list[5])
    # print(p_list[6])
    code_list = [e for e in p_list if not is_contains_chinese(e)]
    if len(code_list) == 2:
        res['最新激活码'] = code_list[0]
        res['2018.1以下版本用这个'] = code_list[1]
    else:
        print(code_list)
    pprint(res)
    text = "\r\n2018.1以下版本用这个\r\n".join(code_list)
    with open(file='code.txt',mode='w') as f:
        f.write(text)


# idea激活码
def get_idea():
    get_jihuoma_html()
    # url = "http://idea.medeming.com/a/jihuoma1.zip"
    # get_jihuoma(url)


def main():
    get_pycharm()


if __name__ == '__main__':
    main()
