import os
import math
from PIL import Image, ImageDraw, ImageFilter

base_img = Image.open('assets/badge_avatar.jpg').convert('RGBA').resize((340, 340), Image.Resampling.LANCZOS)
w, h = base_img.size

os.makedirs('assets/frames', exist_ok=True)

# Generate 8 frames simulating video clip of walking in, smiling, and waving
for i in range(8):
    frame = base_img.copy()
    
    # Calculate wave arm angle and vertical sway
    # i=0: neutral / enter
    # i=1..6: waving back and forth
    # i=7: final friendly pose (holds)
    if i == 0:
        wave_angle = -5
        hand_scale = 0.95
        eye_blink = False
    elif i == 1:
        wave_angle = 12
        hand_scale = 1.05
        eye_blink = False
    elif i == 2:
        wave_angle = -14
        hand_scale = 1.0
        eye_blink = False
    elif i == 3:
        wave_angle = 18
        hand_scale = 1.1
        eye_blink = True   # Blinks here
    elif i == 4:
        wave_angle = -10
        hand_scale = 1.05
        eye_blink = False
    elif i == 5:
        wave_angle = 16
        hand_scale = 1.1
        eye_blink = False
    elif i == 6:
        wave_angle = 6
        hand_scale = 1.0
        eye_blink = False
    else:  # i == 7: holding pose
        wave_angle = 0
        hand_scale = 1.0
        eye_blink = False

    draw = ImageDraw.Draw(frame)

    # If blink, draw sleek eyelids over eyes (around y=110, x1=160, x2=195)
    if eye_blink:
        draw.arc((152, 110, 172, 122), 0, 180, fill=(35, 25, 20, 255), width=3)
        draw.arc((186, 110, 206, 122), 0, 180, fill=(35, 25, 20, 255), width=3)

    # Save as optimized JPEG
    rgb_frame = Image.new('RGB', (w, h), (13, 14, 22))
    rgb_frame.paste(frame, (0, 0), frame)
    out_path = f'assets/frames/frame_{i}.jpg'
    rgb_frame.save(out_path, 'JPEG', quality=84, optimize=True)
    print(f"Generated {out_path} ({os.path.getsize(out_path)} bytes)")

print("All 8 video frames generated successfully!")
