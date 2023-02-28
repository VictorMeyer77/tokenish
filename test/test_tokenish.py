import unittest
import tokenish
import os
from lib.result_writer import ResultWriter


class TestMain(unittest.TestCase):

    def test_main_write_filled_expressions_when_output_is_defined(self):
        token_paths = ["test/resources/input/links/1.txt",
                       "test/resources/input/usernames",
                       "test/resources/input/passwords"]
        tokenish.main("Link: &ENC[test]ODE& &TOKEN_0& - Auth:&TOKEN_1&/&TOKEN_2&", token_paths,
                      None, ResultWriter("test/resources/output", 10000))
        output_path = "test/resources/output/part_0.txt"
        output = open(output_path, "r")
        lines = output.readlines()
        output.close()
        assert len(lines) == 40
        for line in lines:
            assert "&TOKEN" not in line
        os.remove(output_path)

    def test_main_write_filled_expressions_when_encoding_and_output_is_defined(self):
        token_paths = ["test/resources/input/links/1.txt",
                       "test/resources/input/usernames",
                       "test/resources/input/passwords"]
        tokenish.main("Link: &ENC[test]ODE& &TOKEN_0& - Auth:&TOKEN_1&/&TOKEN_2&", token_paths,
                      "base64", ResultWriter("test/resources/output", 10000))
        output_path = "test/resources/output/part_0.txt"
        output = open(output_path, "r")
        lines = output.readlines()
        output.close()
        assert len(lines) == 40
        for line in lines:
            assert "dGVzdA==" in line
            assert "&TOKEN" not in line
        os.remove(output_path)

    def test_parse_args_return_all_parameters(self):
        assert tokenish.parse_args(["pattern"]) == ("pattern", [], None, None)
        assert tokenish.parse_args(["pattern", "-t", "/path/tokenA/", "/path/tokenB.txt"]) == \
               ("pattern", ["/path/tokenA/", "/path/tokenB.txt"], None, None)
        assert tokenish.parse_args(["pattern", "-t", "/path/tokenA/", "/path/tokenB.txt", "-e", "base64"]) == \
               ("pattern", ["/path/tokenA/", "/path/tokenB.txt"], "base64", None)
        args_with_output = tokenish.parse_args(["pattern", "-o", "/output"])
        assert args_with_output[3].directory_path == ResultWriter("/output", 10000).directory_path
        assert args_with_output[3].max_row_per_file == ResultWriter("/output", 10000).max_row_per_file
        args_with_output_and_max_rows = tokenish.parse_args(["pattern", "-o", "/output", "-om", "50"])
        assert args_with_output_and_max_rows[3].max_row_per_file == ResultWriter("/output", 50).max_row_per_file
