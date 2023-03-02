from distutils.core import setup

setup(name="tokenish",
      version="0.1",
      description="A simple tool to fill pattern with tokens from file or directory",
      url="https://github.com/VictorMeyer77/tokenish",
      author="Victor Meyer",
      author_email="victor_meyer@outlook.fr",
      packages=["tokenish", "tokenish.lib"],
      python_requires=">=3.6, <4",
      scripts=["bin/tokenish"],
      license="MIT",
      classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "License :: OSI Approved :: MIT License",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX",
            "Programming Language :: Python",
            ],
      )
