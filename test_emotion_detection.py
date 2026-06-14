import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_joy(self):
        result = emotion_detector("I am so happy and excited today!")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_sadness(self):
        result = emotion_detector("I feel very sad and depressed.")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_anger(self):
        result = emotion_detector("I am really angry about this situation.")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_fear(self):
        result = emotion_detector("I am scared and worried about the future.")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_disgust(self):
        result = emotion_detector("I feel disgusted by this.")
        self.assertEqual(result["dominant_emotion"], "disgust")

if __name__ == "__main__":
    unittest.main()