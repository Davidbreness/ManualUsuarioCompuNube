FROM registry.fedoraproject.org/fedora:44

RUN dnf -y upgrade --refresh && \
    dnf -y install \
    git \
    curl \
    wget \
    vim \
    python3 \
    python3-pip \
    nodejs \
    npm \
    gcc \
    gcc-c++ \
    make && \
    dnf clean all

RUN mkdir -p /workspace && \
    chgrp -R 0 /workspace && \
    chmod -R g=u /workspace

WORKDIR /workspace

CMD ["sleep", "infinity"]
