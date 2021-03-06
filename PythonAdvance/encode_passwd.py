# coding=utf-8

import sys
import uuid
from optparse import OptionParser

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class prpcrypt():
    def __init__(self):
        self.key = prpcrypt.get_mac_address()
        self.mode = AES.MODE_CBC

        # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数
    @staticmethod
    def get_mac_address():
        return uuid.UUID(int=uuid.getnode()).hex[-16:].upper()

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 16
        count = len(text)

        if (count % length != 0):
            add = length - (count % length)
        else:
            add = 0

        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        return b2a_hex(self.ciphertext)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return str(plain_text, encoding="utf-8").rstrip('\0')


usage = """
 python %prog [--data] [--file] [--code]"""

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--data', '-d', dest='data', default='0123456789')
    parser.add_option('--file', '-f', dest='file', default='pw')

    options, args = parser.parse_args()

    pc = prpcrypt()
    e = pc.encrypt(options.data)
    with open(options.file, 'w') as pw_file:
        line = str(e, encoding="utf-8")
        pw_file.write(line)

    with open(options.file) as pw_file:
        e = pw_file.read()
        d = pc.decrypt(e)
        print(e, d)
