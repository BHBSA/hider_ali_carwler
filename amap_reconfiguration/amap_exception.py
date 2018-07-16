class AmapException(Exception):
    def __init__(self):
        Exception.__init__(self, '类型总量大于key的数量')
