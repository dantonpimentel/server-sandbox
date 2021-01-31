from copy import deepcopy

from gunicorn.app.base import BaseApplication


class GunicornServer(BaseApplication):
    def __init__(self, app, config):
        self.options = deepcopy(config)
        self.application = app
        super().__init__()

    def load_config(self):
        config = {key: value for key, value in self.options.items()
                  if key in self.cfg.settings and value is not None}
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application
