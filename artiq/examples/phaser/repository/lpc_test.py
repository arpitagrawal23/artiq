from artiq.experiment import *

class LpcTest(EnvExperiment):
    def build(self):
        print(self.__doc__)
        self.setattr_device("core")
        self.setattr_device("ttl_sma_diff")
        self.setattr_device("lpc_eem3_0")
        self.setattr_device("lpc_eem3_1")

    @kernel
    def run(self):
        self.core.reset()
        delay(1*ms)
        while True:
            self.ttl_sma_diff.pulse(1*us)
            self.lpc_eem3_0.pulse(1*us)
            self.lpc_eem3_1.pulse(1*us)
            delay(1*ms)
