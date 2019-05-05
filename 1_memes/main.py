from PIL import Image, ImageFont, ImageDraw
import speech_recognition as sr
import random, textwrap

IMAGE_URL = 'meme.jpg'
FONT_TYPE = 'fonts/opensans.ttf'
SAMPLE_TEXT = 'this is a sample text this is a sample text this is a sample text'
WIDTH = 0
HEIGHT = 0

# Get random meme image from images folder
def get_rand_img():
  image_names = ['jackie_chan', 'michael_jordan', 'pikachu', 'spongebob', 'success_kid']
  random_num = random.randint(0, len(image_names) - 1)
  image_url = "images/{}.jpg".format(image_names[random_num])
  try:
    img = Image.open(image_url)
    return img
  except IOError as e:
    print('IOError: {0}'.format(e))
    return None

# Get text from computer microphone using Google Speech Recognition
def get_txt_from_speech():
  initial_txt = SAMPLE_TEXT
  txt = textwrap.fill(initial_txt, width=40)
  return txt

# Add the text on the image and return final image
def overlay_text_on_image(img, txt):
  width, height = img.size
  draw = ImageDraw.Draw(img)

  # Draw black box at the bottom and add wrapped text
  font = ImageFont.truetype(FONT_TYPE, int(height/20))
  draw.rectangle(((0, height*(8/10)), (width, height*(19/20))), fill='black')
  draw.text((width/10, height*(8/10)), txt, fill='white', font=font)

  img.save(IMAGE_URL)
  return

if __name__ == '__main__':
  # First get the random image
  img = get_rand_img()

  store_globals(img)

  # Second get the text from the user microphone
  txt = get_txt_from_speech()

  # Ensure that both the txt and img are valid
  if img != None and txt != None:
    overlay_text_on_image(img, txt)
    meme = Image.open(IMAGE_URL)
    meme.show()
  else:
    print('Error: Image or text not valid')

# obtain audio from the microphone
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)
# try:
#     # for testing purposes, we're just using the default API key
#     # to use another API key, use
#     # `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
#     # instead of `r.recognize_google(audio)`
#     print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))
