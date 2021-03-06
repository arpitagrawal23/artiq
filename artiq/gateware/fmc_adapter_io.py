from migen.build.generic_platform import *

def get_fmc_adapter_io():
    r = []
    for connector in "LPC", "HPC":
        r += [
            (connector.lower() + "_config", 0,
             Subsignal("latch", Pins(connector + ":LA32_P")),
             Subsignal("clk", Pins(connector + ":LA32_N")),
             Subsignal("ser", Pins(connector + ":LA33_P")),
             IOStandard("LVCMOS25")
             ),
            ###############################################
            (connector.lower() + "_eem0", 0,
             Subsignal("p", Pins(connector + ":LA00_CC_P")),
             Subsignal("n", Pins(connector + ":LA00_CC_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem0", 1,
             Subsignal("p", Pins(connector + ":LA01_CC_P")),
             Subsignal("n", Pins(connector + ":LA01_CC_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem0", 2,
             Subsignal("p", Pins(connector + ":LA02_P")),
             Subsignal("n", Pins(connector + ":LA02_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem0", 3,
             Subsignal("p", Pins(connector + ":LA03_P")),
             Subsignal("n", Pins(connector + ":LA03_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem0", 4,
             Subsignal("p", Pins(connector + ":LA04_P")),
             Subsignal("n", Pins(connector + ":LA04_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem0", 5,
             Subsignal("p", Pins(connector + ":LA05_P")),
             Subsignal("n", Pins(connector + ":LA05_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem0", 6,
             Subsignal("p", Pins(connector + ":LA06_P")),
             Subsignal("n", Pins(connector + ":LA06_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem0", 7,
             Subsignal("p", Pins(connector + ":LA07_P")),
             Subsignal("n", Pins(connector + ":LA07_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            ###############################################
            (connector.lower() + "_eem1", 0,
             Subsignal("p", Pins(connector + ":LA08_P")),
             Subsignal("n", Pins(connector + ":LA08_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem1", 1,
             Subsignal("p", Pins(connector + ":LA09_P")),
             Subsignal("n", Pins(connector + ":LA09_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem1", 2,
             Subsignal("p", Pins(connector + ":LA10_P")),
             Subsignal("n", Pins(connector + ":LA10_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem1", 3,
             Subsignal("p", Pins(connector + ":LA11_P")),
             Subsignal("n", Pins(connector + ":LA11_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem1", 4,
             Subsignal("p", Pins(connector + ":LA12_P")),
             Subsignal("n", Pins(connector + ":LA12_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem1", 5,
             Subsignal("p", Pins(connector + ":LA13_P")),
             Subsignal("n", Pins(connector + ":LA13_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem1", 6,
             Subsignal("p", Pins(connector + ":LA14_P")),
             Subsignal("n", Pins(connector + ":LA14_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem1", 7,
             Subsignal("p", Pins(connector + ":LA15_P")),
             Subsignal("n", Pins(connector + ":LA15_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            ###############################################
            (connector.lower() + "_eem2", 0,
             Subsignal("p", Pins(connector + ":LA16_P")),
             Subsignal("n", Pins(connector + ":LA16_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem2", 1,
             Subsignal("p", Pins(connector + ":LA17_CC_P")),
             Subsignal("n", Pins(connector + ":LA17_CC_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem2", 2,
             Subsignal("p", Pins(connector + ":LA18_CC_P")),
             Subsignal("n", Pins(connector + ":LA18_CC_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem2", 3,
             Subsignal("p", Pins(connector + ":LA19_P")),
             Subsignal("n", Pins(connector + ":LA19_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem2", 4,
             Subsignal("p", Pins(connector + ":LA20_P")),
             Subsignal("n", Pins(connector + ":LA20_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem2", 5,
             Subsignal("p", Pins(connector + ":LA21_P")),
             Subsignal("n", Pins(connector + ":LA21_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem2", 6,
             Subsignal("p", Pins(connector + ":LA22_P")),
             Subsignal("n", Pins(connector + ":LA22_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem2", 7,
             Subsignal("p", Pins(connector + ":LA23_P")),
             Subsignal("n", Pins(connector + ":LA23_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            ###############################################
            (connector.lower() + "_eem3", 0,
             Subsignal("p", Pins(connector + ":LA24_P")),
             Subsignal("n", Pins(connector + ":LA24_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem3", 1,
             Subsignal("p", Pins(connector + ":LA25_P")),
             Subsignal("n", Pins(connector + ":LA25_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem3", 2,
             Subsignal("p", Pins(connector + ":LA26_P")),
             Subsignal("n", Pins(connector + ":LA26_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem3", 3,
             Subsignal("p", Pins(connector + ":LA27_P")),
             Subsignal("n", Pins(connector + ":LA27_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem3", 4,
             Subsignal("p", Pins(connector + ":LA28_P")),
             Subsignal("n", Pins(connector + ":LA28_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem3", 5,
             Subsignal("p", Pins(connector + ":LA29_P")),
             Subsignal("n", Pins(connector + ":LA29_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem3", 6,
             Subsignal("p", Pins(connector + ":LA30_P")),
             Subsignal("n", Pins(connector + ":LA30_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             ),
            (connector.lower() + "_eem3", 7,
             Subsignal("p", Pins(connector + ":LA31_P")),
             Subsignal("n", Pins(connector + ":LA31_N")),
             IOStandard("LVDS_25"), Misc("DIFF_TERM=TRUE")
             )
        ]
    return r

fmc_adapter_io = get_fmc_adapter_io()
