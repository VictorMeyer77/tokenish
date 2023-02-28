import unittest
from lib import encoder


class TestEncoder(unittest.TestCase):

    def test_apply_encoding_raises_error_when_encoding_is_unknown(self):
        with self.assertRaises(ValueError):
            encoder.apply_encoding("", "unknown")

    def test_apply_encoding_base64_returns_encoded_str(self):
        assert encoder.apply_encoding("hello world", "baSe64") == "aGVsbG8gd29ybGQ="

    def test_encode_expression_raises_error_when_tokens_are_malformed(self):
        with self.assertRaises(ValueError):
            encoder.encode_expression("&ENC[Hello", "base64")
        with self.assertRaises(ValueError):
            encoder.encode_expression("Hello]ODE&", "base64")

    def test_encode_expression_returns_encoded_target(self):
        assert encoder.encode_expression("&ENC[Hello]ODE&, World", "base64") == "SGVsbG8=, World"
        assert encoder.encode_expression("Hello, World", "base64") == "SGVsbG8sIFdvcmxk"

    def test_encode_expressions_returns_encoded_target(self):
        assert encoder.encode_expressions(["&ENC[Hello]ODE&, World", "Hello, World"], "base64") == \
               ["SGVsbG8=, World", "SGVsbG8sIFdvcmxk"]
