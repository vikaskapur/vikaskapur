from .display_profile import DisplayProfile

user_profile = DisplayProfile()

def profile():
    user_profile.display_profile()

def name():
    user_profile.display_name()

def photo():
    user_profile.display_image()
