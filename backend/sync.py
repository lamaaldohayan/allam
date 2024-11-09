from story import generateStory
from prompt import generate_story_based_on_choice
from image import Generate_image
from audio import generate_audio
import json


async def allam_storyteller(story_type, subType, story, name, age):
    enhancement_prompt = generate_story_based_on_choice(story_type, subType, story, name, age)
    allam_story = generateStory(enhancement_prompt)

    
    image = await Generate_image(story_type, subType, allam_story)
    audio = await generate_audio(allam_story)

    
    output = {
        "story": allam_story,
        "image": image,  
        "audio": audio   
    }

    return output






