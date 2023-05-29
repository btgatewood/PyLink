import os
from PIL import Image, ImageCms

"""
Animated Body
    body  x 1
    hands x 2 (L/R)
    feet  x 2 (L/R)
    wings x 2 (L/R)

Character Options
    head    x 3
    hair    x 3
    horns   x 5
    eyes    x 7
    mouth   x 8
    weapon  x 3
"""

"""
Notes
    - player sprites are ~64x96 with 256x256 textures
    - only the death animation has the player move outside of hitbox
"""

class GraphicsDataBuilder:
    def __init__(self):
        self.root = 'C:/Users/gatew/Projects/PyLink/'
        self.src_root = self.root + 'data/rgsdev/'
        self.dst_root = self.root + 'data/' # TODO: 'data/graphics/'? 'test/'?

        profile = ImageCms.createProfile('sRGB')
        self.icc_profile = ImageCms.ImageCmsProfile(profile).tobytes()
    
    def build_data(self):
        """ Main class method; modifies and exports graphics data. """
        self._make_dirs()
        # self._resize_environment_textures()
        # TODO: resize extras folder  (bullet, crosshair, and muzzle)
        # resize player animation frames
        self._resize_images_dir('char3_no_hands/', 'player/', 256)
        # resize weapon textures
        self._resize_images_dir('weapons/', 'weapons/', 128)
    
    def _make_dirs(self):
        """ Utility function to build the output directory structure. """
        if not os.path.exists(self.dst_root):
            os.mkdir(self.dst_root)
        for path in ['extras/', 'player/', 'weapons/']:
            # TODO: delete pre-existing folders?
            dst_path = os.path.join(self.dst_root, path)
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
    
    def _resize_image(self, img, size):
        """ Utility function to get a resized image using the best filter. """
        return img.resize((size,size), Image.Resampling.LANCZOS)
    
    def _save_image(self, img, path):
        """ Utility function to save images with the correct srgb profile. """
        img.save(path, icc_profile = self.icc_profile)
    
    def _resize_images_dir(self, src_dir, dst_dir, size):
        """ Utility function to resize all images in a folder to one size. """
        src_path = os.path.join(self.src_root, src_dir)
        dst_path = os.path.join(self.dst_root, dst_dir)
        for file in os.listdir(src_path):
            with Image.open(src_path + file) as img:
                self._save_image(self._resize_image(img, size), 
                                 f'{dst_path}{file}')
                print(f'file resized: {src_dir}{file}')
    

if __name__ == '__main__':
    data = GraphicsDataBuilder()
    data.build_data()
    print('data.py: graphics.build_data() complete')
