FROM docker.io/alpine:3.21.3

RUN apk add --no-cache \
    python3

WORKDIR /var/app

COPY ./src /var/app

EXPOSE 8080

ENTRYPOINT [ \
    "python3", \
    "-m", \
    "http.server", \
    "--bind", \
    "0.0.0.0", \
    "8080" \
]
