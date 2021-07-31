import yaml


class YamlUtil:
    def __init__(self,yaml_file):
        """
        通过init方法把yaml文件传入类
        :param yaml_file:
        """
        self.yaml_file = yaml_file

    # 读取yaml文件
    def read_yaml(self):
        """
        读取yaml,对yanl反序列化，把yaml格式转换成dict格式
        :return:
        """
        with open(self.yaml_file,encoding='utf-8')as fp:
            value = yaml.load(fp,Loader=yaml.FullLoader)
            print(value)

        fp = open(self.yaml_file,encoding='utf-8')
        value = yaml.load(fp,Loader=yaml.FullLoader)
        print(value)

        return value

if __name__ == '__main__':
    YamlUtil('test_api.yaml').read_yaml()