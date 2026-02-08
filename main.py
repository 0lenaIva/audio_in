from pygame import *
import sounddevice as sd

fs = 44100
chunk = 1024
SIZE = (800,400)

init()

screen = display.set_mode(SIZE)
display.set_caption('Звук')
clock = time.Clock()

data = [0.0] * chunk

def audio_callback(indata, frames, time_info,status):
    global data
    if status:
        print(status)
    
    data = [sample * (SIZE[1]//2) for sample in indata[:, 0].tolist()]

stream= sd.InputStream(
    callback=audio_callback,
    channels=1,
    samplerate=fs,
    blocksize=chunk,
    dtype='float32'
)
stream.start()

running = True
while running:
    screen.fill((0,0,0))
    for e in event.get():
        if e.type == QUIT:
            running = False

    points=[]
    for i, sample in enumerate(data):
        x = int(i*SIZE[0]/ chunk)
        y = int(SIZE[1]/2 + sample)
        points.append((x,y))

    if len(points) > 1:
        draw.lines(screen, (0,200, 0), False, points, 2)
    
    display.update()
    clock.tick(60)

stream.stop()
quit()