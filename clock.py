from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1309

serial = spi(port=0, address=0)
d = ssd1309(serial)

import math
import time
import datetime
import pytz


def posn(angle, arm_length):
    dx = int(math.cos(math.radians(angle)) * arm_length)
    dy = int(math.sin(math.radians(angle)) * arm_length)
    return (dx, dy)

def render_clock(device):
    today_last_time = "Unknown"
    tz = pytz.timezone("America/Los_Angeles")
    now_gmt = datetime.datetime.now()
    now = now_gmt.astimezone(tz)
    today_date = now.strftime("%d %b %y")
    today_time = now.strftime("%I:%M:%S %P")
    if today_time != today_last_time:
        today_last_time = today_time
        with canvas(device) as draw:
            now_gmt = datetime.datetime.now()
            now = now_gmt.astimezone(tz)
            today_date = now.strftime("%d %b %y")

            margin = 3

            cx = min(device.width, 60) / 2
            cy = min(device.height, 64) / 2

            left = cx - cy
            right = cx + cy

            hrs_angle = 270 + (30 * (now.hour + (now.minute / 60.0)))
            hrs = posn(hrs_angle, cy - margin - 7)

            min_angle = 270 + (6 * now.minute)
            mins = posn(min_angle, cy - margin - 2)

            sec_angle = 270 + (6 * now.second)
            secs = posn(sec_angle, cy - margin - 2)

            draw.ellipse((left + margin, margin, right - margin, min(device.height, 64) - margin), outline="white")
            draw.line((cx, cy, cx + hrs[0], cy + hrs[1]), fill="white")
            draw.line((cx, cy, cx + mins[0], cy + mins[1]), fill="white")
            draw.line((cx, cy, cx + secs[0], cy + secs[1]), fill="red")
            draw.ellipse((cx - 2, cy - 2, cx + 2, cy + 2), fill="white", outline="white")
            draw.text((margin, 2 * (cy + margin)), today_date, fill="yellow")
            draw.text((margin, 2 * (cy + margin) + 10), today_time, fill="yellow")


def run_clock(device, page):
    while page.flag[0]:
        render_clock(device)
        time.sleep(0.1)


if __name__ == "__main__":
    try:
        run_clock(d)
    except KeyboardInterrupt:
        pass