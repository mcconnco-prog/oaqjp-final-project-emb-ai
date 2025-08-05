from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestDetectorAnalyzer(unittest.TestCase):
    def test_detector_analysis(self):
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1['dominant emotion'], "joy")

        result2 = emotion_detector("I am really mad about this")
        self.assertEqual(result2['dominant emotion'], "anger")

        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3['dominant emotion'], "disgust")

        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4['dominant emotion'], "sadness")

        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5['dominant emotion'], "fear")

unittest.main()
