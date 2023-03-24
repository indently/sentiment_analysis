import unittest
from main import get_mood, Mood


class TestMoodAnalysis(unittest.TestCase):

    def test_get_mood(self):
        test_cases = [
            {
                'input_text': 'I love this place! The staff is so friendly and helpful.',
                'threshold': 0.3,
                'expected_emoji': '😊',
            },
            {
                'input_text': 'This is the worst experience I\'ve ever had. I can\'t believe how terrible the service is.',
                'threshold': 0.3,
                'expected_emoji': '😠',
            },
            {
                'input_text': 'It\'s an average place, not too bad but not too good either.',
                'threshold': 0.3,
                'expected_emoji': '😐',
            },
        ]

        for case in test_cases:
            input_text = case['input_text']
            threshold = case['threshold']
            expected_emoji = case['expected_emoji']

            mood = get_mood(input_text, threshold=threshold)
            self.assertIsInstance(mood, Mood)
            self.assertEqual(mood.emoji, expected_emoji)


if __name__ == '__main__':
    unittest.main()
