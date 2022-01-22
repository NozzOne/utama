import requests, re
from jsbeautifier.unpackers import packer


class Fembed:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        id = self.getUrl(self.url)

        if id:
            r = requests.post("https://www.fembed.com/api/source/"+id)
            if r.status_code == 200:
                return self.parse(r.json())
            else:
                return None
            

        else:
            return None
            
    def parse(self, response):
        array = []
        for i in response['data']:
            array.append(i['file'])
            array.append(i['label'])
        return array[2]

        

    def getUrl(self, string:str):
        regex =  "(v|f)(\\/|=)(.+)(\\/|&)?";
        match = re.search(regex, string)
        if match:
            return match.group(3)
        else:
            return None


class SolidFiles:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        
        r = requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
        if r.status_code == 200:
            return self.getUrl(r.text)
        else:
            return None

    def parse(self, response:str):
        src = self.getUrl(response)
        if src:
            return src

    def getUrl(self, string:str):
        regex =  "downloadUrl\":\"(.*?)\""
        match = re.search(regex, string)
        if match:
            return match.group(1)
        else:
            return None


class MixDrop:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        if id:
            r = requests.post(self.url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
            if r.status_code == 200:
                return self.parse(r.text)
            else:
                return None
        else:
            return None



    def parse(self, response:str):
        unpacker = self.getEvalcode(response)

        if packer.detect(unpacker):
            src:str = self.getsrc(packer.unpack(unpacker))
            if src and src.__len__() > 0:
                src = "https:"+src
                return src
            else:
                return None
        else:
            return None
    def getsrc(self, code):
        regex = "wurl=?\"(.*?)\";"
        match = re.search(regex, code)
        if match:
            return match.group(1);


    def getEvalcode(self, html:str):
        regex = "eval(.*)"
        match = re.search(regex, html)
        if match:
            return match.group(0);
        else:
            return None

