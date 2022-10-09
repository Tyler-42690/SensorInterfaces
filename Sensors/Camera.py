import cv2
import os
class Camera():
    def __init__(self) -> None:
        self.camera = cv2.VideoCapture()
        pass
    def take_picture(self):
        # frame
        currentframe = 0
        try:
      
         # creating a folder named data
            if not os.path.exists('data'):
                 os.makedirs('data')
  
# if not created then raise error
        except OSError:
             print ('Error: Creating directory of data')
        while(True):

        # reading from frame
            ret,frame = self.camera.read()
            if ret:
            # if video is still left continue creating images
                name = './data/frame' + str(currentframe) + '.jpg'
                print ('Creating...' + name)
  
        # writing the extracted images
                cv2.imwrite(name, frame)
  
        # increasing counter so that it will
        # show how many frames are created
                currentframe += 1
            else:
                break
  
# Release all space and windows once done
        self.camera.release()
        cv2.destroyAllWindows()
        pass
    