import urllib.request
from ip2geotools.databases.noncommercial import DbIpCity
import json
class NetworkInfo:
    def __init__(self):
        self.users = {}

    def get_client_information(self,ip):
        try:
            res = DbIpCity.get(ip, api_key="free")
            print(f"IP Address: {res.ip_address}")
            self.users=json.loads(res.ip_address)
            if self.users['ip'] is None:
                raise Exception('Data not valid')
        except ValueError:
            raise Exception('Unable to find your network')

    def get_public_ip(self):
        try:
            external_ip= urllib.request.urlopen('http://ipinfo.io/json').read().decode('utf8')
            if external_ip is not None:
                self.get_client_information(external_ip)
            else:
                raise Exception("Process failed for lake information")
        except ConnectionError:
            raise Exception('Unable to get Main Information.')
    
    