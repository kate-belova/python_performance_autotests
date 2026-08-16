from abc import ABC, abstractmethod

from seeds.builder import SeedsBuilder
from seeds.dumps import save_seeds_result, load_seeds_result
from seeds.schemas.plan import SeedsPlan
from seeds.schemas.result import SeedsResult


class SeedsScenario(ABC):
    def __init__(self, builder: SeedsBuilder):
        self.builder = builder

    @property
    @abstractmethod
    def plan(self) -> SeedsPlan:
        pass

    @property
    @abstractmethod
    def scenario(self) -> str:
        pass

    def save(self, result: SeedsResult) -> None:
        save_seeds_result(result=result, scenario=self.scenario)

    def load(self) -> SeedsResult:
        return load_seeds_result(scenario=self.scenario)

    def build(self) -> None:
        result = self.builder.build(self.plan)
        self.save(result)
