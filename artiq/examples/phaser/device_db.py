# The RTIO channel numbers here are for Phaser on KC705.

core_addr = "192.168.1.71"
zotino_start = -3
sawgstart = zotino_start + 6

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
    # "zotino_led_srclk": {
    #     "type": "local",
    #     "module": "artiq.coredevice.ttl",
    #     "class": "TTLOut",
    #     "arguments": {"channel": zotino_start + 0}
    # },
    # "zotino_led_rclk": {
    #     "type": "local",
    #     "module": "artiq.coredevice.ttl",
    #     "class": "TTLOut",
    #     "arguments": {"channel": zotino_start + 1}
    # },
    # "zotino_led_ser": {
    #     "type": "local",
    #     "module": "artiq.coredevice.ttl",
    #     "class": "TTLOut",
    #     "arguments": {"channel": zotino_start + 2}
    # },
    "zotino_ldac": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": zotino_start + 3}
    },
    "zotino_spi": {
        "type": "local",
        "module": "artiq.coredevice.spi",
        "class": "SPIMaster",
        "arguments": {"channel": zotino_start + 4}
    },
    "zotino_dac": {
        "type": "local",
        "module": "artiq.coredevice.ad5360",
        "class": "AD5360",
        "arguments": {"spi_device": "zotino_spi", "ldac_device": "zotino_ldac"}
    },
    "diff1": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": zotino_start + 5}
    },
    "diff2": {
        "type": "local",
        "module": "artiq.coredevice.ttl",
        "class": "TTLOut",
        "arguments": {"channel": zotino_start + 6}
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
