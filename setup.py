from setuptools import setup, find_packages

setup(
    name="comfy-image-switch",
    version="1.0.0",
    description="An image source switch node for ComfyUI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Ben Staniford",
    author_email="no@spam.com",
    url="https://github.com/yourusername/comfy-image-switch",
    packages=find_packages(),
    install_requires=[
        "torch",
        "torchvision",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)
