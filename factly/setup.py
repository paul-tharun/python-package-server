import setuptools
long_description = "Test Package"

setuptools.setup(
   name="pypi",
   version="0.0.1",
   author="lwpro2",
   author_email="lwpro2",
   description="A pypi for python packages",
   long_description=long_description,
   long_description_content_type="text/markdown",
   url="https://github.com/paul-tharun",
   packages=setuptools.find_packages(),
   classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
   ]
)