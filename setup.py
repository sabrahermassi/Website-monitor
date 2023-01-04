import setuptools

with open("README.rst", 'r') as f:
    long_description = f.read()

setuptools.setup(
   name='Website-checker-Database-writer',
   version='1.0.0',
   description='A periodic website checker that saves website check results into a database',
   long_description=long_description,
   author='Sabra Hermassi',
   author_email='sabra.herm@gmail.com',
   url="https://github.com/sabrahermassi/Website-checker-Database-writer",
   packages=setuptools.find_packages('src'),
   package_dir={'':'src'},
   install_requires=['PyYAML', 'kafka-python', 'psycopg2-binary', 'pytest', 'requests']
)
