FROM python:3.10-buster

# コンテナにアクセスした際のデフォルトディレクトリ
ARG work_dir="/workspace/"
WORKDIR ${work_dir}

RUN apt-get update \
  && apt-get install -y \
  locales \
  curl \
  git \
  make \
  curl \
  xz-utils \
  file \
  sudo \
  mecab \
  libmecab-dev \
  mecab-ipadic-utf8

RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9

# mecab-ipadic-neologd install
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
  && cd mecab-ipadic-neologd \
  && yes yes | ./bin/install-mecab-ipadic-neologd -n \
  && cd ..


# poetryのインストール
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python && \
  # シンボリックによるpathへのpoetryコマンドの追加
  cd /usr/local/bin && \
  ln -s /opt/poetry/bin/poetry && \
  # 仮想環境を作成しない設定(コンテナ前提のため，仮想環境を作らない)
  poetry config virtualenvs.create false
