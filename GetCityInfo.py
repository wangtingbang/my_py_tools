import urllib2

svr = "http://www.zou114.com/qh/"

zippage = open("zippage.csv", "r")

for province in zippage.readlines():
    url,name=province.split(",")
    url = url.strip()
    print "=="+url+"=="

    url = svr+url

    print url
    response = urllib2.urlopen(url)

    print response
    break