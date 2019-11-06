from unittest import TestCase

from andong_edu import AndongEdu


class TestAndongEdu(TestCase):
    def test_hello_world(self):
        test_edu = AndongEdu()
        assert "Hello, test!" == test_edu.hello("test")

    def test_failure(self):
        assert "Hello" == "World"
