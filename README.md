

# AI & IoT: Energy Efficient Light Automation

## Project Description

The **AI & IoT: Energy Efficient Light Automation** project is designed to create a smart lighting solution that dynamically adjusts the brightness of lights based on the ambient light in the environment. The system uses a Raspberry Pi microcontroller, light sensors (LDR), and a relay module to automatically control the brightness of an LED light bulb. By implementing real-time control and adaptability, the project enhances energy efficiency, reduces electricity usage, and improves overall user comfort. 

This intelligent system ensures that lights are only as bright as necessary, depending on the amount of natural light in the room, thus contributing to a smarter and more energy-efficient home.

## Features

- **Automatic Light Adjustment:** The system adjusts the light brightness based on ambient lighting conditions.
- **Energy Efficiency:** Minimizes electricity usage by automatically turning off or dimming lights when sufficient natural light is present.
- **User Comfort:** Maintains optimal lighting conditions, enhancing convenience and comfort for users.
- **Flexibility and Adaptability:** Dynamically responds to changes in room lighting, whether it’s too bright or too dark.
- **Maintenance and Longevity:** Helps prolong the life of the light bulb through predictive maintenance and reduced wear.

## Tech Stack

- **Microcontroller:** Raspberry Pi
- **Sensors:** Light Dependent Resistor (LDR) to detect light levels
- **Relay Module:** Controls the LED light bulb
- **Software:** Python (FastAPI for further expansion), CircuitPython (for hardware control)
- **Database (Optional):** MySQL or SQLite for logging light adjustments and power usage data

## Installation

### Prerequisites

- **Raspberry Pi (or similar microcontroller)**
- **Python 3.x** installed on Raspberry Pi
- **LDR (Light Dependent Resistor)** for light sensing
- **Relay Module** to control the LED light
- **LED Light Bulb** for adjustable lighting
- **Wires and Breadboard** for hardware connections
- **Libraries:**
  - `RPi.GPIO` for GPIO pin control
  - `time` for delay operations
  - `ngrok` (Optional) for remote access to the project

### Steps to Run Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ai-iot-light-automation.git
   cd ai-iot-light-automation
   ```

2. **Set Up the Hardware**
   - Connect the LDR sensor to the Raspberry Pi GPIO pins.
   - Connect the relay module to control the LED light bulb.
   - Make sure the power supply is properly connected.

3. **Install Dependencies**
   ```bash
   pip install RPi.GPIO
   ```

4. **Run the Python Script**
   ```bash
   python light_control.py
   ```

5. **Test the Setup**
   - Place the system in different lighting environments and monitor how the light automatically adjusts in response to the ambient light.

## Code Example

Here’s an example of the code used to control the light based on ambient light levels:

```python
import RPi.GPIO as GPIO
import time

LDR_PIN = 17  # GPIO pin where LDR is connected
LIGHT_PIN = 27  # GPIO pin to control the light

GPIO.setmode(GPIO.BCM)
GPIO.setup(LDR_PIN, GPIO.IN)
GPIO.setup(LIGHT_PIN, GPIO.OUT)

def read_light_sensor():
    return GPIO.input(LDR_PIN)

try:
    while True:
        light_level = read_light_sensor()
        if light_level == 0:  # Low ambient light
            GPIO.output(LIGHT_PIN, GPIO.HIGH)  # Turn on the light
        else:
            GPIO.output(LIGHT_PIN, GPIO.LOW)  # Turn off the light
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()
```

## Project Structure

```
📁 ai-iot-light-automation/
├── 📁 hardware/
│   └── circuit_diagram.png   # Circuit diagram for connecting hardware
├── 📁 scripts/
│   └── light_control.py       # Python script for light automation
├── README.md                  # Project documentation
├── requirements.txt           # List of dependencies
├── LICENSE                    # License file
```

## Usage

1. **Ambient Light Control:** The system automatically adjusts the brightness of the light based on the amount of ambient light in the room. 
2. **Real-time Monitoring:** Real-time control and monitoring of the light, with possible expansion to integrate data logging.
3. **Remote Control (Optional):** Use ngrok or any remote access solution to control the system from any location.

## Future Enhancements

- **Mobile App Integration:** Allow users to control the light through a mobile app or web interface.
- **Motion Detection:** Integrate motion sensors to control lights based on room occupancy.
- **Advanced AI Integration:** Use machine learning algorithms to predict user preferences and automatically adjust lighting conditions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please reach out to **Geethapriya S L** (mail to:s.l.geethapriya8888@gmail.com).

