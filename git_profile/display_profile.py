import climage
import pyfiglet

class DisplayProfile:
    """ Display Profile class to display name and image """
    
    def __init__(self):
        self.name = "Vikas Kapur"
        self.image = "resources/vikas.jpg"

    def display_name(self):
        name_banner = pyfiglet.figlet_format(self.name)
        print(name_banner)

    def display_image(self):
        image_banner = climage.convert(self.image, is_unicode=True, width=30)
        print(image_banner)

    def display_profile(self):
        self.display_name()
        self.display_image()

