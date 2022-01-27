import setuptools

with open("README.md", "r") as fh:
   long_description = "Test Lib"

setuptools.setup(
   name="package1",
   version="0.0.2",
   author="paul",
   author_email="test@test.com",
   description="A fake library",
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