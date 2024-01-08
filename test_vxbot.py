import unittest
from vxbot import contains_twitter_url, extract_username_and_hash, create_vxtwitter_url

class TestVxBot(unittest.TestCase):
    def test_contains_twitter_url(self):
        self.assertTrue(contains_twitter_url('aaa https://twitter.com/test/status/1234567890'))
        self.assertTrue(contains_twitter_url('https://x.com/test/status/1234567890'))
        self.assertFalse(contains_twitter_url('https://example.com/test/status/1234567890'))

    def test_extract_username_and_hash(self):
        username, tweet_id = extract_username_and_hash('bbb https://twitter.com/test/status/1234567890')
        self.assertEqual(username, 'test')
        self.assertEqual(tweet_id, '1234567890')

    def test_create_vxtwitter_url(self):
        url = create_vxtwitter_url('test', '1234567890')
        self.assertEqual(url, 'https://vxtwitter.com/test/status/1234567890')

if __name__ == '__main__':
    unittest.main()