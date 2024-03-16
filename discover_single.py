# https://python-kasa.readthedocs.io/en/latest/discover.html
#
import asyncio
from kasa import Discover, Credentials

async def main():
    device = await Discover.discover_single(
        "127.0.0.1",
        credentials=Credentials("myusername", "mypassword"),
        discovery_timeout=10
    )

    await device.update()  # Request the update
    print(device.alias)  # Print out the alias

    devices = await Discover.discover(
        credentials=Credentials("myusername", "mypassword"),
        discovery_timeout=10
    )
    for ip, device in devices.items():
        await device.update()
        print(device.alias)

if __name__ == "__main__":
    asyncio.run(main())
