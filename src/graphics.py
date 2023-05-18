"""
Base Animations
    body  x 1
    hands x 2 (L/R)
    feet  x 2 (L/R)
    wings x 2 (L/R)

Options
    head  x 3
    hair  x 3
    horns x 5
    eyes  x 7
    mouth x 8
    weapon x 3
"""

"""
Notes
    - player sprites are ~64x96 with 256x256 textures
"""

import os
from PIL import Image, ImageCms


class GraphicsDataBuilder:
    def __init__(self):
        self.root = 'C:/Users/gatew/Projects/PyLink/'
        self.src_root = self.root + 'rgsdev/'
        self.dst_root = self.root + 'test_data/'

        profile = ImageCms.createProfile('sRGB')
        self.icc_profile = ImageCms.ImageCmsProfile(profile).tobytes()
    
    def _make_dirs(self):
        """ Utility function to build the output directory structure. """
        if not os.path.exists(self.dst_root):
            os.mkdir(self.dst_root)
        for path in ['player/', 'environment/', 'extras/', 'weapons/']:
            dst_path = os.path.join(self.dst_root, path)
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
    
    def _save_image(self, img, path):
        """ Utility function to save images with the correct srgb profile. """
        img.save(path, icc_profile = self.icc_profile)
    
    def _resize_environment_texture(self, file, img):
        dst_path = os.path.join(self.dst_root, 'environment/')
        file, ext = os.path.splitext(file)
        match file:
            case 'ground2_white':
                # resize ground detail texture from 2048px to various sizes
                img256 =
                img512 = 
                img1028 = img.resize(())
            case 'rock1' | 'rock2' | 'rock3':
                # resize rock textures from 2048px to various sizes
                img64 = img.resize((64,64), Image.Resampling.LANCZOS)
                img96 = img.resize((96,96), Image.Resampling.LANCZOS)
                img128 = img.resize((128,128), Image.Resampling.LANCZOS)
                self._save_image(img64, f'{dst_path}{file}_64{ext}')
                self._save_image(img96, f'{dst_path}{file}_96{ext}')
                self._save_image(img128, f'{dst_path}{file}_128{ext}')
    
    def _resize_environment_textures(self):
        src_path = os.path.join(self.src_root, 'environment/')
        for file in os.listdir(src_path):
            with Image.open(src_path + file) as img:
                self._resize_environment_texture(file, img)

    def build_data(self):
        """ Main class method; modifies and exports graphics data. """
        self._make_dirs()
        # TODO: resize player animations
        self._resize_environment_textures()
        # TODO: resize extras folder  (bullet, crosshair, and muzzle)
        # TODO: resize weapons folder (weapons)


if __name__ == '__main__':
    data = GraphicsDataBuilder()
    data.build_data()