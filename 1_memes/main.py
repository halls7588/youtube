from PIL import Image, ImageFont, ImageDraw
import speech_recognition as sr
import random

IMAGE_URL = 'final_img.jpg'
FONT_TYPE = 'sans-serif.ttf'
SAMPLE_TEXT = 'this is a sample text'

# Get random meme image from images folder
def get_rand_img():
  image_names = ['jackie_chan', 'michael_jordan', 'pikachu', 'spongebob', 'success_kid']
  random_num = random.randint(0, len(image_names) - 1)
  image_url = "images/{}.jpg".format(image_names[random_num])
  try:
    img = Image.open(image_url)
    return img
  except IOError:
    print('IOError')
    return None

# TODO: Get text from computer microphone using Google Speech Recognition
def get_txt_from_speech():
  return SAMPLE_TEXT

# Add the text on the image and return final image
def overlay_text_on_image(img, txt):
  width, height = img.size
  draw = ImageDraw.Draw(img)
  # font = ImageFont.truetype('arial.ttf', 16)
  # font = ImageFont.load('arial.pil')
  # draw.text((0, 0), txt, (255,255,255), font=font)
  draw.text((width/4, height*4/5), txt, fill=(255, 255, 255, 255))
  img.save(IMAGE_URL)
  return

if __name__ == '__main__':
  # First get the text from the user microphone
  txt = get_txt_from_speech()

  # Second get the random image
  img = get_rand_img()

  # Ensure that both the txt and img are valid
  if img != None and txt != None:
    overlay_text_on_image(img, txt)
    final_img = Image.open(IMAGE_URL)
    final_img.show()

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

# images = ['jackie_chan', 'mj', 'pika', 'spongebob', 'success_kid']
# try:
#   #Relative Path
#   #Image on which we want to paste
#   print('wtf')
#   img = Image.open("images/mj.jpg")
#   img.show()
# except IOError:
#   print('err')