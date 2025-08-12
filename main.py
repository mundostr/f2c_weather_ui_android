import asyncio
import struct
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from bleak import BleakClient, BleakScanner
from bleak.exc import BleakError

DEVICE_ADDRESS = "C8:F0:9E:F4:BA:DA"
CHARACTERISTIC_UUID = "00002a6e-0000-1000-8000-00805f9b34fb"

class WeatherUI(BoxLayout):
    temperature = StringProperty("N/A")
    pressure = StringProperty("N/A")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.client = None
        asyncio.ensure_future(self.connect_to_device())

    async def connect_to_device(self):
        try:
            await asyncio.sleep(1) # Add a small delay
            print("Scanning for devices...")
            devices = await BleakScanner.discover()
            print("Discovered devices:")
            for d in devices:
                print(d)
            
            device = await BleakScanner.find_device_by_address(DEVICE_ADDRESS, timeout=20.0)
            if not device:
                raise BleakError(f"A device with address {DEVICE_ADDRESS} could not be found.")
            
            self.client = BleakClient(device)
            await self.client.connect()
            print(f"Connected to {DEVICE_ADDRESS}")
            asyncio.ensure_future(self.read_data_loop())
        except Exception as e:
            print(f"Failed to connect: {e}")

    async def read_data_loop(self):
        """Periodically reads data from the BLE characteristic."""
        while self.client.is_connected:
            try:
                data = await self.client.read_gatt_char(CHARACTERISTIC_UUID)
                # Unpack the raw byte data into a single 4-byte float
                temp, = struct.unpack('f', data)
                self.temperature = f"{temp:.2f} °C"
                self.pressure = "N/A"
            except Exception as e:
                print(f"Failed to read data: {e}")
            await asyncio.sleep(2)

class WeatherApp(App):
    def build(self):
        return WeatherUI()

    def on_stop(self):
        if App.get_running_app().root.client:
            asyncio.ensure_future(App.get_running_app().root.client.disconnect())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = WeatherApp()
    loop.run_until_complete(app.async_run())
