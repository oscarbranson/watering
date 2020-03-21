from setuptools import setup, find_packages

setup(name='watering',
      version='0.0.1',
      description='Frivolous project for watering plants.',
      long_description_content_type="text/markdown",
      url='https://github.com/oscarbranson/watering',
      author='Oscar Branson',
      author_email='oscarbranson@gmail.com',
      license='MIT',
      packages=find_packages(),
      classifiers=['Development Status :: 4 - Beta',
                   'Programming Language :: Python :: 3',
                   ],
      python_requires='>3.8',
      install_requires=[
        'RPi.GPIO'
                        ],
      zip_safe=False)
