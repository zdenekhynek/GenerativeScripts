GenerativeScripts
=================

Little scripts helping exploring generative art.

IMAGESHUFFLER.PY

A python code written after reading tutorial on manualy editing JPEGs with plain text editing, sort of blind image hacking. http://www.computerarts.co.uk/tutorials/break-jpeg-code

The ImageShuffler module will go through the JPEG images line by line, cut random lines and paste them somewhere else further down the road. The new image is created with a name of the inputted image and added timestamp of processing.


Sample usage - with default parameters: 

python ImageShuffler.py some_image.jpg

Sample usage - with parameters: 

python ImageShuffler.py some_image.jpg shuffleStart shuffleLen shuffleGap shuffleCount randomize

Parameters explained:

some_image.jpg - url to the image to be processed

shuffleStart - number of lines that won't be touched by shuffler ( should be above 80, because the first roughly eighty lines are JPEG header, if you messed with them, image won't be readible )

shuffleLen - how many lines will be cutted and placed somewhere else

shuffleGap - distance between cutting and pasting lines

shuffleCount - how many times should be cutting and pasting process repeated

randomize - flash whether should be the cutted lines shuffle between themselves







