from PIL import Image
import os

class Image_Tools:

    #defining constructor
    def __init__(self, filePath):
        self.file_path = filePath

    def return_list_of_files(self):
        main_file_list = []
        for file_name in os.listdir(self.file_path):
            main_file_list.append(file_name)
        return main_file_list


    def compress_pictures(self, picture_path, compression_quality):
        full_path_of_file = self.file_path + "/" + picture_path
        directories = ["1.User Optimised", "2.Small", "3.Medium", "4.Large", "5.Thumbnails"]

        compression_quality = int(compression_quality)

        try:
            #1 User Optimised
            with Image.open(full_path_of_file) as image_to_convert:
                picture_file_path = self.file_path + "/" + directories[0] + "/" + picture_path
                image_to_convert.save(picture_file_path, optimize=True, quality=compression_quality)
            #2 Small
            with Image.open(full_path_of_file) as image_to_convert:
                thumbnail_size = 640, 480
                picture_file_path = self.file_path + "/" + directories[1] + "/" + picture_path
                image_to_convert.thumbnail(thumbnail_size)
                image_to_convert.save(picture_file_path, optimize=True, quality=compression_quality)
            #3 Medium
            with Image.open(full_path_of_file) as image_to_convert:
                thumbnail_size = 1024, 768
                picture_file_path = self.file_path + "/" + directories[2] + "/" + picture_path
                image_to_convert.thumbnail(thumbnail_size)
                image_to_convert.save(picture_file_path, optimize=True, quality=compression_quality)
            #4 Large
            with Image.open(full_path_of_file) as image_to_convert:
                thumbnail_size = 2048, 1536
                picture_file_path = self.file_path + "/" + directories[3] + "/" + picture_path
                image_to_convert.thumbnail(thumbnail_size)
                image_to_convert.save(picture_file_path, optimize=True, quality=compression_quality)
            #5 Thumbnail
            with Image.open(full_path_of_file) as image_to_convert:
                thumbnail_size = 128, 128
                output_file_name = os.path.splitext(picture_path)[0] + ".thumbnail"
                picture_file_path = self.file_path + "/" + directories[4] + "/" + output_file_name
                image_to_convert.thumbnail(thumbnail_size)
                image_to_convert.save(picture_file_path, "JPEG")
        except Exception as e:
            print(e)


    def setup_directories(self):
        directories = ["1.User Optimised", "2.Small", "3.Medium", "4.Large", "5.Thumbnails"]
        for directory in directories:
            try:
                os.mkdir(f'{self.file_path}/{directory}')
            except Exception as e:
                print(e)

    def add_a_logo(self, picture_path, logo_file_path):
        directory = "Logo Added"
        full_path_of_file = self.file_path + "/" + picture_path
        try:
            os.mkdir(f'{self.file_path}/{directory}')
        except Exception as e:
            print(e)

        picture_file_path = self.file_path + "/" + directory + "/" + picture_path
        image_to_convert = Image.open(full_path_of_file)
        logo = Image.open(logo_file_path)
        image_copy = image_to_convert.copy()
        position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
        image_copy.paste(logo, position, logo)
        image_copy.save(picture_file_path)