from PIL import Image


def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    width, height = image.size

    # Convert key to integer
    key = int(key)

    # Encrypt each pixel in the image
    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            encrypted_pixel = tuple(
                (p + key) % 256 for p in pixel)  # Add key and ensure pixel values are in the range [0, 255]
            encrypted_pixels.append(encrypted_pixel)

    # Create a new image with encrypted pixels
    encrypted_image = Image.new(image.mode, (width, height))
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save("encrypted_image.png")
    print("Image encrypted successfully.")


def decrypt_image(image_path, key):
    # Open the encrypted image
    image = Image.open(image_path)
    width, height = image.size

    # Convert key to integer
    key = int(key)

    # Decrypt each pixel in the image
    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            decrypted_pixel = tuple(
                (p - key) % 256 for p in pixel)  # Subtract key and ensure pixel values are in the range [0, 255]
            decrypted_pixels.append(decrypted_pixel)

    # Create a new image with decrypted pixels
    decrypted_image = Image.new(image.mode, (width, height))
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save("decrypted_image.png")
    print("Image decrypted successfully.")


if __name__ == "__main__":
    image_path = "example.png"  # Change this to the path of your image
    key = input("Enter encryption/decryption key: ")

    encrypt_image(image_path, key)
    decrypt_image("encrypted_image.png", key)
