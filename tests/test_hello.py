from unittest import TestCase

from hello.hello import hello_world


class TestHello(TestCase):
    def test_hello_world(self):
        assert hello_world() == 'Hello, World!'
