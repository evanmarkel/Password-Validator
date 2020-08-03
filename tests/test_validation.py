import sys
from unittest import TestCase

sys.path.append(".")
from password_validator import Validate


class TestNotAscii(TestCase):
    """ Use custom configuration in our test directory
    to test edge cases of candidate passwords
    """
    def test_foreign_characters(self):
        common_password = []
        values = ['dfdflpk.-øåå','6dfjksdklfjaks;^^&&&',',ัะเ่า']

        val = Validate(values, common_password, 8, 64)

        self.assertEqual(val('dfdflpk.-øåå', common_password), 'dfdflpk.-***')
        self.assertEqual(val('6dfjksdklfjæaks;^^&&&', common_password), '6dfjksdklfj*aks;^^&&&')
        self.assertEqual(val('ะเ่า', common_password),'****')



if __name__ == '__main__':
    unittest.main()