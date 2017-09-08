from artiq.experiment import *

class ZotinoTest(EnvExperiment):
    """ZotinoTest
    KC705-> FMC-VHDCI adapter -> VHDCI cable -> VHDCI carrier -> IDC cable-> 3U BNC
    """
    def build(self):
        print(self.__doc__)
        self.setattr_device("core")
        self.setattr_device("ttl_sma_diff")
        self.setattr_device("lpc_eem0_0")
        self.setattr_device("lpc_eem0_1")
        self.setattr_device("lpc_eem0_2")
        self.setattr_device("lpc_eem0_3")
        self.setattr_device("lpc_eem0_4")
        self.setattr_device("scheduler")


    @kernel
    def run(self):
        self.core.reset()
        delay(1 * ms)
        while True:
            self.ttl_sma_diff.pulse(1*us)
            self.lpc_eem0_0.pulse(1*us)
            self.lpc_eem0_1.pulse(1*us)
            self.lpc_eem0_2.pulse(1*us)
            self.lpc_eem0_3.pulse(1*us)
            self.lpc_eem0_4.pulse(1*us)
            delay(100*ms)


