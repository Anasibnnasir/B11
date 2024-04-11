from django.test import TestCase

# Create your tests here.
def demo(str1,str2):
    return str1+str2
class Testdemo(TestCase):
    def test_concate(self):
        self.assertequals(demo("hello","world") ("helloworld"))