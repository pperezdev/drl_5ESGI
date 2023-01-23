from .test_agent import TestAgentMethods
import unittest

def get_only_test(unit_test_class:unittest.TestCase) -> list:
    return [str(x) for x in dir(unit_test_class) if x.startswith("test")]

def add_test(unit_test_class:unittest.TestCase, suite:unittest.TestSuite):
    [suite.addTest(unit_test_class(fct)) for fct in get_only_test(unit_test_class)]
    
def suite() -> unittest.TestSuite:
    suite = unittest.TestSuite()
    add_test(TestAgentMethods, suite)
    return suite

def test_execute():
    runner = unittest.TextTestRunner()
    runner.run(suite())