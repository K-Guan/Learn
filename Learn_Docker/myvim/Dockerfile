FROM ubuntu:latest

MAINTAINER Kevin Guan <KevinGuan.gm@gmail.com>


ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y sudo vim git fontconfig && \
    apt-get clean && \
    apt-get autoclean


RUN useradd kevin && \
    echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers && \
    cp /usr/share/zoneinfo/America/Los_Angeles /etc/localtime && \
    dpkg-reconfigure locales && \
    locale-gen en_US.UTF-8 && \
    /usr/sbin/update-locale LANG=en_US.UTF-8

WORKDIR /home/kevin
ENV HOME /home/kevin
ENV LC_ALL en_US.UTF-8

RUN chown -R kevin:kevin $HOME
USER kevin

# setup pathogen vim plugin manager
RUN mkdir -p $HOME/.vim/autoload $HOME/.vim/bundle $HOME/.vim/colors
ADD https://raw.githubusercontent.com/tpope/vim-pathogen/master/autoload/pathogen.vim $HOME/.vim/autoload/pathogen.vim

# setup vim color theme
ADD https://raw.githubusercontent.com/tomasr/molokai/master/colors/molokai.vim $HOME/.vim/colors/molokai.vim

# setup vimrc
ADD https://raw.githubusercontent.com/K-Guan/private/master/config/vimrc $HOME/.vimrc

# setup vim plugins
WORKDIR $HOME/.vim/bundle
RUN \
    git clone --depth=1 https://github.com/mbbill/undotree && \
    git clone --depth=1 https://github.com/terryma/vim-multiple-cursors && \
    git clone --depth=1 https://github.com/tpope/vim-fugitive && \
    git clone --depth=1 https://github.com/easymotion/vim-easymotion && \
    git clone --depth=1 https://github.com/kien/ctrlp.vim && \
    git clone --depth=1 https://github.com/tacahiroy/ctrlp-funky.git && \
    git clone --depth=1 https://github.com/kshenoy/vim-signature && \
    git clone --depth=1 https://github.com/tpope/vim-repeat.git && \
    git clone --depth=1 https://github.com/klen/python-mode && \
    git clone --depth=1 https://github.com/ConradIrwin/vim-bracketed-paste && \
    git clone --depth=1 https://github.com/kien/rainbow_parentheses.vim && \
    git clone --depth=1 https://github.com/bling/vim-airline && \
    git clone --depth=1 https://github.com/Glench/Vim-Jinja2-Syntax && \
    git clone --depth=1 https://github.com/gorodinskiy/vim-coloresque

WORKDIR $HOME


# Powerline fonts
RUN mkdir -p $HOME/.fonts $HOME/.config/fontconfig/conf.d
ADD https://github.com/Lokaltog/powerline/raw/develop/font/PowerlineSymbols.otf $HOME/.fonts/PowerlineSymbols.otf
ADD https://github.com/Lokaltog/powerline/raw/develop/font/10-powerline-symbols.conf $HOME/.config/fontconfig/conf.d/10-powerline-symbols.conf 

RUN sudo chown -R kevin:kevin $HOME
RUN fc-cache -vf $HOME/.fonts/
CMD vim
