import time

import epics
import bme680

def main():
    T_PV = "WS1:TEMPERATURE"
    P_PV = "WS1:PRESSURE"
    H_PV = "WS1:HUMIDITY"

    b = bme680.BME680()

    while 1:
        b.get_sensor_data()
        d = b.data
        epics.caput(T_PV, d.temperature)
        epics.caput(P_PV, d.pressure)
        epics.caput(H_PV, d.humidity)
        time.sleep(epics.caget("WS1:UPDATE"))

main()
