import piface.pfio as pfio
import time

pfio.init()
teste = pfio.digital_read(2)
print (teste)
start=time.time()

led1 = pfio.LED(7)
led1.turn_on()
time.sleep(1)
led1.turn_off()

elapsed = (time.time() - start)
print elapsed


