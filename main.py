from PIL import Image

Image.MAX_IMAGE_PIXELS = None

if __name__ == '__main__':
    img = Image.open('./123.png')
    img = img.convert("RGB")
    original_width, original_height = img.size
    print(original_height)
    print(original_width)
    parts = 1
    left = 0
    # right = original_width
    right = 1098
    part_height = 20000
    while part_height * parts < original_height:
        upper = part_height * (parts - 1)
        lower = part_height * parts
        im_crop = img.crop((left, upper, right, lower))
        im_crop.save("split_part" + str(parts) + ".jpg")
        parts = parts + 1
    upper = part_height * (parts - 1)
    lower = original_height
    im_crop = img.crop((left, upper, right, lower))
    im_crop.save("split_part" + str(parts) + ".jpg")
