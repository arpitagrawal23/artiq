from artiq.experiment import *

class ZotinoTestDAC(EnvExperiment):
    def build(self):
        print(self.__doc__)
        self.setattr_device("core")
        # self.setattr_device("zotino_ldac")
        # self.setattr_device("zotino_spi")
        self.setattr_device("zotino_dac")
        self.setattr_device("diff1")
        self.setattr_device("diff2")

    @kernel
    def run(self):
        self.core.reset()
        delay(1*ms)
        self.zotino_dac.setup_bus(write_div=128, read_div=128)
        delay(100*ms)
        self.zotino_dac.write_offsets()
        delay(100*ms)
        # self.zotino_spi.set_config_mu(32, 4, 7)
        # self.zotino_spi.set_xfer(1, 24, 0)
        delay(100*ms)
        while(True):
            self.diff1.on()
            self.diff2.on()
            self.zotino_dac.set([0x7fff for i in range(32)])
            # self.zotino_spi.set_config_mu(32, 4, 7)
            # self.zotino_spi.set_xfer(1, 24, 0)
            # self.zotino_spi.write(0x55555500)
            delay(10*ms)
            self.diff1.off()
            self.diff2.off()
            self.zotino_dac.set([0x0000 for i in range(32)])
            # self.zotino_spi.set_config_mu(32, 4, 7)
            # self.zotino_spi.set_xfer(1, 24, 0)
            # self.zotino_spi.write(0xcccccc00)
            delay(10*ms)
