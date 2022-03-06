Idempotence
===========

.. note::

   En mathématiques et en informatique, l'idempotence signifie qu'une opération a le même effet qu'on l'applique une ou plusieurs fois

.. code-block:: python
   :emphasize-lines: 3,5

   def __url_replace(self,url) -> str:
      return url.replace(" ","%20")