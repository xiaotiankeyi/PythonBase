# -*-coding:GBK -*-,
from unittest import mock
import unittest
from python_module.mock import temple


class Test_zhifu_statues(unittest.TestCase):
    '''��Ԫ��������'''

    def test_01(self):
        '''����֧���ɹ�����'''
        # mock һ��֧���ɹ�������
        temple.zhifu = mock.Mock(
            return_value={
                "result": "success",
                "reason": "null"})
        # ����֧���������ҳ����ת
        statues = temple.pay_statues()
        print(statues)
        self.assertEqual(statues, "֧���ɹ�")

    def test_02(self):
        '''����֧��ʧ�ܳ���'''
        # mock һ��֧���ɹ�������
        temple.zhifu = mock.Mock(return_value={"result": "fail",
                                               "reason": "����"})
        # ����֧���������ҳ����ת
        statues = temple.pay_statues()
        self.assertEqual(statues, "֧��ʧ��")


if __name__ == "__main__":
    unittest.main()
