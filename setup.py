from distutils.core import setup
setup(
  name = 'fireblocks_sdk',
  packages = ['fireblocks_sdk'],
  version = '0.1.3',
  license='MIT',
  description = 'Fireblocks python SDK',
  url = 'https://github.com/fireblocks/fireblocks-sdk-py',
  download_url = 'https://github.com/fireblocks/fireblocks-sdk-py/archive/v0.1.3.tar.gz',
  keywords = ['Fireblocks', 'SDK'],
  install_requires=[
          'PyJWT==1.7.1',
          'requests==2.22.0',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development',    
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)