FROM jupyterhub/k8s-singleuser-sample:0.9.0
COPY . /app
USER root
RUN cd /app && python setup.py install && python setup.py build
USER jovyan