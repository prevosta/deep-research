import unittest

from deep_research import module  # changed import from my_package to deep_research


class TestModule(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(module.hello(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()
