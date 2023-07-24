from __future__ import annotations
from typing import TYPE_CHECKING

from dataclasses import dataclass

from alts.core.experiment_module import ExperimentModule
from alts.core.subscriber import ExpModSubscriber


if TYPE_CHECKING:
    from alts.core.subscribable import Subscribable
    from alts.core.data.data_pools import ResultDataPools



@dataclass
class DependencyTest(ExperimentModule, ExpModSubscriber):

    def experiment_update(self, subscription: Subscribable):
        super().experiment_update(subscription)
        t,p = self.test()

    def test(self):
        raise NotImplementedError()
    
    @property
    def data_pools(self) -> ResultDataPools:
        return super().data_pools