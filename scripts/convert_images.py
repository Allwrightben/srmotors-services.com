from PIL import Image
import os

IMG_DIR = os.path.join(os.path.dirname(__file__), '..', 'images')
IMG_DIR = os.path.abspath(IMG_DIR)

EXTS = {'.png', '.PNG', '.webp', '.WEBP', '.webp', '.bmp', '.gif'}
SKIP_EXTS = {'.jpg', '.jpeg', '.JPG', '.JPEG'}

converted = []
errors = []

for name in os.listdir(IMG_DIR):
    base, ext = os.path.splitext(name)
    if ext in SKIP_EXTS:
        continue
    if ext in EXTS:
        src = os.path.join(IMG_DIR, name)
        dst = os.path.join(IMG_DIR, base + '.jpg')
        try:
            with Image.open(src) as img:
                # Convert to RGBA to handle transparency uniformly
                if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
                    rgba = img.convert('RGBA')
                    background = Image.new('RGBA', rgba.size, (255, 255, 255, 255))
                    background.paste(rgba, mask=rgba.split()[3])
                    rgb = background.convert('RGB')
                else:
                    rgb = img.convert('RGB')

                rgb.save(dst, format='JPEG', quality=85, optimize=True)
            os.remove(src)
            converted.append((name, base + '.jpg'))
        except Exception as e:
            errors.append((name, str(e)))

print('Converted files:')
for s,d in converted:
    print(f' - {s} -> {d}')

if errors:
    print('\nErrors:')
    for f,err in errors:
        print(f' - {f}: {err}')
else:
    print('\nAll conversions completed successfully.')
