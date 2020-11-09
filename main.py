light.set_brightness(5)
while True:
    light.set_all(light.rgb(255,0,255))
    pause(1000)
    light.clear()
    pause(1000)
