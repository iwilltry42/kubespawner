from jupyterhub.singleuser import SingleUserNotebookApp
from jupyterhub.utils import random_port, url_path_join
from traitlets import default

class KubeSingleUserNotebookApp(SingleUserNotebookApp):
    @default('port')
    def _port(self):
        return random_port()

    def start(self):
        print("RANDOM PORT = ", self.port)
        # Send Notebook app's port number to remote Spawner
        self.hub_auth._api_request(method='POST',
                                   url=url_path_join(self.hub_api_url, 'kubespawner'),
                                   json={'port' : self.port})
        super().start()

def main(argv=None):
    return KubeSingleUserNotebookApp.launch_instance(argv)

if __name__ == "__main__":
    main() 