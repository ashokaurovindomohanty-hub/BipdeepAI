from abc import ABC, abstractmethod
class AbstractAgent(ABC):
  @abstractmethod
  def act(self, state):
    pass
  @abstractmethod
  def learn(self, reward):
    pass
