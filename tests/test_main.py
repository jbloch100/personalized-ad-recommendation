import unittest
from src.main import Recommender

class TestRecommender(unittest.TestCase):
    def test_recommendation(self):
        r = Recommender()
        r.record_interaction('u1', 'ad1')
        r.record_interaction('u1', 'ad2')
        r.record_interaction('u2', 'ad2')
        r.record_interaction('u2', 'ad3')
        r.record_interaction('u3', 'ad3')
        r.record_interaction('u3', 'ad4')
        recs = r.recommend('u1')
        self.assertIsInstance(recs, list)
        self.assertTrue(all(item not in {'ad1', 'ad2'} for item in recs))

if __name__ == '__main__':
    unittest.main()
