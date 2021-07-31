import pytest
import requests
import json

from testcase.yaml_util import YamlUtil


class TestApi:

    @pytest.mark.parametrize('args',YamlUtil('testcase/test_api.yaml').read_yaml())
    def test_02(self,args):
        url = args['request']['url']
        method= args['request']['method']
        headers = args['request']['headers']
        params = args['request']['params']
        resp = requests.request(url=url,method=method,params=params,headers=headers)
        resp = json.loads(resp.text)
        if 'eq' in args['assert']:
            assert args['assert']['eq']['ret'] == resp['ret']

