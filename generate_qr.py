#!/usr/bin/env python3

import qrcode
import argparse
from PIL import Image

def generate_qr(data, logo_path=None, output="python_qr.png"):
    # Generate QR Code
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create QR code image
    qr_img = qr.make_image(fill="black", back_color="white").convert("RGB")

    # If a logo is provided, overlay it
    if logo_path:
        try:
            logo = Image.open(logo_path)

            # Resize the logo
            logo_size = qr_img.size[0] // 4
            logo = logo.resize((logo_size, logo_size))

            # Get position for overlay
            pos = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)

            # Overlay the logo
            qr_img.paste(logo, pos, mask=logo)
        except FileNotFoundError:
            print(f"Warning: {logo_path} not found. Generating QR without logo.")

    # Save the QR code
    qr_img.save(output)
    print(f"QR Code saved as '{output}'")

    # Open the image automatically on macOS
    qr_img.show()

# Parse command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR code with optional Python 3 logo.")
    parser.add_argument("data", help="The data to encode in the QR code (e.g., a URL).")
    parser.add_argument("--logo", help="Path to the Python logo image (optional).", default=None)
    parser.add_argument("--output", help="Output filename (default: python_qr.png).", default="python_qr.png")

    args = parser.parse_args()

    # Generate QR code with given parameters
    generate_qr(args.data, args.logo, args.output)

