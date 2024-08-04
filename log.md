# LOG
## Thur 7/11 - Hours 3
### Notes:
- Weirdly difficult to set up
- I2C connection wasn’t working
- Switched to SPI and it worked but the demo code stopped working at a point
- Snowflakes are only on top bit and half of scroll is still on the screen
### Future:
- Learn to program it with actual words
- Maybe switch to raspi to give it more functionality
- Switch to Nano maybe

## Mon 7/22 - Hours 4.5
### Notes:
- With JQ
- Connected TOLED to Raspi
- Worked, got clock, and scrolling to run
```python
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309

serial = spi(port=0, address=0)
device = ssd1309(serial)
```

### Future: 
- Scrape Canvas
- Find interfaces - buttons, touchscreens, dials
- attach to glasses?
  - Figure out where to display information

## Tues 7/23
> [!Warning]
> Somehow the variable names get worse and worse as time goes on :(
### Notes:
- created canvas access through canvas API
- set up a button push using interrupts
- created new heat sink and aesthestic wifi dongle
- connected canvas to the screen itself and showed live data

### Future:
- connect to glasses
- add alternate pages with other data
  - weather, notes, something else
- add camera and allow it to process data
- add mike for subtitles

## Wed 7/31 - Hours 2 
### Notes:
- Not a lot of progress
- Button does not work

### Future: 
- Fix button
- Swaperoonies


## Thur 8/1 - Hours 3
### Notes:
- Fixed button
- Started on state machine
- Started on gyro, stopped because FRC is trash

### Future:
- Camera functionality
- Put it all together so far

## Fri 8/2 - Hours 1 
### Notes:
- Solo loser
- Struggled to vnc
- Remember to vncserver-virtual every time
- Connected camera (didn’t get it working)

### Future:
- Get camera working

## Sat 8/3 - Hours 3.5
### Notes:
- Late at night
- Worked on state-machine - finally worked, overusing resources though
- Got camera working
- No scripts could access because picamera2 then libcamera decided they didn’t want to work

### Future:
- Get camera to read images
- Hand motions to change page
- Cleaner page transitions
- Split on_enter_func into on_enter and while_running
