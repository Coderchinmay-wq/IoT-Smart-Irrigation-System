import network
from machine import Pin, ADC, Timer
from umqtt.simple import MQTTClient
import time

# Blynk credentials
BLYNK_AUTH_TOKEN ="YOUR_BLYNK_TOKEN"
BLYNK_SERVER = "blynk.cloud"
BLYNK_PORT = 1883
PUMP_SWITCH = "V6"
SOIL_MOISTURE_VPIN = "V5"

# WiFi credentials
WIFI_SSID = "YOUR_WIFI_NAME"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
# Pin configurations
SOIL_MOISTURE_PIN = 34
PUMP_PIN = 2
THRESHOLD_MOISTURE = 100  # Adjust based on sensor readings

# Variables
is_pump_on = False
client = None

# Set up hardware
soil_moisture_sensor = ADC(Pin(SOIL_MOISTURE_PIN))
soil_moisture_sensor.atten(ADC.ATTN_11DB)  # Set ADC range 0-3.6V
pump = Pin(PUMP_PIN, Pin.OUT)

# Connect to WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)
    while not wlan.isconnected():
        print("Connecting to WiFi...")
        time.sleep(1)
    print("Connected to WiFi:", wlan.ifconfig())

# Send data to Blynk
def send_to_blynk(vpin, value):
    topic = f"v1/{BLYNK_AUTH_TOKEN}/update/{vpin}"
    message = f"[{value}]"
    client.publish(topic, message)

# Check soil moisture and control pump
def check_soil_moisture(timer):
    global is_pump_on
    soil_moisture = soil_moisture_sensor.read()
    soil_moisture_percentage = max(0, min(100, 100 - int((soil_moisture - 3500) / 6.0)))
    print(f"Soil Moisture: {soil_moisture} ({soil_moisture_percentage}%)")
    
    # Send data to Blynk
    send_to_blynk(SOIL_MOISTURE_VPIN, soil_moisture_percentage)

    # Control pump
    if is_pump_on or soil_moisture_percentage < THRESHOLD_MOISTURE:
        pump.on()
        if not is_pump_on:                        
            print("Soil moisture is below the threshold. Pump turned ON automatically.")
            send_to_blynk("moisture_alert", '"Soil moisture is below the threshold!"')
    else:
        pump.off()

# Handle incoming Blynk commands
def blynk_callback(topic, msg):
    global is_pump_on
    if topic.decode() == f"v1/{BLYNK_AUTH_TOKEN}/set/{PUMP_SWITCH}":
        is_pump_on = bool(int(msg.decode()))
        if is_pump_on:
            print("Pump manually turned ON")
        else:
            print("Pump manually turned OFF")

# Set up MQTT client
def connect_blynk():
    global client
    client = MQTTClient("esp32", BLYNK_SERVER, BLYNK_PORT, BLYNK_AUTH_TOKEN)
    client.set_callback(blynk_callback)
    client.connect()
    client.subscribe(f"v1/{BLYNK_AUTH_TOKEN}/set/{PUMP_SWITCH}")
    print("Connected to Blynk MQTT server.")

# Main program
def main():
    connect_wifi()
    connect_blynk()

    # Start a timer to check soil moisture every 3 seconds
    timer = Timer(0)
    timer.init(period=3000, mode=Timer.PERIODIC, callback=check_soil_moisture)

    # Loop to handle incoming MQTT messages
    while True:
        client.check_msg()
        time.sleep(0.1)

# Run the program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program stopped.")
        pump.off()
