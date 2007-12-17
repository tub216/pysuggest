#!/usr/bin/env python

from distutils.core import setup, Extension

setup(name='suggest',
      version='1.0',
      description='Python wrapper for the SUGGEST, which is a Top-N recommendation engine that implements a variety of recommendation algorithms for collaborative filtering.',
      author='Python wrapper by Ricardo Niederberger Cabral. Recommendation engine by George Karypis (http://glaros.dtc.umn.edu/gkhome/suggest/overview)',
      author_email='ricardo.cabral at imgseek.net',
      #url='http://www.python.org/sigs/distutils-sig/',
      #packages=['distutils', 'distutils.command'],
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
