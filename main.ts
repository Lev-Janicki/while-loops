light.setBrightness(5)
while (true) {
    light.setAll(light.rgb(255, 0, 255))
    pause(1000)
    light.clear()
    pause(1000)
}
