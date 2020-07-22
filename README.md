# Audio-Based-Guidance-for-Blind-People-Using-Google-Vision-API-and-Rasberry-pi
Steps:- 
0. Install rasberrypi ISO by flashing image
1. The ultrasonics sensor detects if person is going to hit anything and warns with a buzzer
2. Create a button with connections in Rasberry pi when the person clicks it captures and ouput the audio
3. When button is Clicked the Python script which is imported will be executed
4. The python file will capture an image using picamera module and camera sensor that is connected to rasberry pi and send the image to Google Vision API
   and get the text, the text is then converted into audio is played using the head phone connected to rasberry pi head phone jack


Components Required:-
	Raspberry Pi  (Pi3 or newer)
	Power Supply
	Raspberry Pi Camera
	Google Cloud Account
	HeadPhones
	Ultrasonic sensors


Moudles Required:- 
python3 -m pip install RPi.GPIO
python3 -m pip install --user pip
python3 -m pip install --user google-cloud-vision
python3 -m pip install --user Pillow
python3 -m pip install --user picamera
python3 -m pip install gTTS #audio module
python3 -m pip install python-vlc


Note-
Download your Google VISION API credentials as JSON file and store 
export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/filename.json
GOOGLE_APPLICATION_CREDENTIALS="/home/pi/filename.json"
echo $GOOGLE_APPLICATION_CREDENTIALS
