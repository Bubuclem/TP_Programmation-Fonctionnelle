Fonctions pures
===============

.. note::

   En programmation informatique, une fonction pure est une fonction qui possède les propriétés suivantes:
      • Sa valeur de retour est la même pour les mêmes arguments
      • Son évaluation n'a pas d'effets de bord

Exemple de fonction pure
------------------------

.. code-block:: python
   :emphasize-lines: 3,5

Exemple de fonctions impures
----------------------------

.. code-block:: python
   :emphasize-lines: 3,5

   def f() -> int:
      return 0

.. code-block:: python
   :emphasize-lines: 3,5

   def f( i ) -> int:
      return i

.. code-block:: python
   :emphasize-lines: 3,5

   def f():
      i = 0
      return i+1

.. code-block:: python
   :emphasize-lines: 3,5

   def f():
      return +1