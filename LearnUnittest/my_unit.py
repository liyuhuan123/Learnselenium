import unittest

class MyUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass:在每个类之前执行一次，如：创建数据库，生成日志对象")

    def setUp(self):
        print("\nsetUp:在测试用例之前的准备工作，如：打开浏览器，加载网页，注意：执行所有测试用例前都会执行一次")

    def tearDown(self) -> None:
        print("tearDown：在每个测试用例结束之后的扫尾的工作，如：关闭浏览器")

    @classmethod  # 装饰器，必须加上
    def tearDownClass(cls) -> None:
        print("tearDownClass:在每个类之后执行一次，如关闭数据库连接，销毁日志对象")