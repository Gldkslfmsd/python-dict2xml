from setuptools import setup
import sys
if not (sys.version_info.major == 3 and sys.version_info.minor == 2):
	p = ["dict2xml.no32"]
else:
	p = []

# Setup the project
setup(
      name = "dict2xml"
    , version = '1.4.1'
    , packages = ['dict2xml'] + p

    , extras_require =
      { 'tests' :
        [ 'fudge'
        , 'noseOfYeti>=1.5.0'
        , 'nose'
        ]
      }

    , install_requires =
      [ "six"
      ]

    # metadata
    , author = "Stephen Moore"
    , author_email = "stephen@delfick.com"
    , description = "small script to output xml as a string from a python dictionary"
    , license = "WTFPL"
    )

