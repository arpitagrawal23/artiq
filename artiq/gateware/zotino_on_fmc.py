from migen.build.generic_platform import *

zotino_on_fmc = [
    # ("zotino_led_srclk", 0,
    #  Subsignal("p", Pins("LPC:LA00_CC_P")),
    #  Subsignal("n", Pins("LPC:LA00_CC_N")),
    #  IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
    #  ),
    # ("zotino_led_rclk", 0,
    #  Subsignal("p", Pins("LPC:LA04_P")),
    #  Subsignal("n", Pins("LPC:LA04_N")),
    #  IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
    #  ),
    # ("zotino_led_ser", 0,
    #  Subsignal("p", Pins("LPC:LA01_CC_P")),
    #  Subsignal("n", Pins("LPC:LA01_CC_N")),
    #  IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
    #  ),
    ("zotino_spi", 0,
        Subsignal("clk_p", Pins("LPC:LA00_CC_P")),
        Subsignal("clk_n", Pins("LPC:LA00_CC_N")),
        Subsignal("miso_p", Pins("LPC:LA01_CC_P")),
        Subsignal("miso_n", Pins("LPC:LA01_CC_N")),
        Subsignal("mosi_p", Pins("LPC:LA02_P")),
        Subsignal("mosi_n", Pins("LPC:LA02_N")),
        Subsignal("cs_n_p", Pins("LPC:LA03_P")),
        Subsignal("cs_n_n", Pins("LPC:LA03_N")),
        IOStandard("LVDS_25")
    ),
    ("zotino_ldac", 0,
     Subsignal("p", Pins("LPC:LA05_P")),
     Subsignal("n", Pins("LPC:LA05_N")),
     IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
     )
]
