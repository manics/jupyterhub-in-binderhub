import os

c.JupyterHub.port = int(os.getenv("PORT"))
c.JupyterHub.base_url = os.getenv("BASEURL")

c.JupyterHub.authenticator_class = "dummy"
c.JupyterHub.spawner_class = "simple"
