import pytest
import mock_project
from mock_project import some_file 
import random


# SAMPLE ONE
def fake_random():
    return 1

def fake_amplify_10(x):
    return  int(x/10)

class TestA:
    def test_01(self, mocker):
        mocker.patch.object(some_file,"random",fake_random)
        assert some_file.generate_random() == 1

    def test_02(self, mocker):
        mocker.patch("mock_project.some_file.random",fake_random)
        assert some_file.generate_random() == 1


#     def test_02(self, mocker):

#         def fake_random():
#             return 1

#         with pytest.raises(Exception) as excinfo:
#             mocker.patch.object("some_file","random",fake_random)
#             assert some_file.generate_random() == 1
#         print(excinfo.value.args[0])
        

#     def test_03(self, mocker):

#         def fake_random():
#             return 1

#         mocker.patch.object(some_file,"random",fake_random)
#         assert some_file.generate_random() == 1
#         print("pass")


class TestB:

    def test_01(self, mocker):
        mocker.patch.object(some_file,"amplify_10",fake_amplify_10)
        assert some_file.process_10(10) == 1
        print("amplify test")

class TestC:

    def test_01(self, mocker):
        mock_MeCab = mocker.Mock()
        mock_MeCab_Tagger = mocker.Mock()

        def fake_parse(x):
            return "a b c"
        mock_MeCab_Tagger.parse = fake_parse
        
        mock_MeCab.Tagger = mocker.Mock(return_value=mock_MeCab_Tagger)

        mocker.patch.object(some_file,"MeCab",mock_MeCab)
        
        res = some_file.parse_sent("ハロー、今日わ")
        assert res == ["a","b","c"]
