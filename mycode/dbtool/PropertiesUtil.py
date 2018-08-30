class PropertiesUtil(object):
    __file_dict = {}

    def get_config_dict(self, file_path):

        if file_path not in self.__file_dict:
            properties = {}
            with open(file_path, 'r') as pro_file:
                for line in pro_file.readlines():
                    line = line.strip().replace('\n', '')
                    if line.find('=') > 0 and not line.startswith('#'):
                        strs = line.split('=')
                        value = line[len(strs[0]) + 1:]
                        self.__get_dict(strs[0].strip(), properties, value.strip())
            self.__file_dict[file_path] = properties
        return self.__file_dict[file_path]

    def get_config_value(self, file_path, prop_name):

        return self.get_config_dict(file_path)[prop_name]

    def __get_dict(self, dict_name, properties, value):

        if dict_name.find('.') > 0:
            key = dict_name.split('.')[0]
            properties.setdefault(key, {})
            self.__get_dict(dict_name[len(key) + 1:], properties[key], value)
        else:
            properties[dict_name] = value


prop = PropertiesUtil()
