
from microbit import *
import music

a = Image("00900:"
            "09090:"
            "99999:"
            "90009:"
            "90009")

b = Image("99900:"
            "90090:"
            "99900:"
            "90090:"
            "99900")

c = Image("09990:"
            "90000:"
            "90000:"
            "90000:"
            "09990")

d = Image("99900:"
            "90090:"
            "90090:"
            "90090:"
            "99900")

e = Image("09990:"
            "09000:"
            "09990:"
            "09000:"
            "09990")

f = Image("09990:"
            "09000:"
            "09990:"
            "09000:"
            "09000")

g = Image("09990:"
            "90000:"
            "90099:"
            "90009:"
            "09990")

h = Image("90009:"
            "90009:"
            "99999:"
            "90009:"
            "90009")

i = Image("00900:"
            "00900:"
            "00900:"
            "00900:"
            "00900")

j = Image("00009:"
            "00009:"
            "00009:"
            "90009:"
            "09990")

k = Image("90090:"
            "90900:"
            "99000:"
            "90900:"
            "90090")

l = Image("90000:"
            "90000:"
            "90000:"
            "90000:"
            "99999")

m = Image("90009:"
            "99099:"
            "90909:"
            "90909:"
            "90909")

n = Image("90009:"
            "99009:"
            "90909:"
            "90099:"
            "90009")

o = Image("09990:"
            "90009:"
            "90009:"
            "90009:"
            "09990")


p = Image("99900:"
            "90090:"
            "99900:"
            "90000:"
            "90000")


q = Image("09990:"
            "90009:"
            "90009:"
            "09990:"
            "00009")


r = Image("99900:"
            "90090:"
            "99900:"
            "90090:"
            "90090")

s = Image("09990:"
            "90000:"
            "09900:"
            "00090:"
            "99900")

t = Image("99999:"
            "00900:"
            "00900:"
            "00900:"
            "00900")

u = Image("90009:"
            "90009:"
            "90009:"
            "90009:"
            "09990")

v = Image("90009:"
            "90009:"
            "90009:"
            "09090:"
            "00900")

w = Image("90909:"
            "90909:"
            "90909:"
            "90909:"
            "09090")

x = Image("90009:"
            "09090:"
            "00900:"
            "09090:"
            "90009")

y = Image("90009:"
            "09090:"
            "00900:"
            "00900:"
            "00900")


z = Image("99999:"
            "00090:"
            "00900:"
            "09000:"
            "99999")

zero = Image("09990:"
            "09090:"
            "09090:"
            "09090:"
            "09990")

one = Image("00900:"
            "09900:"
            "00900:"
            "00900:"
            "09990")

two = Image("00900:"
            "09090:"
            "00900:"
            "09000:"
            "09990")

three = Image("09900:"
            "00090:"
            "00900:"
            "00090:"
            "09900")

four = Image("09090:"
            "09090:"
            "09999:"
            "00090:"
            "00090")

five = Image("09990:"
            "09000:"
            "00990:"
            "00090:"
            "09900")

six = Image("00900:"
            "09000:"
            "09900:"
            "09090:"
            "00900")

seven = Image("09999:"
            "00009:"
            "00090:"
            "00900:"
            "09000")

eight = Image("09990:"
            "09090:"
            "09990:"
            "09090:"
            "09990")

nine = Image("09990:"
            "09090:"
            "09990:"
            "00090:"
            "00090")

letters = (a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z)
length = len(letters)

numbers = (zero, one, two, three, four, five, six, seven, eight, nine)
num = len(numbers)


display.scroll("HI")

i = 0
j = 0

while i <= length and j <= num:
    while button_a.is_pressed():
        if accelerometer.was_gesture("right"):
            sleep(550)
            display.show(letters[i])
            music.play(music.JUMP_UP)
            i += 1
        if accelerometer.was_gesture("left"):
            sleep(550)
            display.show(letters[i])
            music.play(music.JUMP_DOWN)
            i -= 1
        if i == (length -1):
            display.show(letters[i])
            music.play(music.POWER_UP)

    while button_b.is_pressed():
        if accelerometer.was_gesture("right"):
            sleep(550)
            display.show(numbers[j])
            music.play(music.JUMP_UP)
            j += 1
        if accelerometer.was_gesture("left"):
            sleep(550)
            display.show(numbers[j])
            music.play(music.JUMP_DOWN)
            j -= 1
        if i == (length -1):
            display.show(numbers[j])
            music.play(music.POWER_UP)
