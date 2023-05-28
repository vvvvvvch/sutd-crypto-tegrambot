from PIL import Image

filename = "sobaken.jpg"
with Image.open(filename) as img:
    img.load()

new_img = img.resize((img.width // 3, img.height // 3))

new_img.save("resized_sobaken.jpg")

converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
converted_img.save("image_flipsobaken_top.jpg")
converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
converted_img.save("image_flip_sobaken.jpg")
