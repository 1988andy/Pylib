import urllib.request

class WebClient:
    def __init__(self, url):
        '''
        Initializes a WebClient instance with url parameter.
        '''
        self.url = url

    def getbytes(self):
        '''
        Gets the responsed bytes.
        '''
        return urllib.request.urlopen(self.url).read()

    def getstring(self, encoding = "utf-8"):
        '''
        Gets the responsed string using the specified coding(utf-8).
        '''
        return self.getbytes().decode(encoding)


def webrequest(url, encoding = "utf-8"):
    return WebClient(url).getstring(encoding)

