from dataclasses import dataclass

from alts.core.experiment_module import ExperimentModule


@dataclass
class DependencyMeasure(ExperimentModule):
    
    def apply(self, samples):
        raise NotImplementedError()
