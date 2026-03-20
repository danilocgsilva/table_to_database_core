FROM debian:bookworm-slim

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install git -y
RUN apt-get install vim -y
COPY ./install_requirements_and_keep.sh .
RUN chmod +x ./install_requirements_and_keep.sh

CMD /install_requirements_and_keep.sh
# CMD while : ; do sleep 1000; done