import os
from PIL import Image, ImageCms


profile = ImageCms.createProfile('sRGB')

def save_image(img, path, file):
        # save image with correct srgb profile
        img.save(path + file, icc_profile=
                 ImageCms.ImageCmsProfile(profile).tobytes())



class Animated2DCharacterData:
    src_root = '2DAnimatedVectorCharacters/'
    dst_root = 'C:/Users/gatew/Projects/PyLink/data/'
    
    def build_data(self):
        self.__create_dirs()

        # resize animations
        self.__resize_dir('_Char3_NoHands/', 'player/')
        # self._resize_images('_Weapon_R2/', 'weapon/')  # TODO: weapon anims?

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

    def __resize_textures(self, file, img):
        # resize textures (ground, weapons, etc.) from 2048px to various sizes
        match file:
            # weapon effects
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
            # weapon images
            case 'weaponR1.png' | 'weaponR2.png' | 'weaponR3.png':
                # weapons are 2048px; poor fit w/player @ 256px; try 128x128px
                img128 = img.resize((128,128))
                save_image(img128, self.dst_root, file)
            # ground and rock textures
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
    # run_ninja_adventure_data()
    data = Animated2DCharacterData()
    data.build_data()
    print('data.py -> 2DAnimatedVectorCharacter.build_data(): success?!')



class NinjaAdventureData:  
    def __init__(self):
        self.path = 'NinjaAdventure/'
        self.profile = ImageCms.createProfile('sRGB')
    
    def _save_image(self, img, path, file):
        # save image with correct srgb profile
        img.save(path + file, icc_profile=
                 ImageCms.ImageCmsProfile(self.profile).tobytes())

    def resize_spritesheet(self):
        path = self.path + '_Characters/GoldKnight/Spritesheet.png'
        with Image.open(path) as img:
            img32 = img.resize((img.width * 2, img.height * 2), 0)
            self._save_image(img32, self.path, 'spritesheet.png')
    
    def resize_anim_images(self):
        if not os.path.exists(os.path.join(self.path, 'frames32/')):
            os.mkdir(os.path.join(self.path, 'frames32/'))
        src_path = self.path + '_Characters/GoldKnight/SeparateAnim/'
        for file in os.listdir(src_path):
            with Image.open(src_path + file) as img:
                img32 = img.resize((img.width * 2, img.height * 2), 0)
                file, ext = os.path.splitext(file.lower())
                if img32.width != 32:  # image is multiple frames
                    dst_path = self.path
                else:
                    dst_path = self.path + 'frames32/'
                self._save_image(img32, dst_path, file + ext)
    
    def _direction(self, i):
        match (i):
            case 0:
                return 'down'
            case 1:
                return 'up'
            case 2:
                return 'left'
            case 3:
                return 'right'
            case _:
                return ''
    
    def _split_frames(self, anim):
        tile_size = 32
        with Image.open(self.path + anim + '.png') as img:
            for i in range(4):
                box = (i * tile_size, 0,                      # x, y
                       i * tile_size + tile_size, tile_size)  # right, bottom
                frame = img.crop(box)
                path = self.path + 'frames32/'
                file = anim + '_' + self._direction(i) + '.png'
                self._save_image(frame, path, file)
    
    def split_anim_frames(self):
        # split anim strips into individual tiles for each direction
        for anim in ['attack', 'idle', 'jump']:
            self._split_frames(anim)
        # split walk spritesheet into animations (4 tiles) for each direction
        with Image.open(self.path + 'walk.png') as img:
            for row in range(4):
                for col in range(4):
                    left = col * 32
                    upper = row * 32
                    right = left + 32
                    lower = upper + 32
                    box = (left, upper, right, lower)
                    frame = img.crop(box)
                    path = self.path + 'frames32/'
                    file = 'walk_' + self._direction(col) + '_' + str(row)
                    self._save_image(frame, path, file + '.png')
    
    def resize_frames(self):
        # scale frames to 64x64 for zelda tutorial
        path = os.path.join(self.path, 'frames64/')
        if not os.path.exists(path):
            os.mkdir(path)
        for file in os.listdir(self.path + 'frames32/'):
            with Image.open(self.path + 'frames32/' + file) as img32:
                img64 = img32.resize((img32.width * 2, img32.height * 2), 0)
                self._save_image(img64, path, file)
    
    def resize_tilesets_32(self):
        path = os.path.join(self.path, 'tilesets32/')
        if not os.path.exists(path):
            os.mkdir(path)
        for root, dirs, files in os.walk(self.path + '_Tilesets/'):
            for file in files:
                with Image.open(root + '/' + file) as img:
                    img32 = img.resize((img.width * 2, img.height * 2), 0)
                    if file == 'Elements.png':
                        file = 'InteriorElements.png'
                    self._save_image(img32, path, file.lstrip('Tileset'))
    
    def resize_tilesets_64(self):
        dst_path = os.path.join(self.path, 'tilesets64/')
        if not os.path.exists(dst_path):
            os.mkdir(dst_path)
        src_path = self.path + 'tilesets32/'
        for file in os.listdir(src_path):
            with Image.open(src_path + file) as img:
                img64 = img.resize((img.width * 2, img.height * 2), 0)
                self._save_image(img64, dst_path, file)

def run_ninja_adventure_data():
    data = NinjaAdventureData()
    data.resize_spritesheet()
    data.resize_anim_images()
    data.split_anim_frames()
    data.resize_frames()
    data.resize_tilesets_32()
    data.resize_tilesets_64()
