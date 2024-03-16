#
#
import asyncio
found_devices = asyncio.run(Discover.discover())
[dev.alias for dev in found_devices]
