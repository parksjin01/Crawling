# -*- encoding:utf-8 -*-
import sys
import json
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib2
from bs4 import BeautifulSoup, Comment
import urlparse

def cleaning_code(soup, target="comment"):
    if target == 'comment':
        comments = soup.findAll(text=lambda text: isinstance(text, Comment))
        for comment in comments:
            comment.extract()
    else:
        [x.extract() for x in soup.findAll(target)]

def naver_blog_nhn(url):
    page = urllib2.urlopen(url).read()
    soup = BeautifulSoup(page, 'html5lib')
    frame = soup.findAll('frame', attrs={'id':'mainFrame'})[0]
    url_parse = urlparse.urlparse(url)
    return url_parse.scheme+'://'+url_parse.netloc+frame['src']

def crawl_text(url):
    result = {}
    if urlparse.urlparse(url).netloc == 'blog.naver.com':
        post_number = urlparse.urlparse(url).path.split('/')[-1]
        url = naver_blog_nhn(url)
    page = urllib2.urlopen(url).read()
    try:
        page = unicode(page, 'euc-kr')
    except:
        try:
            page = unicode(page, 'utf-8')
        except:
            try:
                page = unicode(page, 'MS949')
            except:
                pass
    soup = BeautifulSoup(page, "html5lib")
    cleaning_code(soup)
    cleaning_code(soup, 'script')
    netloc = urlparse.urlparse(url).netloc
    if netloc == 'news.naver.com':
        try:
            result['title'] = soup.findAll('h3', attrs={'id':'articleTitle'})[0].text
        except:
            pass
        try:
            result['date'] = soup.findAll('span', attrs={'class': 't11'})[0].text
        except:
            pass
        try:
            result['image'] = [soup.findAll('span', attrs={'class':'end_photo_org'})[0].findAll('img')[0]['src']]
        except:
            pass
        try:
            result['image_description'] = [soup.findAll('span', attrs={'class':'end_photo_org'})[0].text]
            soup.findAll('span', attrs={'class': 'end_photo_org'})[0].extract()
        except:
            pass
        try:
            result['content'] = soup.findAll('div', attrs={'id':'articleBodyContents'})[0].text.replace('\t', '').replace('\n', '')
        except:
            pass
    elif netloc == 'sports.news.naver.com':
        try:
            result['title'] = soup.findAll('h3', attrs={'class':'info_tit'})[0].text
        except:
            pass
        try:
            result['date'] = soup.findAll('span', attrs={'class':'info_date'})[0].text
        except:
            pass
        try:
            content = soup.findAll('div', attrs={'class':'naver_post'})[0]
        except:
            content = soup.findAll('div', attrs={'id':'newsEndContents'})[0]
        img = []
        try:
            img_tag = content.findAll('img')
            for tag in img_tag:
                try:
                    img.append(tag['lazy-src'])
                except:
                    img.append(tag['src'])
        except:
            pass
        result['image'] = img
        result['image_description'] = []
        try:
            result['content'] = content.text.replace('\t', '').replace('\n', '')
        except:
            pass
    elif netloc == 'blog.naver.com':
        try:
            result['title'] = soup.findAll('span', attrs={'class':'pcol1 itemSubjectBoldfont'})[0].text
        except:
            result['title'] = ''
        try:
            result['date'] = soup.findAll('p', attrs={'class':'date fil5 pcol2 _postAddDate'})[0].text
        except:
            result['date'] = ''
        content = soup.findAll('div', attrs={'class':'post-view pcol2 _param(1) _postViewArea%s' %post_number})[0]
        img = []
        try:
            img_tag = content.findAll('img')
            for tag in img_tag:
                img.append(tag['src'])
        except:
            pass
        result['image'] = img
        result['image_description'] = []
        result['content'] = content.text.replace('\t', '')

    return json.dumps(result)



result = crawl_text('http://blog.naver.com/ghjang5711/221048866567')
result = json.loads(result)
print result['title']
print result['image']
print result['image_description']
print result['content']
print result['date']
# print result