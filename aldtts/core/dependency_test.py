from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses import dataclass
from abc import abstractmethod

from alts.core.experiment_module import ExperimentModule


if TYPE_CHECKING:
    from alts.core.data.data_pools import ResultDataPools


class DependencyTest(ExperimentModule):

    @abstractmethod
    def test(self):
        raise NotImplementedError()
    
    @property
    def data_pools(self) -> ResultDataPools:
        return super().data_pools