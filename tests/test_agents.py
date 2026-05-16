import unittest
from agents.abstract_agent import AbstractAgent
class TestAgents(unittest.TestCase):
  def test_abstract_agent(self):
    with self.assertRaises(TypeError):
      AbstractAgent()
