"""
 测试数据共享文件 conftest.py
"""

import pytest


@pytest.fixture(scope="class")
def login():
    # 使用pytest fixture 实现 setup 和 teardown
    print("登录")
    yield {"token":"1045645343565sldjhncundm"}
    print("登出")


@pytest.fixture(scope="class")
def db_connect():
    print("连接数据库")
    yield
    print("断开数据库")
