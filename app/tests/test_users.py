import unittest
from app.models import User

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password = 'mypass')
    
    def test_password_setter(self)@run.command
def test():
    '''
    Run the unit test
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
:
        self.assertTrue(self.new_user.hash_pass is not None)
    
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
        
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('mypass'))