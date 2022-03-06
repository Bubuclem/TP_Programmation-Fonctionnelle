Idempotence
===========

.. note::

   En mathématiques et en informatique, l'idempotence signifie qu'une opération a le même effet qu'on l'applique une ou plusieurs fois

Exemple de fonction idempotence

.. code-block:: python
   :emphasize-lines: 3,5

   def __url_replace(self,url) -> str:
      return url.replace(" ","%20")

La fonction retourne toujours une chaine qui remplace les espaces dans une URL fournit, par des %20 pour les requêtes HTTP.

.. code-block:: python
   :emphasize-lines: 3,5

    def __url_request(self,url):
        return requests.get(url,headers={'content-type': 'application/json'})

La fonction effectue un GET sur l'URL fournit.