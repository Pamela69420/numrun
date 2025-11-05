#!/usr/bin/env python3
"""
Generate PNG icons for NumRun Android app
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_gradient_background(size):
    """Create purple gradient background matching game theme"""
    img = Image.new('RGB', (size, size))
    draw = ImageDraw.Draw(img)

    # Colors from game: #667eea to #764ba2
    start_color = (102, 126, 234)  # #667eea
    end_color = (118, 75, 162)     # #764ba2

    for y in range(size):
        ratio = y / size
        r = int(start_color[0] + (end_color[0] - start_color[0]) * ratio)
        g = int(start_color[1] + (end_color[1] - start_color[1]) * ratio)
        b = int(start_color[2] + (end_color[2] - start_color[2]) * ratio)
        draw.line([(0, y), (size, y)], fill=(r, g, b))

    return img

def add_rounded_rectangle(draw, xy, corner_radius, fill):
    """Draw rounded rectangle"""
    x0, y0, x1, y1 = xy
    draw.rectangle([x0 + corner_radius, y0, x1 - corner_radius, y1], fill=fill)
    draw.rectangle([x0, y0 + corner_radius, x1, y1 - corner_radius], fill=fill)
    draw.ellipse([x0, y0, x0 + corner_radius * 2, y0 + corner_radius * 2], fill=fill)
    draw.ellipse([x1 - corner_radius * 2, y0, x1, y0 + corner_radius * 2], fill=fill)
    draw.ellipse([x0, y1 - corner_radius * 2, x0 + corner_radius * 2, y1], fill=fill)
    draw.ellipse([x1 - corner_radius * 2, y1 - corner_radius * 2, x1, y1], fill=fill)

def create_icon(size, output_path):
    """Create NumRun icon"""
    # Create gradient background
    img = create_gradient_background(size)
    draw = ImageDraw.Draw(img)

    # Add white rounded square overlay for contrast
    margin = size // 10
    overlay_alpha = 20
    overlay_color = (255, 255, 255, overlay_alpha)

    # Draw mathematical symbols
    padding = size // 5
    symbol_color = (255, 255, 255)

    # Try to load font, fallback to default
    try:
        font_size = size // 3
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Draw "N" and "R" with math symbols
    text = "N+R"

    # Get text bounding box for centering
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (size - text_width) // 2
    y = (size - text_height) // 2 - bbox[1]

    # Draw text with shadow for depth
    shadow_offset = size // 100
    draw.text((x + shadow_offset, y + shadow_offset), text, fill=(0, 0, 0, 100), font=font)
    draw.text((x, y), text, fill=symbol_color, font=font)

    # Add small mathematical symbols in corners
    try:
        small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size // 10)
    except:
        small_font = ImageFont.load_default()

    corner_margin = size // 20
    # Top-left: plus
    draw.text((corner_margin, corner_margin), "+", fill=(255, 255, 255, 150), font=small_font)
    # Top-right: multiply
    draw.text((size - corner_margin - size//10, corner_margin), "×", fill=(255, 255, 255, 150), font=small_font)
    # Bottom-left: minus
    draw.text((corner_margin, size - corner_margin - size//10), "−", fill=(255, 255, 255, 150), font=small_font)
    # Bottom-right: divide
    draw.text((size - corner_margin - size//10, size - corner_margin - size//10), "÷", fill=(255, 255, 255, 150), font=small_font)

    # Save
    img.save(output_path, 'PNG', quality=95)
    print(f"✓ Created: {output_path} ({size}x{size}px)")

def main():
    """Generate all required icon sizes"""
    sizes = [
        (192, 'icon-192.png'),
        (512, 'icon-512.png'),
        (72, 'icon-72.png'),
        (96, 'icon-96.png'),
        (144, 'icon-144.png'),
        (48, 'icon-48.png'),
    ]

    print("🎨 Generating NumRun icons...")

    for size, filename in sizes:
        create_icon(size, filename)

    print("\n✅ All icons generated successfully!")
    print("\n📱 Icons ready for:")
    print("  - PWA manifest")
    print("  - Android APK")
    print("  - Google Play Store")

if __name__ == '__main__':
    main()
