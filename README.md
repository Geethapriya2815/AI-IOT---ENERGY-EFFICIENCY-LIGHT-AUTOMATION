**AI & IoT: Energy Efficient Light Automation**

_**Overview**_

The Energy Efficient Light Automation project aims to create an adaptive lighting solution that automatically adjusts light intensity based on environmental conditions, such as the natural light in a room. This system helps to minimize electricity wastage, enhance user comfort, and extend the life of lighting equipment.

_**Key Features:**_

**1.**Energy Efficiency:**** Adjusts light intensity based on natural light availability, reducing energy consumption.

****2.User Comfort:**** Provides appropriate lighting levels for different tasks and user preferences.

**3.Adaptability:** Dynamically responds to changing environmental conditions.

**4.Maintenance and Longevity:** Helps increase the performance and life of the light bulb through predictive maintenance.

_**Hardware Requirements:**_

**1.Raspberry Pi (or similar microcontroller):** The brain of the system to run the control logic.

****2.LDR (Light Dependent Resistor):**** Light sensor used to detect the ambient light level in the room.

**3.Relay Module:** Controls the power of the light bulb based on the sensor readings.

**4.LED Light Bulb:** For efficient lighting.

**5.Power Supply:** Required for the Raspberry Pi and relay module.

**6.Connecting Wires:** For connecting the components to the Raspberry Pi.

_**Software Requirements:**_

**1.Python:** To write the automation logic.

**2.Raspbian OS:** Recommended operating system for Raspberry Pi.

**3.Required Python Libraries:**

**RPi.GPIO:** To control the GPIO pins.

**time:** For timing functions in the automation script.

__**Setup and Installation:**__

**Hardware Connections:**

1.Connect the LDR sensor to one of the GPIO pins on the Raspberry Pi.

2.Connect the relay module to another GPIO pin to control the light bulb.

3.Install Required Libraries: On your Raspberry Pi, install the necessary libraries 

```sudo apt-get update

sudo apt-get install python3-rpi.gpio
```
 Write the Python script to read values from the light sensor and adjust the brightness of the light bulb accordingly. Use Pulse Width Modulation (PWM) to control the relay module.

**Automation Logic:** Implement the automation logic to adjust the brightness based on the ambient light conditions.

**Testing:** Test the system in different lighting conditions (daytime, evening, low light, etc.) to ensure that it behaves as expected.

**Enclosure and Setup:** Once the system works as expected, house the components in an enclosure for protection and easy installation.

**Optional - User Interface:** You can add a web or mobile interface to allow users to control the system or view its status.

**Arduino Sketch (for basic automation):**

```#define sensorPin A5  
#define light 2

int sensorValue;
int led = 2;

void setup() {
  pinMode(led, OUTPUT);
  pinMode(sensorPin, INPUT);
}

void loop() {
  sensorValue = analogRead(sensorPin);  
  if (sensorValue < 100) {
    digitalWrite(light, HIGH);  // Turn on light if it's dark
  } else {
    digitalWrite(light, LOW);   // Turn off light if there's enough light
  }
}
```


****Python Code(for Raspberry Pi automation):******


```import RPi.GPIO as GPIO
import time

sensor_pin = 18  # GPIO pin for LDR
relay_pin = 23   # GPIO pin for relay

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(relay_pin, GPIO.OUT)

while True:
    sensor_value = GPIO.input(sensor_pin)
    if sensor_value == 0:  # Dark
        GPIO.output(relay_pin, GPIO.HIGH)  # Turn on light
    else:
        GPIO.output(relay_pin, GPIO.LOW)   # Turn off light
    time.sleep(1)
```

_**Conclusion:**_

This project provides a smart lighting system that optimizes energy usage by dynamically adjusting the light intensity based on environmental factors. 
The combination of AI and IoT technologies ensures that the lighting system is energy-efficient, user-friendly, and adaptable to different conditions.
