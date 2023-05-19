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
    - TODO: NOTE: weapons are 2048px, poor fit w/player @ 256px; try 128x128px
    - player sprites are ~64x96 with 256x256 textures
    - only the death animation has the player move outside of hitbox
    - the biggest rocks (128px) are best fit for player (use as walls)
"""

"""
Thoughts
    - a tiled map probably isn't the best choice for this game
    - unless we implement more CQB, topdown shooter mechanics
"""

import os
from PIL import Image, ImageCms


class GraphicsDataBuilder:
    def __init__(self):
        self.root = 'C:/Users/gatew/Projects/PyLink/'
        self.src_root = self.root + 'data/rgsdev/'
        self.dst_root = self.root + 'data/' # TODO: 'data/graphics/'? 'test/'?

        profile = ImageCms.createProfile('sRGB')
        self.icc_profile = ImageCms.ImageCmsProfile(profile).tobytes()
    
    def _make_dirs(self):
        """ Utility function to build the output directory structure. """
        if not os.path.exists(self.dst_root):
            os.mkdir(self.dst_root)
        for path in ['player/', 'environment/']: # TODO: 'extras/', 'weapons/'
            dst_path = os.path.join(self.dst_root, path)
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
    
    # TODO: Use resize_image() and save_image() to create a super method.
    def _resize_image(self, img, size):
        """ Utility function to get a resized image using the best filter. """
        return img.resize((size,size), Image.Resampling.LANCZOS)
    
    def _save_image(self, img, path):
        """ Utility function to save images with the correct srgb profile. """
        img.save(path, icc_profile = self.icc_profile) 
    
    def _resize_player_animation_frames(self):
        """ Resize all char anim textures and save in player folder. """
        src_path = os.path.join(self.src_root, 'char3_no_hands/')
        dst_path = os.path.join(self.dst_root, 'player/')
        for file in os.listdir(src_path):
            with Image.open(src_path + file) as img:
                self._save_image(self._resize_image(img, 256), 
                                 f'{dst_path}{file}')
                print(f'file resized: {dst_path}{file}')

    def _resize_environment_texture(self, file, img):
        dst_path = os.path.join(self.dst_root, 'environment/')
        file, ext = os.path.splitext(file)
        match file:
            case 'ground_white':
                # resize background color texture from 2048px to 128px
                img128 = self._resize_image(img, 128)
                self._save_image(img128, f'{dst_path}{file}_128{ext}')
            case 'ground2_white':
                # resize ground detail texture from 2048px to various sizes
                img256 = self._resize_image(img, 256)
                img512 = self._resize_image(img, 512)
                # TODO: rotate texture?
                # # save image in 2 sizes, rotated in 4 directions each
                # for i in range(4):
                #     save_image(img256, f'{dst_path}{file}_256_{i}{ext}'
                #     save_image(img512, f'{dst_path}{file}_512_{i}{ext}'
                #     if i < 3:
                #         # -90 degrees counter-clockwise
                #         img256 = img256.rotate(-90, Image.Resampling.NEAREST)
                #         img512 = img512.rotate(-90, Image.Resampling.NEAREST)
                img1028 = self._resize_image(img, 1024)
                self._save_image(img256, f'{dst_path}{file}_256{ext}')
                self._save_image(img512, f'{dst_path}{file}_512{ext}')
                self._save_image(img1028, f'{dst_path}{file}_1028{ext}')
            case 'ground3_white':
                # resize from 762x735 to nearest pow of 2?
                img256 = self._resize_image(img, 256)
                img512 = self._resize_image(img, 512)
                self._save_image(img256, f'{dst_path}{file}_256{ext}')
                self._save_image(img512, f'{dst_path}{file}_512{ext}')
            case 'rock1' | 'rock2' | 'rock3':
                # resize rock textures from 2048px to various sizes
                img64 = self._resize_image(img, 64)
                img96 = self._resize_image(img, 96)
                img128 = self._resize_image(img, 128)
                self._save_image(img64, f'{dst_path}{file}_64{ext}')
                self._save_image(img96, f'{dst_path}{file}_96{ext}')
                self._save_image(img128, f'{dst_path}{file}_128{ext}')
            case _:
                print(f'file not resized: {dst_path}{file}{ext}')
                return
        print(f'file resized: {dst_path}{file}{ext}')
    
    def _resize_environment_textures(self):
        src_path = os.path.join(self.src_root, 'environment/')
        for file in os.listdir(src_path):
            with Image.open(src_path + file) as img:
                self._resize_environment_texture(file, img)
        
        # copy a mock player image for tiled map
        with Image.open(self.dst_root + 'player/idle_0.png') as img:
            self._save_image(img, self.dst_root + 'environment/idle_0.png')

    def build_data(self):
        """ Main class method; modifies and exports graphics data. """
        self._make_dirs()
        self._resize_player_animation_frames()
        self._resize_environment_textures()
        # TODO: resize extras folder  (bullet, crosshair, and muzzle)
        # TODO: resize weapons folder (weapons)


if __name__ == '__main__':
    data = GraphicsDataBuilder()
    data.build_data()
    print('data.py: graphics.build_data() -> success?')
