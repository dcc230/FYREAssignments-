# Team member names: Agragyan, Cristian, Dean
# Purpose of the code: Read sensor data and add to CSV files
# Date code was started: 09/16/26
# Date of last update: 09/16/26
# Explanation of AI use: We used AI to write the whole thing

from machine import Pin, ADC
import time

# Rain sensor AO -> D6 / GPIO 9
rain = ADC(Pin(9))
rain.atten(ADC.ATTN_11DB)

file_number = 1
data_count = 0
recording = False

while True:
    # Read sensor
    adc_value = rain.read()
    voltage = (adc_value / 4095) * 3.3

    print("ADC:", adc_value, "Voltage:", voltage)

    # Don't start recording until both values are not 0
    if not recording:
        if adc_value != 0 and voltage != 0:
            recording = True
            data_count = 0
            filename = "rain_data{}.csv".format(file_number)

            # Create new CSV file
            with open(filename, "w") as f:
                f.write("adc_value,voltage\n")

            print("Started recording:", filename)

    # Save data once recording has started
    if recording:
        with open(filename, "a") as f:
            f.write("{},{:.3f}\n".format(adc_value, voltage))

        data_count += 1
        print("Saved data point", data_count, "of 10")

        # Stop after 10 data points
        if data_count >= 10:
            print("Finished:", filename)

            file_number += 1
            recording = False

    time.sleep(1)
