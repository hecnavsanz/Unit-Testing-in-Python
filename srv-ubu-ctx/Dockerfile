FROM ubuntu:22.04 AS ubuntulinux

ENV container=docker
ENV LC_ALL=C
ENV DEBIAN_FRONTEND=noninteractive

# change root password
RUN echo -n 'root:UnitTestingPython_4ALL' | chpasswd

# update the system and setup systemd
RUN apt-get update -y; \
    apt-get install -y systemd systemd-sysv; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/* \
           /tmp/* \
           /var/tmp/*; \
    cd /lib/systemd/system/sysinit.target.wants/; \
    rm $(ls | grep -v systemd-tmpfiles-setup); \
    rm -f /lib/systemd/system/multi-user.target.wants/* \
          /etc/systemd/system/*.wants/* \
          /lib/systemd/system/local-fs.target.wants/* \
          /lib/systemd/system/sockets.target.wants/*udev* \
          /lib/systemd/system/sockets.target.wants/*initctl* \
          /lib/systemd/system/basic.target.wants/* \
          /lib/systemd/system/anaconda.target.wants/* \
          /lib/systemd/system/plymouth* \
          /lib/systemd/system/systemd-update-utmp*

# setup support for ssh, git and other tools
RUN echo "America/New_York" > /etc/timezone; \
    apt-get update -y; \
    apt-get install openssh-server openssh-client sshpass git-all sudo net-tools iproute2 iputils-ping lsof unzip wget curl vim bat jq dos2unix -y; \
    systemctl enable apache2

# setup labs user and group
RUN groupadd labs; \
    useradd --create-home -s /bin/bash -g labs labs; \
    echo -n 'labs:UnitTestingPython_4ALL' | chpasswd; \
    echo 'labs ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/labs; \
    chmod 440 /etc/sudoers.d/labs; \
    mkdir -p /home/labs/.ssh; \
    chmod 700 /home/labs/.ssh; \
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== labs insecure public key" > /home/labs/.ssh/authorized_keys; \
    chmod 600 /home/labs/.ssh/authorized_keys; \
    sed -i -e 's/Defaults.*requiretty/#&/' /etc/sudoers; \
    sed -i -e 's/\(UsePAM \)yes/\1 no/' /etc/ssh/sshd_config; \
    mkdir -p /home/labs/.local/bin; \
    ln -s /usr/bin/batcat /usr/local/bin/bat; \
    chown -R labs:labs /home/labs; \
    rm -Rf /run/nologin

RUN apt-get -qqy install libnss3-tools openjdk-17-jre-headless; \
    export ARCH=$(dpkg --print-architecture); \
    sed -i 's/securerandom\.source=file:\/dev\/random/securerandom\.source=file:\/dev\/urandom/' /usr/lib/jvm/java-17-openjdk-${ARCH}/conf/security/java.security; \
    groupadd selenium; \
    useradd --create-home -s /bin/bash -g selenium selenium; \
    echo -n 'selenium:UnitTestingPython_4ALL' | chpasswd; \
    echo 'selenium ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/selenium; \
    chmod 440 /etc/sudoers.d/selenium; \
    mkdir -p /home/selenium/.ssh; \
    chmod 700 /home/selenium/.ssh; \
    echo "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== selenium insecure public key" > /home/selenium/.ssh/authorized_keys; \
    chmod 600 /home/selenium/.ssh/authorized_keys; \
    mkdir -p /home/selenium/.local/bin; \
    chown -R selenium:selenium /home/selenium; \
    mkdir -p /opt/selenium /opt/selenium/assets /opt/selenium/secrets /home/selenium/.mozilla /home/selenium/.vnc /home/selenium/.pki/nssdb; \
    certutil -d sql:/home/selenium/.pki/nssdb -N --empty-password; \
    touch /opt/selenium/config.toml; \
    chown -R selenium:selenium /opt/selenium /home/selenium; \
    chmod -R 775 /opt/selenium /home/selenium; \
    wget --no-verbose https://github.com/SeleniumHQ/selenium/releases/download/selenium-4.25.0/selenium-server-4.25.0.jar \
        -O /opt/selenium/selenium-server.jar; \
    chgrp -R 0 /opt/selenium /home/selenium /opt/selenium/assets; \
    chmod -R g=u /opt/selenium /home/selenium /opt/selenium/assets; \
    curl -fL https://github.com/coursier/coursier/releases/download/v2.1.13/coursier.jar > /tmp/cs; \
    chmod +x /tmp/cs; \
    mkdir -p /external_jars; \
    chmod -R 775 /external_jars; \
    java -jar /tmp/cs fetch --classpath --cache /external_jars \
        io.opentelemetry:opentelemetry-exporter-otlp:1.42.1 \
        io.grpc:grpc-netty:1.66.0 io.netty:netty-codec-http:4.1.113.Final > /external_jars/.classpath.txt; \
    chmod 664 /external_jars/.classpath.txt; \
    rm -fr /root/.cache/*

COPY --chown="selenium:selenium" certs/add-cert-helper.sh certs/add-jks-helper.sh /opt/bin/
COPY --chown="selenium:selenium" certs/tls.crt certs/tls.key certs/server.jks certs/server.pass /opt/selenium/secrets/

RUN apt-get -qqy install xvfb libxcb1 xauth pulseaudio x11vnc x11-utils fluxbox eterm hsetroot feh \
    language-pack-en \
    locales \
    libfontconfig \
    libfreetype6 \
    xfonts-scalable \
    xfonts-cyrillic \
    fonts-ubuntu \
    fonts-liberation \
    fonts-ipafont-gothic \
    fonts-wqy-zenhei \
    fonts-tlwg-loma-otf \
    fonts-noto-color-emoji; \
    locale-gen en_US.UTF-8; \
    dpkg-reconfigure --frontend noninteractive locales; \
    apt-get clean; \
    wget -nv -O noVNC.zip \
       "https://github.com/novnc/noVNC/archive/refs/heads/master.zip"; \
    unzip -x noVNC.zip; \
    mv noVNC-master /opt/bin/noVNC; \
    cp /opt/bin/noVNC/vnc.html /opt/bin/noVNC/index.html; \
    rm -f noVNC.zip; \
    wget -nv -O websockify.zip \
      "https://github.com/novnc/websockify/archive/refs/heads/master.zip"; \
    unzip -x websockify.zip; \
    mv websockify-master /opt/bin/noVNC/utils/websockify; \
    rm -f websockify.zip; \
    rm -rf /opt/bin/noVNC/utils/websockify/docker /opt/bin/noVNC/utils/websockify/tests; \
    chmod +x /dev/shm; \
    mkdir -p /tmp/.X11-unix; \
    x11vnc -storepasswd UnitTestingPython_4ALL /home/selenium/.vnc/passwd; \
    chown -R "selenium:selenium" /home/selenium/.vnc; \
    chmod -R 775 /home/selenium/ /tmp/.X11-unix; \
    chgrp -R 0 /home/selenium/ /tmp/.X11-unix; \
    chmod -R g=u /home/selenium/ /tmp/.X11-unix

COPY --chown="selenium:selenium" scripts/start-selenium-node.sh \
      scripts/start-xvfb.sh \
      scripts/start-vnc.sh \
      scripts/start-novnc.sh \
      scripts/generate_config scripts/generate_relay_config /opt/bin/

COPY scripts/selenium_grid_logo.png /usr/share/images/fluxbox/ubuntu-light.png

USER selenium:selenium

RUN /opt/bin/add-jks-helper.sh -d /opt/selenium/secrets; \
    /opt/bin/add-cert-helper.sh -d /opt/selenium/secrets TCu,Cu,Tu

COPY --chown="selenium:selenium" config/config.toml /opt/selenium/

USER root

# initialize ssh
RUN systemctl enable ssh.service

# change working dir for root
WORKDIR /root

CMD ["/lib/systemd/systemd"]
