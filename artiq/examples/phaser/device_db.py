# The RTIO channel numbers here are for Phaser on KC705.

core_addr = "192.168.1.71"
lpc_start = 0
sawgstart = lpc_start + 36

device_db = {
    "core": {
        "type": "local",
        "module": "artiq.coredevice.core",
        "class": "Core",
        "arguments": {"host": core_addr, "ref_period": 5e-9/6}
    },
    "core_log": {
        "type": "controller",
        "host": "::1",
        "port": 1068,
        "command": "aqctl_corelog -p {port} --bind {bind} " + core_addr
    },
    "core_cache": {
        "type": "local",
        "module": "artiq.coredevice.cache",
        "class": "CoreCache"
    },
    "lpc_latch": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 0}
    },
    "lpc_clk": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 1}
    },
    "lpc_ser": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 2}
    },
    "lpc_eem0_0": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 3}
    },
    "lpc_eem0_1": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 4}
    },
    "lpc_eem0_2": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 5}
    },
    "lpc_eem0_3": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 6}
    },
    "lpc_eem0_4": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 7}
    },
    "lpc_eem0_5": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 8}
    },
    "lpc_eem0_6": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 9}
    },
    "lpc_eem0_7": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 10}
    },
    "lpc_eem1_0": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 11}
    },
    "lpc_eem1_1": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 12}
    },
    "lpc_eem1_2": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 13}
    },
    "lpc_eem1_3": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 14}
    },
    "lpc_eem1_4": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 15}
    },
    "lpc_eem1_5": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 16}
    },
    "lpc_eem1_6": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 17}
    },
    "lpc_eem1_7": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 18}
    },
    "lpc_eem2_0": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 19}
    },
    "lpc_eem2_1": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 20}
    },
    "lpc_eem2_2": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 21}
    },
    "lpc_eem2_3": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 22}
    },
    "lpc_eem2_4": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 23}
    },
    "lpc_eem2_5": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 24}
    },
    "lpc_eem2_6": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 25}
    },
    "lpc_eem2_7": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 26}
    },
    "lpc_eem3_0": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 27}
    },
    "lpc_eem3_1": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 28}
    },
    "lpc_eem3_2": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 29}
    },
    "lpc_eem3_3": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 30}
    },
    "lpc_eem3_4": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 31}
    },
    "lpc_eem3_5": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 32}
    },
    "lpc_eem3_6": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 33}
    },
    "lpc_eem3_7": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 34}
    },
    # support for FMC HPC AD9154 prototype board (4 channel SAWG)
    # using ARTIQ phaser demo
    "lpc_vhdci_i2c": {
        "type": "local",
        "module": "artiq.coredevice.i2c",
        "class": "TCA9548A",
        "arguments": {"address": 0x44}
    },
    "ttl_sma_diff": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": lpc_start + 35}
    },
    "sysref": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLInOut",
        "arguments": {"channel": sawgstart + 0}
    },
    "converter_spi": {
        "type": "local",
        "module": "artiq.coredevice.spi",
        "class": "NRTSPIMaster",
    },
    "ad9154_spi": {
        "type": "local",
        "module": "artiq.coredevice.ad9154_spi",
        "class": "AD9154",
        "arguments": {"spi_device": "converter_spi", "chip_select": 1}
    },
    "sawg0": {
        "type": "local",
        "module": "artiq.coredevice.sawg",
        "class": "SAWG",
        "arguments": {"channel_base": sawgstart + 1, "parallelism": 2}
    },
    "sawg1": {
        "type": "local",
        "module": "artiq.coredevice.sawg",
        "class": "SAWG",
        "arguments": {"channel_base": sawgstart + 11, "parallelism": 2}
    },
    "sawg2": {
        "type": "local",
        "module": "artiq.coredevice.sawg",
        "class": "SAWG",
        "arguments": {"channel_base": sawgstart + 21, "parallelism": 2}
    },
    "sawg3": {
        "type": "local",
        "module": "artiq.coredevice.sawg",
        "class": "SAWG",
        "arguments": {"channel_base": sawgstart + 31, "parallelism": 2}
    }
}
