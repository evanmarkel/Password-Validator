import sys
import unittest

sys.path.append(".")
from password_validator import Validate


class TestNotAscii(unittest.TestCase):
    """ Use strings to test edge cases of candidate passwords
    Note: Validate class print changed to return output for testing
    """
    def test_foreign_characters(self):
        common_password = []
        values = 'dfdflpk.-øåå','6dfjksdklfjaks;^^&&&',',ัะเ่า'

        val = Validate(values, common_password, 8, 64)

        self.assertEqual(val('dfdflpk.-øåå', common_password), 'dfdflpk.-***')
        self.assertEqual(val('6dfjksdklfjæaks;^^&&&', common_password), '6dfjksdklfj*aks;^^&&&')
        self.assertEqual(val('ะเ่า', common_password),'****')


class TestLengthOutOfRange(unittest.TestCase):
    """ Test passwords out of range of the length criteria
    """
    def test_too_short(self):
        common_password = []
        values = '','lol','seven77'

        val = Validate(values, common_password, 8, 64)

        self.assertEqual(val('', common_password), '  -> Error: Too Short')
        self.assertEqual(val('lol', common_password), 'lol  -> Error: Too Short')
        self.assertEqual(val('seven77', common_password),'seven77 -> Error: Too Short.')

    def test_too_long(self):
        common_password = []
        values = '12345678910111213141516171819202122232425262728293031323334353637383940',\
                '..............................................................................................................'

        val = Validate(values, common_password, 8, 64)

        self.assertEqual(val('12345678910111213141516171819202122232425262728293031323334353637383940', common_password),\
            '12345678910111213141516171819202122232425262728293031323334353637383940  -> Error: Too Long')
        self.assertEqual(val('..............................................................................................................'\
            , common_password), '..............................................................................................................-> Error: Too Short')
        self.assertEqual(val('seven77', common_password),'seven77 -> Error: Too Short.')


if __name__ == '__main__':
    unittest.main()