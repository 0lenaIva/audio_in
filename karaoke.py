from pygame import *
import sounddevice as sd
import scipy.io.wavfile as wav

fs = 44100
recording = None
is_recording = False
voice_file = ''
minus_track = ''

init()

mixer.init()
mixer.music.set_volume(0.5)
SIZE = (1200,600)
window = display.set_mode(SIZE)
clock = time.Clock()
font.init()
font_big = font.SysFont('Times New Roman', 32)

btn_rect = Rect(425, 250, 350, 80)
rect_color = 'white'
btn_text = 'Record'


while True:
    for e in event.get():
        if e.type == QUIT:
            quit()
    
    window.fill('black')
    draw.rect(window, rect_color, btn_rect)
    text_surface = font_big.render(btn_text, True, 'black')
    window.blit(text_surface, (btn_rect.x +20, btn_rect.y + 25))

    display.update()
    clock.tick(40)