SUGGEST is a Top-N recommendation engine that implements a variety of recommendation algorithms for collaborative filtering.

Python wrapper by Ricardo Niederberger Cabral (ricardo.cabral at imgseek.net).

Recommendation engine by George Karypis (http://glaros.dtc.umn.edu/gkhome/suggest/overview).

More about the wrapped library (SUGGEST):

_SUGGEST is a Top-N recommendation engine that implements a variety of recommendation algorithms. Top-N recommender systems, a personalized information filtering technology, are used to identify a set of N items that will be of interest to a certain user. In recent years, top-N recommender systems have been used in a number of different applications such to recommend products a customer will most likely buy; recommend movies, TV programs, or music a user will find enjoyable; identify web-pages that will be of interest; or even suggest alternate ways of searching for information._

_The algorithms implemented by SUGGEST are based on collaborative filtering that is the most successful and widely used framework for building recommender systems. SUGGEST implements two classes of collaborative filtering-based top-N recommendation algorithms, called user-based and item-based._

# Building #

Can be built on Windows and Unix compatible systems with

```
python setup.py build
```

Visual Studio 2003 is needed for building on windows.
Linux (Ubuntu 32bits) shared library is provided.

# FAQ #

## Segmentation faults when initializing the prediction model ##

Due to a SUGGEST undocumented detail, you must feed item ids into the item[.md](.md) array in ascending order.