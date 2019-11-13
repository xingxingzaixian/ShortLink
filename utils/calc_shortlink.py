# encoding: utf-8
"""
@version: 1.0
@author: 
@file: calc_shortlink
@time: 2019-10-29 23:28
"""
import redis
from shortlink.settings import REDIS_HOST, REDIS_PORT


class CalcShortLink:
    """
    计算短码类
    """
    def __init__(self, data):
        self.rc = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=1)
        self.sixty_binary = 'RoTLSFJPQm3KHksGOBt7NdEUxpryuWv89qw6cbY2CVIX0zgZeD5jMhflA41ian'
        self.url = data.get('url')

    def parse(self):
        """
        根据计数计算短码，并返回链接地址，默认为6位短码，所以要从5**62次方开始计数
        :return:
        """
        count = int(self.rc.get('count'))
        if not count:
            count = 62 ** 5

        short_code = self.calc_short_code(count + 1)
        self.rc.set(short_code, self.url)
        self.rc.set('count', count + 1)
        return short_code

    def calc_short_code(self, count):
        """
        计算短码
        :param count:
        :return:
        """
        six_list = []
        scale = len(self.sixty_binary)
        six_list.append(self.sixty_binary[count % scale])
        while count > scale - 1:
            count = int(count / scale)
            six_list.append(self.sixty_binary[count % scale])
        return ''.join(six_list[::-1])
