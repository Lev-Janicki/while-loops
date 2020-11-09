light.set_brightness(5)
'''while True:
    light.set_all(light.rgb(255,0,255))
    pause(1000)
    light.clear()
    pause(1000)
x = 0
for i in range(10):
    light.set_pixel_color(x, light.rgb(255,0,255))
    pause(300)
    light.clear()
    x=x+1'''
while True:
    x = 0
    for i in range(10):
        light.set_pixel_color(x, light.rgb(255,0,255))
        pause(300)
        x=x+1
    x =0
    for i in range (10):
        light.set_pixel_color(x, light.rgb(0,0,0))
        pause (300)
        x=x+1
