# Python script kasa-api.py (this works with both smart strips and smart plugs):

import sys
import asyncio
from kasa import SmartPlug, SmartStrip

async def main():
	if len(sys.argv) != 4:
		print("Usage: python kasa-api.py type IP-address outlet-index")
		return

	device_type = sys.argv[1]
	ip_address = sys.argv[2]
	outlet_index = int(sys.argv[3])

	if device_type == "smartplug":
		await control_smart_plug(ip_address)
	elif device_type == "smartstrip":
		await control_smart_strip(ip_address, outlet_index)
	else:
		print(f"Unsupported device type: {device_type}")

async def control_smart_plug(ip_address):
	plug = SmartPlug(ip_address)

	try:
		await plug.update()

		# Retrieve the current state
		plug_state = plug.is_on

		# Turn off the plug
		await plug.turn_off()

		print(f"Turned off SmartPlug at {ip_address}")
		await asyncio.sleep(5)

		# Turn on the plug if it was previously on
		if plug_state:
			await plug.turn_on()

		print(f"Turned on SmartPlug at {ip_address}")
	except Exception as e:
		print(f"Failed to control SmartPlug at {ip_address}: {e}")

async def control_smart_strip(ip_address, outlet_index):
	strip = SmartStrip(ip_address)

	try:
		await strip.update()

		# Retrieve the current state of the specified child plug
		child_state = strip.children[outlet_index].is_on

		# Turn off the specified child plug
		await strip.children[outlet_index].turn_off()

		print(f"Turned off child plug {outlet_index} in SmartStrip at {ip_address}")
		await asyncio.sleep(5)

		# Turn on the child plug if it was previously on
		await strip.children[outlet_index].turn_on()

		print(f"Turned on child plug {outlet_index} in SmartStrip at {ip_address}")
	except Exception as e:
		print(f"Failed to control SmartStrip at {ip_address}: {e}")

# Run the asyncio event loop
asyncio.run(main())
