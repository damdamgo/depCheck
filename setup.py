from cx_Freeze import setup, Executable
from PIL import PngImagePlugin
from PIL import JpegImagePlugin
from PIL import BmpImagePlugin
from PIL import Image
Image._initialized=2
setup(
    name = "hatefulworld",
    version = "0.1",
    description = "I wish programming was this easy",
    executables = [Executable("dep-check.py")],)
