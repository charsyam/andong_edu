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
