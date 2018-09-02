'''
Parallel使用示例，显著提高速度。
'''
import requests
import re
import sys
import time
from sklearn.externals.joblib import Parallel, delayed
def get_title(url):
    content = requests.get(url).text
    data = re.findall('title="(.*?)">',content)
    #print("finish one page  %s"%(len(data)))
    return data
if __name__=='__main__':
    base_url = "https://bj.lianjia.com/zufang/pg1"
    page_url = []
    for page in range(1,101):
        page_url.append(base_url + str(page))
    now = time.time()
    if len(sys.argv)>=2:
        res = Parallel(n_jobs = int(sys.argv[1]), backend="threading")(delayed(get_title)(url) for url in page_url)
    else:
        res = [get_title(url) for url in page_url]
    print("Finished in ",time.time() - now, "sec")
