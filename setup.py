from setuptools import setup, find_packages

"""
Notes:
MODULE_VERSION is read from microscope_automation/version.py.
See (3) in following link to read about versions from a single source
https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-version
"""

setup(name='Imposter blocker',
      version='1',
      description='Imposter Blocker',
      long_description='Phishing site detection',
      author='Imposter Blocker Team',
      author_email='yrkim1998@gmail.com',
      license='None',
      packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    ext_modules=[
            Extension("my_module", ["my_module.c"],
                      include_dirs=[numpy.get_include()]),
        ],
      install_requires=[
          'ipykernel==5.1.2',
          'keyring==18.0.0',
          'greenlet==0.4.15',
          'pathlib2==2.3.5',
          'kiwisolver==1.1.0',
          'Flask_Cors==3.0.8',
          'pytest==5.2.1',
          'docutils==0.15.2',
          'tornado==6.0.3',
          'importlib_metadata==0.23',
          'selenium==3.141.0',
          'zipp==0.6.0',
          'opencv_python==4.1.2.30',
          'pandas==0.25.1',
          'psutil==5.6.3',
          'webdriver_manager==2.3.0',
          'lxml==4.4.1',
          'nose==1.3.7',
          'scipy==1.3.1',
          'pytz==2019.3',
          'Sphinx==2.2.0',
          'cryptography==3.2',
          'blinker==1.4',
          'brotli==1.0.7',
          'cairocffi==1.1.0',
          'dataclasses==0.7',
          'genapi==0.0.8',
          'ipaddr==2.2.0',
          'ipython==7.13.0',
          'lockfile==0.12.2',
          'mtrand==0.1',
          'mypy_extensions==0.4.3',
          'numpy==1.18.3',
          'ordereddict==1.1',
          'pickle5==0.0.9',
          'Pillow==7.1.1',
          'pretty==0.1',
          'protobuf==3.11.3',
          'pyOpenSSL==19.1.0',
          'PyQt5==5.14.2',
          'PySide2==5.14.2',
          'python-dotenv==0.13.0',
          'scikit_learn==0.22.2.post1',
          'shiboken2==5.14.2',
          'simplejson==3.17.0',
          'sip==5.2.0',
          'toml==0.10.0',
          'watchdog==0.10.2',
          'wincertstore==0.2',
          'Cython==0.29.17'
      ])
