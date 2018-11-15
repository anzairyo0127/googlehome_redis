'''
単体テストプログラムになります。
'''

import unittest
import page


class PyUnitTest(unittest.TestCase):
    def setUp(self):
        '''
        単体テスト用のセットアップです。
        PythonのUnittestモジュール用の特殊メソッドになります。
        キャメル型の名称なのはそれが由来です。
        Flaskでテストを行う場合はこちらが必要になります。
        '''
        self.app = page.app.test_client()

    def test_index(self):
        '''
        index()メソッドのテストです。
        「/」ページをテストしています。
        '''
        response = self.app.get('/')
        self.assertEqual(b'Hello, World', response.data)


if __name__ == '__main__':
    unittest.main(exit=False)
