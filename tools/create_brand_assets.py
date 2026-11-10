"""Original procedural assets, no external image or sound samples."""
from pathlib import Path
from PIL import Image,ImageDraw
import math,struct,wave,zipfile,json
ROOT=Path(__file__).resolve().parents[1]
out=ROOT/'dist/brand';out.mkdir(parents=True,exist_ok=True)
w,h=1080,2400
wall=Image.new('RGB',(w,h),'#c9d1a8');d=ImageDraw.Draw(wall)
for radius,center,color in [(990,1700,'#325b4b'),(765,1745,'#9eaf8a'),(540,1790,'#e7d9b9'),(315,1835,'#af7055'),(90,1880,'#634f41')]:
    d.ellipse((540-radius,center-radius,540+radius,center+radius),fill=color)
    d.rectangle((540-radius,center,540+radius,2400),fill=color)
wall.save(out/'AsterVale-mineral-wallpaper.png',optimize=True)
with zipfile.ZipFile(out/'bootanimation.zip','w',compression=zipfile.ZIP_STORED) as z:
    z.writestr('desc.txt','1080 2400 24\np 1 0 part0\np 0 0 part1\n')
    import io
    for i in range(24):
        im=Image.new('RGB',(w,h),'#151d1b');p=ImageDraw.Draw(im)
        alpha=min(1,(i+1)/16);base=(21,29,27);target=(181,211,163)
        ink=tuple(round(a+(b-a)*alpha) for a,b in zip(base,target))
        p.line([(400,1300),(540,1050),(680,1300)],fill=ink,width=14,joint='curve');p.line([(465,1190),(615,1190)],fill=ink,width=14)
        p.line([(435,1335),(645,1335)],fill=ink,width=14)
        data=io.BytesIO();im.save(data,format='PNG',optimize=True);z.writestr(f'part0/{i:03}.png',data.getvalue())
        if i==23:z.writestr('part1/000.png',data.getvalue())
for name,notes,duration in [('AsterVale-soft-notification',(523.25,659.25),.45),('AsterVale-soft-start',(392,523.25,659.25),.9)]:
    rate=44100
    with wave.open(str(out/(name+'.wav')),'wb') as wav:
        wav.setnchannels(1);wav.setsampwidth(2);wav.setframerate(rate)
        data=[]
        for i in range(int(rate*duration)):
            t=i/rate;sample=0
            for n,f in enumerate(notes):
                local=t-n*.1
                if local>0:sample+=math.sin(2*math.pi*f*local)*math.exp(-local*9)*min(1,local/.012)
            data.append(struct.pack('<h',int(max(-1,min(1,sample*.14))*32767)))
        wav.writeframes(b''.join(data))
(out/'README.txt').write_text('Original AsterVale assets, Apache-2.0. Boot animation is NOT a recovery/module ZIP. Hardware untested. Do not flash this asset pack. Wallpaper and sounds may be selected manually; boot animation requires a reviewed compatible integration.\n')
with zipfile.ZipFile(ROOT/'dist/AsterVale-art-pack-0.1.0-preview.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(out.glob('*')):z.write(p,p.name)
    z.write(ROOT/'LICENSE','LICENSE')
print('Created original wallpaper, boot animation and two quiet tones; integration untested.')
