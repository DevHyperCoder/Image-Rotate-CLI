# Image Rotate CLI

This is a simple Python CLI to rotate images using `PIL` 

## How to run?
1. Clone this repo: `git clone https://github.com/DevHyperCoder/Image-Rotate-CLI.git`
2. Make a virtualenv `python -m virtualenv venv`
3. Install the required dependencies `pip install -r requirements.txt`
4. Run the file `python main.py` with the arguments

## Arguments
1. `file-dir` : The directory where the script can find the images Required
2. `degree` : The degree to rotate all the images to. Defaults to `-270` Optional
3. `extension` : The extension of all the files Defaults to `jpg` Optional (Requires the degree to be specified) (CAN NOT be used to change the OUTPUT file's extension)

## Examples
1. Just with a `file-dir`:
   `python main.py ./images` Here `./images` is the directory
2. With a degree
   `python main.py ./images/ -90` Rotate each image to `-90` degrees
3. With a extension
   `python main.py ./images/ -90 png` Useful to only rotate the png images