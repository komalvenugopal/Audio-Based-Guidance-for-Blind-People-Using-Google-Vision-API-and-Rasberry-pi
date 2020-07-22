import picamera
from google.cloud import vision
from PIL import Image, ImageDraw
import os

client = vision.ImageAnnotatorClient()
image_name = 'image.jpg'

def takephoto():
    camera = picamera.PiCamera()
    camera.capture(image_name)

def draw_face_rectangle(image_in, rect_in):
    im = Image.open(image_in)
    f,e = os.path.splitext(image_in)
    image_out = f + "_out_boundrectangle" + e
    print("image out is named: "+ image_out)

    draw = ImageDraw.ImageDraw(im)
    draw.rectangle(rect_in)
    im.save(image_out)

def photo():
    takephoto() 
    with open(image_name, 'rb') as image_file:
        content = image_file.read()
    
    #logo and label detection
    image = vision.types.Image(content=content)
    response = client.logo_detection(image=image)
    response = client.label_detection(image=image)
    labels = response.label_annotations

	text="";
    for label in labels:
        text+=(label.description)
    if(text!=""):
		return text

	#face detection 
    response = client.face_detection(image=image)
    faces = response.face_annotations

    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE','LIKELY', 'VERY_LIKELY')
	
	text=""
    for face in faces:
        text+=('anger: {}'.format(likelihood_name[face.anger_likelihood]))
        text+=('joy: {}'.format(likelihood_name[face.joy_likelihood]))
        text+=('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

		#identfying the face area
        vertices = (['({},{})'.format(vertex.x, vertex.y) for vertex in face.bounding_poly.vertices])
        rectangle = []
        rectangle.append((face.bounding_poly.vertices[0].x,face.bounding_poly.vertices[0].y))
        rectangle.append((face.bounding_poly.vertices[2].x,face.bounding_poly.vertices[2].y))
        print('face bounds: {}'.format(','.join(vertices)))
        draw_face_rectangle(image_name, rectangle)

	return text;

text_val=photo()
#Text to audio
#python3 -m pip install gTTS 
#python3 -m pip install python-vlc

from gtts import gTTS
tts = gTTS(text=text_val, lang='en')
tts.save("play.mp3")

import vlc
p = vlc.MediaPlayer("play.mp3")
p.play()
