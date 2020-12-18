import os
import glob

from PIL import Image

imageSize = (128, 128)

def preprocessCelebA(path='./sampleData/raw/CelebA/', savePath='./sampleData/preprocessed/CelebA/'):
    for f in glob.glob(path + '*.jpg'):
        imageName = f.split('\\')[-1]
        numImage = int(imageName.split('.')[0])
        if numImage > 2000:
            continue

        print(imageName)

        faceImage = Image.open(f)
        width, height = faceImage.size

        ymin = int(round((height - 110)/2.))
        xmin = int(round((width - 108)/2.))

        croppedImage = faceImage.crop((xmin, ymin, xmin + 108, ymin + 140))
        croppedImage = croppedImage.resize(imageSize, Image.BILINEAR)

        saveLocation = os.path.join(savePath, imageName)
        croppedImage.save(saveLocation)
    return


def preprocessAnime(path='./sampleData/raw/Anime/', savePath='./sampleData/preprocessed/Anime/'):
    for f in glob.glob(path + '*.jpg'):
        
        try:
            imageName=f.split('\\')[-1]
        
            print(imageName)
            
            faceImage=Image.open(f)    
    
            new_img=faceImage.resize(imageSize,Image.BILINEAR)   
            new_img.save(os.path.join(savePath,imageName))
        
        except Exception as e:
            print(e)

    return


#preprocessCelebA('C:/Users/Administrator/Desktop/face_img/', 'C:/Users/Administrator/Desktop/face/')
preprocessAnime('C:/Users/Administrator/Desktop/anime_img/', 'C:/Users/Administrator/Desktop/anime_dest/')

