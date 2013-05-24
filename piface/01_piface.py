import piface.pfio as pfio
pfio.init()
teste = pfio.digital_read(2)
print (teste)
led1 = pfio.LED(1)
led1.turn_on()

