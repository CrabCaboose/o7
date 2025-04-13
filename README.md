# o7
The o7 orthosis created for MIT's CRE[AT]E Challenge.

# Temperature Monitor

Webpage for graphical UI of temperature from Raspberry Pi Pico

## Requirements

Raspberry Pi Pico W (MicroPython Firmware -- https://micropython.org/resources/firmware/RPI_PICO_W-20241129-v1.24.1.uf2, may or may not also work with other similar devices )

Device with wifi enabled (Such as a phone for viewing UI)

## Usage

Put main.py in filesystem (Must be named main.py)

Put index.html in filesystem (Again, must be named index.html)

Download Chart.js from their official website and store in the Raspberry Pi's filesystem -- https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js

Once supplied power, the Raspberry Pi should create a wifi hotspot named "o7" with the default password "123456789"

Upon connecting to said hotspot, you can connect to the IP 192.168.4.1 with a modern browser and view the GUI
