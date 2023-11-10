# MicroPython WebServer (MWS)

![MWS Logo](https://github.com/NerdCodex/esp32-mws/assets/81899310/820cf4c9-2871-4c83-b78f-dc935618befa)

## Project Description

MicroPython WebServer (MWS) is a specialized web framework designed specifically for the ESP32 microcontroller. The primary goal of the framework is to facilitate the hosting of HTML webpages on the ESP32, allowing for seamless handling of incoming requests and rendering of HTML templates. MWS caters to the unique requirements of the ESP32, providing a user-friendly and efficient solution for web hosting and development.

## Features

- **ESP32 Compatibility:** Tailored to work seamlessly with the ESP32 microcontroller.
  
- **HTML Webpage Hosting:** Enables hosting of HTML webpages directly on the ESP32.

- **Request Handling:** Facilitates easy handling of incoming requests from web clients.

- **Template Rendering:** Provides functionality for rendering HTML templates for dynamic content.

## Project Components

1. **ESP32 Microcontroller:** The core hardware platform for running the MicroPython WebServer.

2. **SD Card Slot:** Utilized for storing HTML webpages and templates.

3. **Jumper Wires:** Used for connecting the ESP32 with the SD card module.

4. **MWS Folder:** Contains essential files for the MicroPython WebServer, including the webserver logic and template rendering.

## Setup Instructions

### Step 1: Connect ESP32 with the SD Card Module

Connect the ESP32 with the SD card module using the following table:

| ESP32 Pin | SD Card Slot Pin |
|-----------|-------------------|
| GND       | GND               |
| VIN       | VCC               |
| D13       | MOSO              |
| D12       | MOSI              |
| D14       | SCK               |
| D27       | CS                |

Double-check the connections with the documentation for your specific ESP32 board and SD card slot.

### Step 2: Set up SD Card and ESP32

1. Connect the SD card to your computer and copy the **MWS folder** to the SD card.

2. Install Thonny on your computer and connect your ESP32 to it.
   
3. Include the `sdcard.py` file to esp32, which serves as the driver for the ESP32 SD card slot.

4. Perform necessary firmware updates and edit the `boot.py` file:


```python
# Add this to boot.py
import os
from machine import Pin, SoftSPI
from sdcard import SDCard

# Set up SoftSPI for SD card communication
spisd = SoftSPI(-1, miso=Pin(13), mosi=Pin(12), sck=Pin(14))

# Initialize the SD card
sd = SDCard(spisd, Pin(27))

# Mount the SD card filesystem
vfs = os.VfsFat(sd)
os.mount(vfs, '/sd')
```
### Step 3: Create `main.py` file
Create a main.py file and add the following code:
```python
import usocket as socket
import network, esp, gc
import sys

# WiFi credentials
ssid = "ESP32-MWS"
passwd = ""

# Configure ESP32 as an access point (AP)
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=passwd)

# Wait for AP to become active
while ap.active() == False:
    pass

# Print the assigned IP address of the AP
print("Access Point IP:", ap.ifconfig()[0])

# Add the "/sd" path to the system path for SD card access
sys.path.append("/sd")

try:
    # Import necessary modules from the EWS package
    from MWS.webserver import *
    from MWS.render_template import *

except ImportError:
    print("Unable to Import EWS Web Server.")

# Create an instance of the EWS web server
App = mws()

# Define a route for the home page
def home(urlargs):
    name = urlargs.get("{name}")
    return render("/sd/templates/index.html", name=name)

# Add the home route to the web server
App.add_route("/{name}", home)

# Run the web server on the specified IP address and port 80
if __name__ == "__main__":
    App.run(host=ap.ifconfig()[0], port=80)
```
### Step 4: Request with Browser
Now, after running the script, you'll see the "Web Server URL" printed in the console, indicating the address where you can access the web server from your browser. Open a web browser and enter this URL to connect to the ESP32 web server.

-----------------------------------------------------------------------
## Contribution

Contributions to the MicroPython WebServer project are welcome. Please refer to the project repository for guidelines on how to contribute.

## Note
This repository, maintained by a college student from India, houses a web framework created in an unprofessional way. Some functions are intended to be very basic, reflecting the humble spark that ignited this project when the student first learned about the ESP32 microcontroller.
