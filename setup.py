import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alarmpy",
    version="1.0.1",
    author="Yuval Adam",
    author_email="_@yuv.al",
    description="Pikud Ha'oref Alarm Tracking",
    license="GPLv3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yuvadm/alarmpy",
    project_urls={
        "Bug Tracker": "https://github.com/yuvadm/alarmpy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    py_modules=["alarmpy"],
    python_requires=">=3.6",
    install_requires=["requests", "click"],
    entry_points={"console_scripts": ["alarmpy = alarmpy:cli"]},
)
