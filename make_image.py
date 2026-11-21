# Build entry.png for make.fun "news-image-20261121": the day's world news, one image.
# Pure drawing with PIL; no network. Run: python3 make_image.py  -> writes entry.png
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (248, 245, 238)
INK = (23, 23, 23)
NAVY = (20, 33, 61)
RED = (180, 24, 34)
GRAY = (96, 94, 90)
RULE = (205, 200, 186)
WHITE = (255, 255, 255)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(kind, size):
    return ImageFont.truetype(BOLD if kind == "b" else REG, size)


def wrap(draw, text, fnt, maxw):
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def panel(d, x0, y0, x1, y1, bar, kicker, head, dek):
    d.rectangle([x0, y0, x1, y1], fill=WHITE, outline=RULE, width=2)
    d.rectangle([x0, y0, x1, y0 + 8], fill=bar)
    tx = x0 + 14
    tw = x1 - x0 - 28
    fk = font("b", 13)
    d.text((tx, y0 + 16), kicker, font=fk, fill=RED if bar == NAVY else NAVY)
    yy = y0 + 36
    fh = font("b", 19)
    for ln in wrap(d, head, fh, tw)[:3]:
        d.text((tx, yy), ln, font=fh, fill=INK)
        yy += 23
    yy += 4
    fd = font("r", 14)
    for ln in wrap(d, dek, fd, tw)[:4]:
        d.text((tx, yy), ln, font=fd, fill=GRAY)
        yy += 18
    return yy


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Masthead
    d.rectangle([0, 0, W, 100], fill=NAVY)
    d.text((24, 22), "THE WORLD TODAY", font=font("b", 46), fill=WHITE)
    fd = font("b", 19)
    d.text((W - 24 - d.textbbox((0, 0), "SATURDAY", font=fd)[2], 24), "SATURDAY", font=fd, fill=WHITE)
    fd2 = font("r", 17)
    d.text((W - 24 - d.textbbox((0, 0), "21 NOVEMBER 2026", font=fd2)[2], 52), "21 NOVEMBER 2026", font=fd2, fill=(214, 219, 232))
    d.rectangle([0, 100, W, 114], fill=RED)

    # Lead story panel with a simple radar graphic
    d.rectangle([24, 134, 1000, 478], fill=WHITE, outline=NAVY, width=3)
    fk = font("b", 15)
    d.text((48, 154), "BREAKING", font=fk, fill=RED)
    fh = font("b", 34)
    yy = 182
    for ln in wrap(d, "RUSSIAN MISSILES CRASH IN POLAND DURING NATO DRILLS", fh, 560)[:3]:
        d.text((48, yy), ln, font=fh, fill=NAVY)
        yy += 42
    yy += 6
    fdk = font("r", 18)
    for ln in wrap(d, "Tusk calls it an intentional provocation: two cruise missiles and a drone "
                      "came down near the exercises as Kyiv weathered a night of 148 drones.", fdk, 560)[:4]:
        d.text((48, yy), ln, font=fdk, fill=INK)
        yy += 25

    cx, cy, r = 800, 300, 92
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=3)
    d.ellipse([cx - r // 2, cy - r // 2, cx + r // 2, cy + r // 2], outline=RULE, width=2)
    d.line([cx, cy - r, cx, cy + r], fill=RULE, width=2)
    d.line([cx - r, cy, cx + r, cy], fill=RULE, width=2)
    d.arc([cx - 130, cy - 130, cx + 130, cy + 130], 200, 300, fill=RED, width=3)
    d.ellipse([cx + 34, cy - 46, cx + 54, cy - 26], fill=RED)
    d.ellipse([cx - 70, cy + 30, cx - 54, cy + 46], fill=NAVY)
    fl = font("r", 13)
    d.text((cx - 118, cy + r + 14), "NATO EXERCISES, SOUTHEAST POLAND", font=fl, fill=GRAY)

    # Middle row
    pw, gap = 312, 20
    xs = [24, 24 + pw + gap, 24 + 2 * (pw + gap)]
    panel(d, xs[0], 500, xs[0] + pw, 706, NAVY, "DIPLOMACY", "HISTORIC SUMMIT IN SHENZHEN",
          "Trump, Xi and Putin agree nuclear-risk talks; China's buildup called hot and heavy.")
    panel(d, xs[1], 500, xs[1] + pw, 706, RED, "GULF", "US-IRAN TENSIONS FLARE",
          "Trump: we will not allow a dirty bomb; Hormuz oil exports down a fifth.")
    panel(d, xs[2], 500, xs[2] + pw, 706, GRAY, "EUROPE", "EU AND BRITAIN CLOSE DEAL",
          "Agri-food trade, linked carbon markets and youth mobility from March 2028.")

    # Bottom row
    panel(d, xs[0], 726, xs[0] + pw, 872, NAVY, "MIDDLE EAST", "SAUDI STRIKES KILL 41 IN YEMEN",
          "Houthis claim attacks on a Saudi power plant and port.")
    panel(d, xs[1], 726, xs[1] + pw, 872, RED, "SCANDINAVIA", "DENMARK EXPELS RUSSIAN ATTACHE",
          "Non-essential Russian visas halted over a foiled plot.")
    panel(d, xs[2], 726, xs[2] + pw, 872, GRAY, "SPACE", "SPACEX DRAGON LEAVES THE ISS",
          "The cargo craft heads home with a load of science samples.")

    # In brief
    d.rectangle([24, 892, 1000, 1000], fill=WHITE, outline=RULE, width=2)
    fb = font("b", 16)
    d.text((40, 908), "IN BRIEF", font=fb, fill=NAVY)
    fi = font("r", 14)
    briefs = [
        "Kyiv: missiles hit homes in the Podilskyi district; Kryvyi Rih struck again.",
        "Lufthansa cuts 1,000 jobs after a 180-million-euro loss; US blames old systems for outages.",
        "The FBI probes an apparent breach of the NCIC crime database.",
    ]
    for i, b in enumerate(briefs):
        col = 40 + i * 322
        d.ellipse([col, 938, col + 6, 944], fill=RED)
        yy = 932
        for ln in wrap(d, b, fi, 300)[:2]:
            d.text((col + 12, yy), ln, font=fi, fill=INK)
            yy += 18

    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
