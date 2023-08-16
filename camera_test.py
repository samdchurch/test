from jetson_utils import videoSource, videoOutput

input = videoSource("/dev/video0")
           
# output
output = videoOutput("test.mp4")


while True:
    img = input.Capture()
    output.Render(img)
    
    if not input.IsStreaming() or not output.IsStreaming():
        break