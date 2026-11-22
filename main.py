import json
from PIL import Image, ImageDraw, ImageFont

def create_news_image():
    img = Image.new('RGB', (1024, 1024), '#1a1a2e')
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
    except:
        font = ImageFont.load_default()
    
    draw.text((512, 200), "WORLD NEWS", fill='#ffffff', font=font, anchor="mm")
    draw.text((512, 300), "21 November 2026", fill='#00ffcc', font=font, anchor="mm")
    draw.text((512, 420), "• Trump announces new tariffs", fill='#ffffff', font=font, anchor="mm")
    draw.text((512, 520), "• Bitcoin surges to $98,000", fill='#ffffff', font=font, anchor="mm")
    draw.text((512, 620), "• AI breakthrough in cancer research", fill='#ffffff', font=font, anchor="mm")
    draw.text((512, 720), "• Major earthquake in Japan", fill='#ffffff', font=font, anchor="mm")
    
    img.save('/output/entry.png')
    print("Image saved to /output/entry.png")

if __name__ == "__main__":
    create_news_image()
