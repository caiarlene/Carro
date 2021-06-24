"""
@Time    :   20/06/2021
@Author  :   Cai Yaling
@Contact :   caiarlene@gmail.com
"""
import logging,time,os

class Logger(object):
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        rq = time.strftime('%Y-%m-%d_%H.%M')
        file_path = os.path.dirname(os.getcwd()) + '/Carro_Python/Logs/'
        file_name = file_path + rq + '.log'
        fn = logging.FileHandler(file_name)
        fn.setLevel(logging.DEBUG)
        formater = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        fn.setFormatter(formater)
        self.logger.addHandler(fn)
        kzt = logging.StreamHandler()
        kzt.setLevel(logging.DEBUG)
        kzt.setFormatter(formater)
        self.logger.addHandler(kzt)
    def getlog(self):
        return self.logger
