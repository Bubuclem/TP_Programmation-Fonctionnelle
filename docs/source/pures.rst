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

      def __url_replace(self,url) -> str:
         return url.replace(" ","%20")

Dans la fonction __url_replace, replace est une fonction pure, elle retourne une chaine avec des caractères remplacés par d'autres

.. code-block:: python
   :emphasize-lines: 3,5

   def __init__(self,json) -> None:
      self.title          = json.get('title')
      self.authors        = json.get('authors')
      self.publisher      = json.get('publisher')
      self.publishedDate  = json.get('publishedDate')
      self.description    = json.get('description')

Dans la fonction initialisation, get est une fonction pure, elle retourne une chaine si la valeur recherchée est trouvée

Exemple de fonctions impures
----------------------------

.. code-block:: python
   :emphasize-lines: 3,5

   def f() -> int:
      return i
à cause de la variation de la valeur de retour avec une variable non locale

.. code-block:: python
   :emphasize-lines: 3,5

   def f( i ) -> int:
      return i

à cause de la variation de la valeur de retour avec un argument mutable de type référence

.. code-block:: python
   :emphasize-lines: 3,5

   def f():
      i = 0
      return i+1

à cause de la mutation d'une variable statique locale

.. code-block:: python
   :emphasize-lines: 3,5

   def f():
      return +i

à cause de la mutation d'une variable non locale