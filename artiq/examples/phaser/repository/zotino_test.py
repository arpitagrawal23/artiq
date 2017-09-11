from artiq.experiment import *

class ZotinoTest(EnvExperiment):
    def build(self):
        print(self.__doc__)
        self.setattr_device("core")
        self.setattr_device("lpc_eem0_0")
        self.setattr_device("lpc_eem0_1")
        self.setattr_device("lpc_eem0_4")

    @kernel
    def SN74LV595A_putData(self, srclk, rclk, ser, data):
        dt = 1*ms;
        srclk.off()
        rclk.off()
        delay(dt)
        for i in range(8):
            if data & 1 == 0:
                ser.off()
            else:
                ser.on()
            srclk.off()
            delay(dt)
            srclk.on()
            delay(dt)
            data = data >> 1
        srclk.off()
        rclk.off()
        delay(dt)
        rclk.on()
        delay(dt)
        rclk.off()


    @kernel
    def run(self):
        self.core.reset()
        delay(1*ms)
        while True:
            self.SN74LV595A_putData(self.lpc_eem0_0, self.lpc_eem0_4, self.lpc_eem0_1, 0xAA)
            delay(500*ms)
            self.SN74LV595A_putData(self.lpc_eem0_0, self.lpc_eem0_4, self.lpc_eem0_1, 0x55)
            delay(500*ms)
