import unittest
import os
from lib.result_writer import ResultWriter


class TestResultWriter(unittest.TestCase):

    def test_result_writer_write_rows_in_different_files(self):
        output_path = "test/resources/output"
        result_writer = ResultWriter(output_path, 3)
        for i in range(0, 99):
            result_writer.write_row(str(i))
        result_writer.close_file()

        for i in range(0, 33):
            file = open(output_path + "/part_{}.txt".format(i), "r")
            lines = file.readlines()
            file.close()
            os.remove(output_path + "/part_{}.txt".format(i))
            assert lines[0] == "{}\n".format(i * 3)
            assert lines[1] == "{}\n".format(i * 3 + 1)
            assert lines[2] == "{}\n".format(i * 3 + 2)
