import setuptools

setuptools.setup(
        name='UlozitTutoPiesen',
        version='4.0.0',
         classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
                     ],
        packages=setuptools.find_packages(),
        install_requires=[
                    'youtube_dl',
                    'youtube_search',
                    'spotipy',
                    #'ffmpeg'
                    ],
        description=('Toto je skript v jazyku Python, ktorý veľmi ľahko sťahuje skladby a dokonca aj zoznamy skladieb zo služieb Spotify a YouTube'),
        scripts=['utp'],
        url='https://github.com/vianoce/UlozitTutoPiesen',
        author='Stefan jancar'
    )
