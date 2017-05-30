Rotten Tomatoes CLI
===================

-  `Introduction <https://github.com/jaebradley/rotten_tomatoes_cli#introduction>`__
-  `Install <https://github.com/jaebradley/rotten_tomatoes_cli#install>`__
-  `Search <https://github.com/jaebradley/rotten_tomatoes_cli#search>`__
-  `Harry Potter
   Example <https://github.com/jaebradley/rotten_tomatoes_cli#harry-potter-example>`__
-  `Master of None
   Example <https://github.com/jaebradley/rotten_tomatoes_cli#master-of-none-example>`__
-  `TV <https://github.com/jaebradley/rotten_tomatoes_cli#tv>`__
-  `Browse Popular TV Shows
   Example <https://github.com/jaebradley/rotten_tomatoes_cli#browse-popular-tv-shows-example>`__
-  `Movies <https://github.com/jaebradley/rotten_tomatoes_cli#movies>`__
-  `Streaming <https://github.com/jaebradley/rotten_tomatoes_cli#streaming>`__

   -  `Upcoming movies on Netflix or Amazon Prime with a minimum rating
      of
      90 <https://github.com/jaebradley/rotten_tomatoes_cli#upcoming-movies-on-netflix-or-amazon-prime-with-a-minimum-rating-of-90>`__

-  `Theaters <https://github.com/jaebradley/rotten_tomatoes_cli#theaters>`__

   -  `Action movies in theaters with a minimum rating of
      90 <https://github.com/jaebradley/rotten_tomatoes_cli#action-movies-in-theaters-with-a-minimum-rating-of-90>`__

Introduction
------------

-  Search for movies and tv shows on Rotten Tomatoes from the command
   line
-  Browse movies in theaters or on various streaming platforms like
   Netflix and Amazon Prime

Install
-------

``pip install rotten_tomatoes_cli``

Search
------

``rotten search {term}``

Harry Potter Example
~~~~~~~~~~~~~~~~~~~~

``rotten search "Harry Potter"``

.. figure:: http://imgur.com/MNAwVxI.png
   :alt: alt-text

   alt-text

Master of None Example
~~~~~~~~~~~~~~~~~~~~~~

``rotten search "Master of None"``

.. figure:: http://imgur.com/FNPejbR.png
   :alt: alt-text

   alt-text

TV
--

``rotten tv {category}``

Category Argument \* ``new`` (default) \* ``popular`` \* ``fresh``

Browse Popular TV Shows Example
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``rotten tv popular``

.. figure:: http://imgur.com/3PYkLuz.png
   :alt: alt-text

   alt-text

Movies
------

Options: \* ``--minimum_rating`` / ``-l`` \* Minimum allowable Rotten
Tomatoes score \* Default: ``70`` \* ``--maximum_rating`` / ``-h`` \*
Maximum allowable Rotten Tomatoes score \* Default: ``100`` \*
``--certified_fresh`` / ``-f`` \* Boolean flag that represents whether
or not to only show "Certified Fresh" movies \* Default: ``True`` \*
``--service`` / ``-s`` \* Filter by specified streaming services \*
Default: All services \* Can specify multiple services \* Values: \*
``amazon`` \* ``prime`` \* ``hbo`` \* ``itunes`` \* ``netflix`` \*
``vudu`` \* ``fandango`` \* ``--genre`` / ``-g`` \* Filter by specified
genres \* Default: All genres \* Can specify multiple genres \* Values:
\* ``action`` \* ``animation`` \* ``art_and_foreign`` \* ``classics`` \*
``comedy`` \* ``documentary`` \* ``drama`` \* ``horror`` \* ``family``
\* ``mystery`` \* ``romance`` \* ``scifi`` \* ``--sort_by`` \* Sort
results by specified value \* Default: ``popularity`` \* Values: \*
``popularity`` \* ``release``

Streaming
~~~~~~~~~

``rotten movies streaming {category}``

Category Argument \* ``new`` (default) \* ``all`` \* ``top`` \*
``upcoming`` \* ``fresh``

Upcoming movies on Netflix or Amazon Prime with a minimum rating of 90
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``rotten movies streaming upcoming -l 90 -s netflix -s prime``

.. figure:: http://imgur.com/7aP33au.png
   :alt: alt-text

   alt-text

Theaters
~~~~~~~~

``rotten movies theaters {category}``

Category Argument \* ``opening`` (default) \* ``playing`` \*
``upcoming`` \* ``fresh``

Action movies in theaters with a minimum rating of 90
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

``rotten movies theaters playing -l 90 -g action``

.. figure:: http://imgur.com/vU54rQr.png
   :alt: alt-text

   alt-text
