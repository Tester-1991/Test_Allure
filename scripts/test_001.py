import pytest,allure

class Test_Abc:

    @allure.step(title="第一个测试")
    def test_abc_001(self):
        allure.attach("这是一个描述", "试一下")
        assert 1

    @allure.issue("http://www.163.com")
    @allure.testcase("http://wwww.baidu.com")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_abc_002(self):
        allure.attach("这是一个描述", "试一下")
        assert 0
