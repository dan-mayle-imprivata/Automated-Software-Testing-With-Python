from unittest import TestCase
from post import Post


class PostTest(TestCase):  # right click on this class then run unit test
    def test_create_post(self):  # test methods must start with test_
        p = Post('Test', 'Test Content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)
