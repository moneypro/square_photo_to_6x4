from PIL import Image
import sys


def duplicate_photo(file_path, output_path, curr_size=(2,2), target_size=(6,4)):
    image = Image.open(file_path)
    output_image = Image.new("RGB", (image.width * target_size[0] // curr_size[0], image.height * target_size[1] // curr_size[1]))
    for step_x in range(target_size[0] // curr_size[0]):
        for step_y in range(target_size[1] // curr_size[1]):
            output_image.paste(image, (step_x * image.width, step_y * image.height))
    output_image.save(output_path)


if __name__ == '__main__':
    duplicate_photo(sys.argv[1], sys.argv[2])