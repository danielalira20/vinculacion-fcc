"""Genera un código QR con módulos redondeados y comprueba que se lee bien.

Uso (requiere requirements-dev.txt):
    python scripts/qr.py "https://ejemplo.org" src/assets/media/qr-ejemplo.png [--color "#26306b"]
"""
import argparse
from pathlib import Path

import zxingcpp
from PIL import Image, ImageDraw

MODULE = 24  # píxeles por módulo
QUIET = 2    # módulos de margen; el marco blanco de la página completa el resto


def matrix(text):
    code = zxingcpp.create_barcode(text, zxingcpp.BarcodeFormat.QRCode, ec_level="H")
    pixels = memoryview(code.to_image(scale=1, add_quiet_zones=False))
    height, width = pixels.shape[:2]
    image = Image.frombytes("L", (width, height), pixels.tobytes())
    size = image.width
    return [[image.getpixel((x, y)) < 128 for x in range(size)] for y in range(size)], size


def in_finder(x, y, size):
    return any(fx <= x < fx + 7 and fy <= y < fy + 7 for fx, fy in ((0, 0), (size - 7, 0), (0, size - 7)))


def render(text, color):
    cells, size = matrix(text)
    side = (size + QUIET * 2) * MODULE
    image = Image.new("RGB", (side, side), "white")
    draw = ImageDraw.Draw(image)
    offset = QUIET * MODULE
    gap = MODULE * 0.1
    for y, row in enumerate(cells):
        for x, dark in enumerate(row):
            if dark and not in_finder(x, y, size):
                left, top = offset + x * MODULE + gap, offset + y * MODULE + gap
                draw.rounded_rectangle((left, top, left + MODULE - 2 * gap, top + MODULE - 2 * gap), radius=MODULE * 0.38, fill=color)
    for fx, fy in ((0, 0), (size - 7, 0), (0, size - 7)):
        left, top = offset + fx * MODULE, offset + fy * MODULE
        draw.rounded_rectangle((left, top, left + 7 * MODULE - 1, top + 7 * MODULE - 1), radius=MODULE * 2.2, fill=color)
        draw.rounded_rectangle((left + MODULE, top + MODULE, left + 6 * MODULE - 1, top + 6 * MODULE - 1), radius=MODULE * 1.5, fill="white")
        draw.rounded_rectangle((left + 2 * MODULE, top + 2 * MODULE, left + 5 * MODULE - 1, top + 5 * MODULE - 1), radius=MODULE * 0.9, fill=color)
    return image


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("text")
    parser.add_argument("output", type=Path)
    parser.add_argument("--color", default="#292724")
    args = parser.parse_args()
    image = render(args.text, args.color)
    decoded = [result.text for result in zxingcpp.read_barcodes(image.resize((480, 480)).convert("L"))]
    if decoded != [args.text]:
        raise SystemExit(f"El QR generado no se lee correctamente: {decoded!r}")
    image.save(args.output, optimize=True)
    print(f"{args.output} · {image.width}px · verificado")


if __name__ == "__main__":
    main()
