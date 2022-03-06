Immutabilité
============

.. note::

   Un objet immuable, en programmation orientée objet et fonctionnelle, est un objet dont l'état ne peut pas être modifié après sa création. Ce concept est à contraster avec celui d'objet variable

Exemple de code immuable

.. code-block:: python
   :emphasize-lines: 3,5

   class API_Google_books():
      URL         = 'https://www.googleapis.com/books/v1/volumes?q='
      kind        = None
      totalItems  = 0
      items       = []

Dans notre classe API_Google_books, la constante URL est immuable 