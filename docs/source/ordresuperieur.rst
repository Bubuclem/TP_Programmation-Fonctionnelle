Fonctions d’ordre supérieur
===========================

.. note::

   En mathématiques et en informatique, les fonctions d'ordre supérieur sont des fonctions qui ont au moins une des propriétés suivantes :
      • elles prennent une ou plusieurs fonctions en entrée
      • elles renvoient une fonction

Exemple de fonction d’ordre supérieur
-------------------------------------

.. code-block:: python
   :emphasize-lines: 3,5

   def __json_parsing(self,json,callback):
      self.kind       = json.get('kind')
      self.totalItems = json.get('totalItems')
      ([ self.items.append(Google_Books_Items(item)) for item in json['items'] ])

      callback()

La fonction __json_parsing prend une fonction en enter pour effectuer un callback après le parsing d'un json

.. code-block:: python
   :emphasize-lines: 3,5

   function_item_Intitle = FunctionItem("Intitle", self.book.get_intitle, ["Enter Intitle"])

La fonction FunctionItem prend également une fonction en enter pour effectuer le traitement affilié s'il est appelé