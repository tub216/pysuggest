= About = 

Python wrapper for the SUGGEST library.

More about the wrapped library (SUGGEST):

SUGGEST is a Top-N recommendation engine that implements a variety of recommendation algorithms. Top-N recommender systems, a personalized information filtering technology, are used to identify a set of N items that will be of interest to a certain user. In recent years, top-N recommender systems have been used in a number of different applications such to recommend products a customer will most likely buy; recommend movies, TV programs, or music a user will find enjoyable; identify web-pages that will be of interest; or even suggest alternate ways of searching for information.

The algorithms implemented by SUGGEST are based on collaborative filtering that is the most successful and widely used framework for building recommender systems. SUGGEST implements two classes of collaborative filtering-based top-N recommendation algorithms, called user-based and item-based.

= Credits =

Python wrapper by Ricardo Niederberger Cabral (ricardo.cabral at imgseek.net). 

Recommendation engine by George Karypis (http://glaros.dtc.umn.edu/gkhome/suggest/overview).

= Usage instructions =

Just import the "suggest" python module.

See test_suggest.py as an example.

= Build instructions =

== Linux ==

Build requirements:

 * libsuggest.a, which can be obtained from the Linux download at http://glaros.dtc.umn.edu/gkhome/suggest/overview 
 * python
 * python-dev
 * gcc
 
Build instructions:

Untar the wrapper tar.gz file.
Copy libsuggest.a to the root of the extracted dir.
Run "python setup.py build"
Copy suggest.so from build/lib* to the root of the extracted dir and name it "_suggest.so"