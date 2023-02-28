import unittest
from lib import tokenizer


class TestEncoder(unittest.TestCase):

    def test_get_file_lines_returns_list_of_file_lines(self):
        lines = tokenizer.get_file_lines("test/resources/input/usernames/1.txt")
        assert lines == ["admin", "root", "user"]

    def test_get_all_file_paths_returns_list_of_paths(self):
        file_paths = tokenizer.get_all_file_paths("test/resources/input/usernames")
        file_paths.sort()
        assert file_paths == ["test/resources/input/usernames/1.txt", "test/resources/input/usernames/2.txt"]

    def test_gather_tokens_returns_list_of_tokens(self):
        token_paths = ["test/resources/input/usernames",
                       "test/resources/input/passwords",
                       "test/resources/input/links/1.txt"]
        token_lists = tokenizer.gather_tokens(token_paths)
        target_list = [["user1", "user2", "admin", "root", "user"],
                       ["abcd", "efgh", "1234", "6712"],
                       ["test.com", "test.fr"]]
        token_lists.sort()
        target_list.sort()
        print(token_lists)
        assert token_lists == target_list

    def test_fill_tokens_raises_error_when_token_missing(self):
        token_lists = [["userA", "userB"], ["pwd1", "pwd2", "pwd3"], ["..."]]
        pattern = "Auth: &TOKEN_0&:&TOKEN_1&"
        with self.assertRaises(ValueError):
            tokenizer.fill_tokens(token_lists, pattern)

    def test_fill_tokens_returns_list_of_tokenized_combinations(self):
        token_lists = [["userA", "userB"], ["pwd1", "pwd2", "pwd3"], ["..."]]
        pattern = "Auth: &TOKEN_0&:&TOKEN_1&&TOKEN_2&"
        assert tokenizer.fill_tokens(token_lists, pattern) == \
               ["Auth: userA:pwd1...", "Auth: userA:pwd2...", "Auth: userA:pwd3...", "Auth: userB:pwd1...",
                "Auth: userB:pwd2...", "Auth: userB:pwd3..."]
