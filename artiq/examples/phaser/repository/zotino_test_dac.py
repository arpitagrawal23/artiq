from artiq.experiment import *

class ZotinoTestDAC(EnvExperiment):
    def build(self):
        print(self.__doc__)
        self.setattr_device("core")
        self.setattr_device("zotino_dac")

    @kernel
    def run(self):
        self.core.reset()
        delay(1*ms)
        self.zotino_dac.setup_bus(write_div=30, read_div=40)
        self.zotino_dac.write_offsets()
        # self.zotino_dac.set([i << 10 for i in range(40)])
        while(True):
            self.zotino_dac.set([0x7fff for i in range(40)])
            delay(1*ms)
            self.zotino_dac.set([0x0000 for i in range(40)])
            delay(1*ms)
