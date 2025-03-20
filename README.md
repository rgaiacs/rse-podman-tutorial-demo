# Demo of Podman

This project illustrates how to use Podman.

## Usage

```
podman kube play play.yml
```

will

1. build the container images,
2. create a pod,
3. create the containers,
4. mount the volumes into the containers,
5. start the containers.

You can access http://localhost:8080/ from your web browser.

Changes in `demo.gesis.org/src/index.html` and `api.demo.gesis.org/src/app.py` take effect imediatly because the the files are mounted into the containers.

Changes in `demo.gesis.org/Dockerfile` and `api.demo.gesis.org/Dockerfile` requires the recreation of the pod and containers by running

```
podman kube play --replace --build play.yml
```
