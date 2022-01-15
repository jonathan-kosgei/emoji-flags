from distutils.core import setup
import os

def read(fname):
    """Utility function to get README.rst into long_description.

    ``long_description`` is what ends up on the PyPI front page.
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = 'emojiflags',
  packages = ['emojiflags'],
  version = '0.1.1',
  description = 'Python Package for Country Flag Emojis.',
  author = 'Jonathan Kosgei',
  author_email = 'jonathan@ipdata.co',
  url = 'https://github.com/jonathan-kosgei/emoji-flags',
  download_url = 'https://github.com/jonathan-kosgei/emoji-flags/archive/0.1.0.tar.gz',
  keywords = ['geolocation', 'flags', 'emoji'],
  long_description=read('README'),
  classifiers = [],
)