import unittest
from unittest.mock import patch
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [
                {"emotion": {
                    "anger": 0.01,
                    "disgust": 0.02,
                    "fear": 0.03,
                    "joy": 0.90,
                    "sadness": 0.04
                }}
            ]
        }

        response = emotion_detector("I am glad this happened")
        self.assertEqual(response["dominant_emotion"], "joy")


    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [
                {"emotion": {
                    "anger": 0.90,
                    "disgust": 0.02,
                    "fear": 0.03,
                    "joy": 0.01,
                    "sadness": 0.04
                }}
            ]
        }

        response = emotion_detector("I am mad")
        self.assertEqual(response["dominant_emotion"], "anger")


if __name__ == "__main__":
    unittest.main()