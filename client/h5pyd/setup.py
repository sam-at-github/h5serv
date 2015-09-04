from setuptools import setup
# run:
#   setup.py install
# or (if you'll be modifying the package):
#   setup.py develop
setup(name='h5pyd',
      version='0.1',
      description='h5py compatible client lib for h5serv',
      url='http://github.com/HDFGroup/h5serv',
      author='John Readey',
      author_email='jreadey at hdfgrouup dot org',
      license='BSD',
      packages = ['h5pyd', 'h5pyd._hl'],
      requires = ['h5py (>=2.5.0)'],
      install_requires = ['h5py>=2.5.0', 'six'],
      setup_requires = ['h5py>=2.5.0', 'pkgconfig', 'six'],
      zip_safe=False)
