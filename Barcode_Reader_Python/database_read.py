import urllib2, urllib

def getData(id):
	dbdata = [('id', id), ('value', 'Products'),('content','BBD')]  # The first is the var name the second is the value
	dbdata = urllib.urlencode(dbdata)
	path = 'http://192.168.1.21/database/communication/comm.php' # the url you want to POST to
	req = urllib2.Request(path, dbdata)
	req.add_header("Content-type", "application/x-www-form-urlencoded")
	page = urllib2.urlopen(req).read()


