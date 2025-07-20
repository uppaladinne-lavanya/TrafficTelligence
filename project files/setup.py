from setuptools import setup, find_packages

setup(
    name="TrafficTelligence",
    version="1.0.0",
    description="AI-powered traffic volume estimation and visualization system",
    author="Your Team Name",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "flask",
        "flask-cors",
        "numpy",
        "pandas",
        "scikit-learn",
        "tensorflow",  # or pytorch if used
        "matplotlib",
        "plotly",
        "requests",
        "opencv-python",  # if using video feed
    ],
    entry_points={
        "console_scripts": [
            "traffic-telligence=traffic_telligence.app:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Flask",
        "Intended Audience :: Developers",
    ],
)