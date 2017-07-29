from setuptools import setup

setup(
    name='lektor-amp',
    version='0.1',
    author=u'Matthias Rebel',
    author_email='webmaster@rebeling.net',
    license='MIT',
    py_modules=['lektor_amp'],
    entry_points={
        'lektor.plugins': [
            'amp = lektor_amp:AmpPlugin',
        ]
    }
)
