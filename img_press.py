from PIL import Image
import aspose.words as aw
import os


image_path = "D:\\for_study\\PHP_projects\\webjox_test_case\\images\\\\"
file_names = os.listdir(image_path)
print(file_names)

image_save_path = "D:\\for_study\\PHP_projects\\webjox_test_case\\preview_images\\"


for file_name in file_names:
    fixed_width = 200 # указываем фиксированный размер стороны
    img = Image.open(image_path + file_name)
    # получаем процентное соотношение
    # старой и новой ширины
    width_percent = (fixed_width / float(img.size[0]))
    # на основе предыдущего значения
    # вычисляем новую высоту
    height_size = int((float(img.size[0]) * float(width_percent)))
    # меняем размер на полученные значения
    new_image = img.resize((fixed_width, height_size))
    # new_image.show()
    new_image.save(image_save_path + file_name)
    #  Create document object
    doc = aw.Document()
    # Create a document builder object
    builder = aw.DocumentBuilder(doc)
    # Load and insert PNG image
    shape = builder.insert_image(image_path + file_name)
    # Specify image save format as SVG
    saveOptions = aw.saving.ImageSaveOptions(aw.SaveFormat.SVG)
    # Save image as SVG
    shape.get_shape_renderer().save(image_save_path + file_name[:len(file_name) - 3] + "svg", saveOptions)



