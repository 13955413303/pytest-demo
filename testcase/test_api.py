# @pytest.mark.parametrize('args', ['百里', '依然', '星耀'])
# def test_01(self, args):
#     print(args)
import pytest
import requests

from testcase.yaml_util import YamlUtil


class TestApi:

    # @pytest.mark.parametrize('name,age', [['aaa', 12], ['bbb', 18]])
    # def test_02(self, name, age):
    #     print(name, age)
    def test_01(self):
        url = r'http://127.0.0.1/api/mgr/customers?action=list_customer'
        method= 'GET'
        params = {
            'action' : 'list_customer'
        }
        resp = requests.request(url=url,method=method,params=params)
        print(resp.text)
    @pytest.mark.parametrize('args',YamlUtil('test_api.yaml').read_yaml())
    def test_02(self,args):
        print(args)
if __name__ == '__main__':
    pytest.main()
