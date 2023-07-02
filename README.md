# hmtaipy - Python API Wrapper for hmtai

pyhmtai is a Python library that serves as an API wrapper for hmtai, a service that provides random anime images based on various categories. This wrapper allows you to easily integrate hmtai functionality into your Python applications.

## Installation

You can install pyhmtai using pip:

```bash
pip install hmtaipy
```
Here's a basic example of how to use pyhmtai:
```
from hmtaipy import pyhmtai

# Create an instance of pyhmtai
hmtai = pyhmtai()

# SFW Example
sfw_image = hmtai.sfw('hug') # OPTIONAL .download()
print(f"SFW Image URL: {sfw_image}")

# NSFW Example
nsfw_image = hmtai.nsfw('hentai') #OPTIONAL .download()
print(f"NSFW Image URL: {nsfw_image}")
```

# Methods
.download()
Downloads the image associated with the current URL. The image will be saved as image.jpg in the current directory. (Next update it will save as the name of the URL

sfw(arg)
Sets the function name for a Safe For Work (SFW) category image. Available SFW functions include:


## SFW (Safe For Work) Categories

| Category         | Category         | Category         |
|------------------|------------------|------------------|
| wave             | hug              | cry              |
| wink             | cuddle           | slap             |
| tea              | five             | glomp            |
| bonk             | happy            | hold             |
| punch            | nom              | smile            |
| poke             | throw            | lick             |
| bully            | bite             | boop             |
| pat              | dance            | like             |
| kiss             | sleep            | nosebleed        |
| kick             | threaten         | tickle           |
| blush            | depression       | wolf_arts        |
| feed             | jahy_arts        | neko_arts        |
| smug             | coffee_arts      | wallpaper        |
|------------------| mobileWallpaper  |------------------|

## NSFW (Not Safe For Work) Categories

| Category         | Category         | Category         |
|------------------|------------------|------------------|
| anal             | hentai           | creampie         |
| ass              | masturbation     | gangbang         |
| bdsm             | public           | footjob          |
| cum              | ero              | boobjob          |
| classic          | orgy             | handjob          |
| pantsu           | elves            | boobs            |
| glasses          | yuri             | thighs           |
| cuckold          | nsfwMobileWallpaper                 | ahegao           |
| blowjob          | nsfwNeko                 | pussy            |
| tentacles        |                  | uniform          |
| gif              |                  | zettaiRyouiki    |

# Information

If you want to help to the repository open an issues, or do a pull requests 
