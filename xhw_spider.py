import requests
import os
from bs4 import  BeautifulSoup as bs
url = 'http://www.xiaohuar.com/list-1-2.html'

def get_pics(url):
    res = requests.get(url)
    soup = bs(res.text,'html.parser')
    images = soup.select('.img img')
    pic_lists = []
    for i in images:
        if (i['src']).split('.')[1] != 'php':
            pic_lists.append('http://www.xiaohuar.com/'+i['src'])
    return pic_lists
            
        
def save_pics(pic_lists):            
    file_name = input("文件夹名称：")
    os.mkdir(file_name)
    os.chdir(os.path.join(os.getcwd(), file_name))
    i = 0
    j = 0

    print('Spiding...')

    for pic in pic_lists:
        with open(str(i)+'.jpg','wb') as fd:
            response = requests.get(pic)
            fd.write(response.content)
            i += 1
    print('下载完成！')
    
if __name__ == "__main__":
    #save_pics()
    url = "http://www.xiaohuar.com/list-1-{}.html"
    total_pics = []
    print('##############################校花网爬虫##############################')
    page = int(input('爬取页数：'))
    for i in range(0,page + 1):
        new_url = url.format(i)
        pics = get_pics(new_url)
        total_pics.extend(pics)
    save_pics(total_pics)
        

        
 
