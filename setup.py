from setuptools import setup, find_packages

__version__ = '1.2dev'

setup(
    name='plone.postpublicationhook',
    version=__version__,
    description="Zope post-publication hook.",
    long_description=(open("README.rst").read() + "\n" +
                      open("CHANGES.rst").read()),
    classifiers=[
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Framework :: Zope2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Zope Public License",
    ],
    keywords='',
    author='Zope Foundation and Contributors',
    author_email='zope-dev@zope.org',
    url='http://pypi.python.org/pypi/plone.postpublicationhook',
    license='ZPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['plone'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.event',
        'zope.interface',
        'zope.security',
    ],
    extras_require={
        'Zope2.10': ['ZPublisherEventsBackport'],
    },
)
