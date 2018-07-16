from amap_reconfiguration.api_key_list import api_key_list


class ApiKey:
    def __init__(self):
        self.data = api_key_list
        self.index = len(api_key_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            self.index = len(api_key_list) - 1
        else:
            self.index = self.index - 1
        return self.data[self.index]