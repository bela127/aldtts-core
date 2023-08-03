from __future__ import annotations
from abc import abstractproperty
from typing import TYPE_CHECKING

from dataclasses import dataclass

import numpy as np
from alts.core.experiment_module import ExperimentModule
from alts.core.query.queryable import Queryable
from alts.core.configuration import init

if TYPE_CHECKING:
    from typing_extensions import Self #type: ignore
    from alts.core.experiment_modules import ExperimentModules
    from alts.core.data_sampler import DataSampler
    from aldtts.core.two_sample_test import TwoSampleTest



@dataclass
class TestInterpolator(ExperimentModule, Queryable):
    test: TwoSampleTest = init()

    def post_init(self):
        super().post_init()
        self.test = self.test()