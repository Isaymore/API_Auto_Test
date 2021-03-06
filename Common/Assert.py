#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File:Assert.py
@E-mail:364942727@qq.com
@Time:2020/9/5 23:03 下午
@Author:Nobita
@Version:1.0
@Desciption:Assert断言封装模块
"""

from Common.Log import logger
import json


class Assertions:
    def __init__(self):
        self.log = logger

    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            return True
        except:
            self.log.info("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))

            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True

        except:
            self.log.info(
                "Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except:
            self.log.info("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)

            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            self.log.info("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))

            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            self.log.info("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))

            raise


if __name__ == '__main__':
    # info_body = {'code': 102001, 'message': 'login success'}
    # Assert = Assertions()
    # expect_code = 10200
    # Assert.assert_code(info_body['code'], expect_code)
    pass
