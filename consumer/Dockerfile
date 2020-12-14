FROM python:slim-stretch

WORKDIR /srv

# UPDATE CACHE AND INSTALL PACKAGES
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    jq \
    make \
    tzdata \
    gcc \
    g++ \
    ca-certificates \
    wget && \
    update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# INSTALL AWS DEPS
RUN cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    echo "America/Sao_Paulo" > /etc/timezone && \
    pip install awscli

ADD requirements.txt /srv/

# ADD APP
ADD . .

# INSTALL FROM REQUIREMENTS FILE
RUN pip install -U pip && pip install -r requirements.txt

# ENTRYPOINT
CMD ["python", "app.py"]