import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# Loads the version from package
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from easy_thumbnails_watermark import __version__ as version

setup(
    name='django-easy-thumbnails-watermark-1',
    version=version,
    packages=['easy_thumbnails_watermark'],
    include_package_data=True,
    license='GPLv3 License',
    description='A watermark filter for easy_thumbnails',
    long_description=README,
    url='https://github.com/frague59/django-easy-thumbnails-watermark',
    author='Davide Riccardo Caliendo',
    author_email='frague59@gmail.com',
    install_requires=['easy_thumbnails'],   
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

