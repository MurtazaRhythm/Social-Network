import unittest
from a5_300404973 import getCommonFriends, recommend, k_or_more_friends, maximum_num_friends, people_with_most_friends, average_num_friends, knows_everyone

# Example network for testing
test_network = [
    (1, [2, 3]),
    (2, [1, 3]),
    (3, [1, 2, 4]),
    (4, [3])
]

class TestSocialNetwork(unittest.TestCase):

    def test_getCommonFriends(self):
        self.assertEqual(getCommonFriends(1, 2, test_network), [3])
        self.assertEqual(getCommonFriends(1, 4, test_network), [3])
        self.assertEqual(getCommonFriends(2, 4, test_network), [3])

    def test_recommend(self):
        # For user 1, recommend should be 4 (most common friends not already connected)
        self.assertEqual(recommend(1, test_network), 4)
        # User 4 should be recommended 1 or 2 or 3 depending on logic
        self.assertIn(recommend(4, test_network), [1, 2])

    def test_k_or_more_friends(self):
        self.assertEqual(k_or_more_friends(test_network, 2), 3)
        self.assertEqual(k_or_more_friends(test_network, 3), 1)

    def test_maximum_num_friends(self):
        self.assertEqual(maximum_num_friends(test_network), 3)

    def test_people_with_most_friends(self):
        self.assertEqual(people_with_most_friends(test_network), [3])

    def test_average_num_friends(self):
        self.assertAlmostEqual(average_num_friends(test_network), 2.0)

    def test_knows_everyone(self):
        self.assertTrue(knows_everyone(test_network))
        # Create a network where someone knows everyone
        network2 = [(1, [2,3]), (2, [1,3]), (3, [1,2])]
        self.assertTrue(knows_everyone(network2))

if __name__ == '__main__':
    unittest.main()
