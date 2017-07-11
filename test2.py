# a = '''http://blog.naver.com/PostView.nhn?blogId=symin67&logNo=221048814253&redirect=Dlog&widgetTypeCall=true&topReferer=https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fwhere%3Dnexearch%26sm%3Dtop_hty%26fbm%3D1%26ie%3Dutf8%26query%3D%25EC%25BC%2580%25EC%25BC%2580%25EC%25BC%2580'''
# b = '''http://blog.naver.com/PostView.nhn?blogId=symin67&logNo=221048814253&redirect=Dlog&widgetTypeCall=true&topReferer=https%3A%2F%2Fsearch.naver.com%2Fsearch.naver%3Fwhere%3Dnexearch%26sm%3Dtop_hty%26fbm%3D1%26ie%3Dutf8%26query%3D%25EC%25BC%2580%25EC%25BC%2580%25EC%25BC%2580'''
# print a == b

import urlparse
print urlparse.urlparse('http://blog.naver.com/symin67/221021847693').path