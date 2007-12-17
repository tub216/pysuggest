#!/usr/bin/env python

from distutils.core import setup, Extension

setup(name='pysuggest',
      version='1.0',
      description='Python wrapper for the SUGGEST, which is a Top-N recommendation engine that implements a variety of recommendation algorithms for collaborative filtering.',
      
      author='Python wrapper by Ricardo Niederberger Cabral. Recommendation engine by George Karypis (http://glaros.dtc.umn.edu/gkhome/suggest/overview)',
      author_email='ricardo.cabral at imgseek.net',      
      url='http://code.google.com/p/pysuggest/',
      download_url='http://code.google.com/p/pysuggest/downloads/list',
      long_description="""Python wrapper by Ricardo Niederberger Cabral (ricardo.cabral at imgseek.net). 

Recommendation engine by George Karypis (http://glaros.dtc.umn.edu/gkhome/suggest/overview).

More about the wrapped library (SUGGEST):

SUGGEST is a Top-N recommendation engine that implements a variety of recommendation algorithms. Top-N recommender systems, a personalized information filtering technology, are used to identify a set of N items that will be of interest to a certain user. In recent years, top-N recommender systems have been used in a number of different applications such to recommend products a customer will most likely buy; recommend movies, TV programs, or music a user will find enjoyable; identify web-pages that will be of interest; or even suggest alternate ways of searching for information.

The algorithms implemented by SUGGEST are based on collaborative filtering that is the most successful and widely used framework for building recommender systems. SUGGEST implements two classes of collaborative filtering-based top-N recommendation algorithms, called user-based and item-based.
      """,
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Intended Audience :: Science/Research',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: POSIX',
                   'Operating System :: Microsoft',
                   ],
      scripts=['test_suggest.py',],
      #packages=['distutils', 'distutils.command'],
      #data_files=[('', ['_suggest.so']),],
      py_modules = ['suggest', ],
      ext_modules = [Extension('suggest', ['suggest.i'],
                               libraries=['suggest'],
                               library_dirs=['.'], 
                               #include_dirs=includes, 
                               #define_macros=macros,
                               #extra_compile_args=['-m32'], 
                               #language=lang, 
                               #swig_opts=['-c++']
                               )
      ],      
     )
