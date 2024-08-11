from django.apps import AppConfig
import os
if os.path.exists("env.py"):
  import env 


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals