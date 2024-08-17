from PIL import Image, ImageDraw, ImageFont

def text_to_handwriting(text, save_path, rgb_color):
    # Define the image size
    image = Image.new('RGB', (800, 600), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Load the Lemon Tuesday font
    font_path = r"D:\pythonprojects\smallproject\Lemon Tuesday.otf"  # Corrected path to the uploaded font file
    try:
        font = ImageFont.truetype(font_path, 30)
    except IOError:
        print("Font file not found. Please ensure the path to the font file is correct.")
        return

    # Draw the text on the image
    draw.text((50, 50), text, fill=tuple(rgb_color), font=font)

    # Save the image
    image.save(save_path)
    print(f"Image saved as {save_path}")

# Text to convert
txt = """Hy wassup guys"""

# Call the function
text_to_handwriting(txt, "txttohand.png", [0, 0, 0])

