# REQUIRES: pip3 install python-kasa
#
import asyncio
strip = SmartStrip("127.0.0.1")
asyncio.run(strip.update())
strip.alias
