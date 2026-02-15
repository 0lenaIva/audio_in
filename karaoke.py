from pygame import *
import sounddevice as sd
import scipy.io.wavfile as wav

fs = 44100
recording = None
is_recording = False
voice_file = 'audio [vocals].mp3'
minus_track = 'audio [music].mp3'

init()
mixer.init()
mixer.music.set_volume(0.5)

def start_voice_record():
    global recording
    recording = sd.rec(int(fs*5), samplerate=fs, 
                       channels=1, dtype='int16')
def stop_voice_record():
    global recording
    if recording is not None:
        wav.write(voice_file, fs, recording)
def play_song_and_voice_together():
    mixer.music.load(minus_track)
    mixer.music.play()
    voice_sound = mixer.Sound(voice_file)
    voice_sound.play()




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
        if e.type == MOUSEBUTTONDOWN:
            if btn_rect.collidepoint(e.pos):
                if not is_recording:
                    rect_color = 'red'
                    btn_text = 'Стоп та прослухати'
                    is_recording = True
                    mixer.music.load(minus_track)
                    mixer.music.play()
                    start_voice_record()
                else:
                    rect_color = 'white'
                    btn_text = 'Запис'
                    is_recording = False
                    stop_voice_record()
                    play_song_and_voice_together()
                    
    window.fill('black')
    draw.rect(window, rect_color, btn_rect)
    text_surface = font_big.render(btn_text, True, 'black')
    window.blit(text_surface, (btn_rect.x +20, btn_rect.y + 25))

    display.update()
    clock.tick(40)
