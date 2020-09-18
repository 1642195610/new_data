from lxml import etree
html = etree.HTML('<div>姜泽毓你好吖!</div><div class="你最棒啦">')
wai = html.xpath('//div/text()')
nei = html.xpath('//div/@class')
print(wai)
print(nei)