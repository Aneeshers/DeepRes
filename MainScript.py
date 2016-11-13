import os
EnhancePYDir = " /Users/aneeshmuppidi/Downloads/DeepRes/enhance.py"
videoDirectory = " /Users/(USERNAME)/Downloads/ATEST.mp4"
FrameRate =  " 24/1"
Filename = "filename"
Dir = " ATEST/"
DirectoryToSave = Dir + Filename + "%03d.jpg"
DirectoryToSaveX = Dir +Filename + "%03d_ne2x.png"
command = "ffmpeg -i " + videoDirectory + " -r " + FrameRate + DirectoryToSave
os.system(command)


command2 = "python3.5" + EnhancePYDir + " --zoom=2" + Dir + "*.jpg"
os.system(command2)
command3 = "avconv -framerate 15 -f image2 -i " + DirectoryToSave + "  -b 65536k out1.mov"
os.system(command3)
command4 = "avconv -framerate 15 -f image2 -i " + DirectoryToSaveX +  " -b 65536k out2.mov"
os.system(command4)
