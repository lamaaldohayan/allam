from story import generateStory
from prompt import generate_story_based_on_choice
from image import Generate_image
from audio import generate_audio
import json


async def allam_storyteller(type,subType,story,name,age):
  enhancement_prompt=await generate_story_based_on_choice(type,subType,story,name,age)
  allam_story=  generateStory(enhancement_prompt)
  image= Generate_image(type,subType,allam_story)
  audio= generate_audio(allam_story)
  output={
    "story":story,
    "image":image,
    "audio":audio,
  }
  return output






