import os
from PIL import Image, ImageCms


profile = ImageCms.createProfile('sRGB')

def save_image(img, path, file):
        # save image with correct srgb profile
        img.save(path + file, icc_profile=
                 ImageCms.ImageCmsProfile(profile).tobytes())


class Animated2DCharacterData:
    root = 'C:Users/gatew/Projects/'
    src_root = root + 'Resources/RGS_Dev-2DAnimatedVectorCharacters/'
    dst_root = root + 'PyLink/data/'
    
    def build_data(self):
        self.__create_dirs()

        # resize animation frames
        self.__resize_dir('Full body animated characters/Char 3/no hands/', 
                          'player/')

        # TODO: resize environment dir (ground and rock textures)
        # TODO: resize extras dir (bullet, crosshair, muzzle textures)
        # TODO: resize weapons dir
        # resize textures
        src_path = os.path.join(self.src_root, 'Textures/')
        # dst_path = os.path.join(self.dst_root, 'textures/')
        for file in os.listdir(src_path):
            with Image.open(src_path + file) as img:
                self.__resize_textures(file, img)
            print(file)
    
    def __create_dirs(self):
        if not os.path.exists(self.dst_root):
            os.mkdir(self.dst_root)
        for dir in ['background/', 'player/',]:  # add new subdirs here
            dst_path = os.path.join(self.dst_root, dir)
            if not os.path.exists(dst_path):
                os.mkdir(dst_path)
    
    def __resize_dir(self, src_dir, dst_dir): 
        # resize images (anim frames) in src_dir from 2048px to 256px
        src_path = os.path.join(self.src_root, src_dir)
        dst_path = os.path.join(self.dst_root, dst_dir)
        for file in os.listdir(src_path):
            with Image.open(src_path + file) as img:
                save_image(img.resize((256, 256), Image.Resampling.LANCZOS),
                           dst_path, file)
            print(dst_dir + file)

    # TODO: resize environment dir (ground and rock textures)
    # TODO: resize extras dir (bullet, crosshair, muzzle textures)
    # TODO: resize weapons dir

    def __resize_textures(self, file, img):
        # resize textures (ground, weapons, etc.) from 2048px to various sizes
        match file:

            # weapon effects  # NOTE: EXTRAS/
            case 'bullet.png' | 'crosshair.png' | 'muzzle.png':
                # output bullet (2048x2048) and crosshair (64x64) and
                # muzzle (2048x2048) in multiple sizes                        
                file, ext = os.path.splitext(file)
                img16 = img.resize((16,16), Image.Resampling.LANCZOS)
                save_image(img16, self.dst_root, file + '16' + ext)
                img24 = img.resize((24,24), Image.Resampling.LANCZOS)
                save_image(img24, self.dst_root, file + '24' + ext)
                img32 = img.resize((32,32), Image.Resampling.LANCZOS)
                save_image(img32, self.dst_root, file + '32' + ext)
                img64 = None
                if file == 'bullet' or file == 'muzzle':
                    img64 = img.resize((64,64), Image.Resampling.LANCZOS)
                else:  # file == 'crosshair.png'
                    img64 = img.copy()
                save_image(img64, self.dst_root, file + '64' + ext)
                print(f'data.py -> {file}: resized and saved')

            # weapon images  # NOTE: WEAPONS/
            case 'weaponR1.png' | 'weaponR2.png' | 'weaponR3.png':
                # weapons are 2048px; poor fit w/player @ 256px; try 128x128px
                img128 = img.resize((128,128))
                save_image(img128, self.dst_root, file)

            # ground and rock textures  # NOTE: ENVIRONMENT/
            case 'ground2_white.png':
                # detailed ground texture, save image in 2 sizes and 
                # rotated in 4 directions
                img256 = img.resize((256,256), Image.Resampling.LANCZOS)
                img512 = img.resize((512,512), Image.Resampling.LANCZOS)
                file, ext = os.path.splitext(file)
                for i in range(4):
                    save_image(img256, f'{self.dst_root}background/', 
                               f'{file}256_{i}{ext}')
                    save_image(img512, f'{self.dst_root}background/', 
                               f'{file}512_{i}{ext}')
                    if i < 3:
                        img256 = img256.rotate(-90, # degress counter-clockwise
                                               Image.Resampling.NEAREST)
                        img512 = img512.rotate(-90, Image.Resampling.NEAREST)
                print(f'data.py -> {file}{ext}: rotated and saved')
            case _:  
                # resize background and rock textures from 2048px to 256px
                img256 = img.resize((256,256), Image.Resampling.LANCZOS)
                save_image(img256, self.dst_root + 'background/', file)


if __name__ == '__main__':
    data = Animated2DCharacterData()
    data.build_data()
    print('data.py -> 2DAnimatedVectorCharacter.build_data(): success?!')
