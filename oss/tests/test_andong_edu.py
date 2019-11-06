from unittest import TestCase

from andong_edu import AndongEdu


class TestAndongEdu(TestCase):
    def test_hello_world_success(self):
        test_edu = AndongEdu()
        assert "Hello, test!" == test_edu.hello("test")

    def test_hello_world_failure(self):
        test_edu = AndongEdu()
        assert "Hello, test123!" != test_edu.hello("test")

    def test_ping_success(self):
        test_edu = AndongEdu()
        assert "pong" == test_edu.ping()

    def test_ping_failure(self):
        test_edu = AndongEdu()
        assert "pong1" != test_edu.ping()

    def test_add_success1(self):
        test_edu = AndongEdu()
        assert 4 == test_edu.add(2,2)

    def test_add_success2(self):
        test_edu = AndongEdu()
        assert 2 == test_edu.add(0,2)

    def test_add_success3(self):
        test_edu = AndongEdu()
        assert 3 == test_edu.add(1,2)
