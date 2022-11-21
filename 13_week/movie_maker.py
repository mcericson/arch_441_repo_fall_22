import os
import moviepy.video.io.ImageSequenceClip


def make_movie(fps, file_name):
    
    all_files = os.listdir()
    all_images = []
    
    for i in all_files:
        if i.endswith(".png"):
            all_images.append(i)
    
    clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(all_images, fps=fps)
    file_path = str(file_name) + ".mp4"
    clip.write_videofile(file_path)
            
    

make_movie(10, "rgb_cube")