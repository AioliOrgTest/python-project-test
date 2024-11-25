FROM 510467250861.dkr.ecr.us-east-1.amazonaws.com/percipio-base:python-3.10-slim

ARG PROJECT_KEY="ENGSEC"
LABEL group=$PROJECT_KEY

ENV HOME /python-project-test
ENV PYTHONUNBUFFERED 1

ADD /app $HOME
WORKDIR $HOME
RUN pip install --upgrade pip
RUN cd ${HOME} && \
    pip install .

EXPOSE 8080

CMD [  "python", "app.py" ]