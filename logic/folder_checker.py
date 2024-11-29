import os
import logging

def folder_for_profiles_check():
    if not os.path.exists('profiles'):
        os.makedirs('profiles')
        logging.info("Папка 'profiles' создана")