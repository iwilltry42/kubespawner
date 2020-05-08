FROM jupyterhub/k8s-hub:0.9.0
COPY . /app
USER root
RUN pip3 uninstall -y jupyterhub-kubespawner && cd /app && python3 setup.py install && python3 setup.py build
USER jovyan