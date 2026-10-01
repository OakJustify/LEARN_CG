import cairo
import subprocess
import math

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 200, 200)
ctx = cairo.Context(surface)

#ctx.arc(100, 100, 50, 0, 2 * 3.14159)
ctx.set_source_rgb(1, 0, 0)
ctx.move_to
ctx.fill()

surface.write_to_png("test.png")
print("OK - test.png dibuat")

subprocess.Popen(["xdg-open", "test.png"])   