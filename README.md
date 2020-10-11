[![Build Status](https://travis-ci.org/bertini36/comments-engine.svg?branch=master)](https://travis-ci.org/bertini36/comments-engine)
[![Coverage Status](https://coveralls.io/repos/github/bertini36/comments-engine/badge.svg?branch=master)](https://coveralls.io/github/bertini36/comments-engine?branch=master)
<h3 align="center">
    bertini36/comments-engine 🙊
</h3>
<p align="center">
  <a href="#-environment-setup" target="_blank">
    Installation
  </a>&nbsp;&nbsp;•&nbsp;
  <a href="https://github.com/bertini36/comments-engine/blob/master/serverless.yml" target="_blank">
    Serverless config
  </a>&nbsp;&nbsp;•&nbsp;
  <a href="https://github.com/bertini36/comments-engine/blob/master/Makefile" target="_blank">
    Commands
  </a>
</p>
<p align="center">
A basic comments engine coded just for fun and to use it on my
 <a href="https://albertopou.dev/" target="_blank">blog</a>.
</p>
<p align="center">
Powered by <a href="https://www.serverless.com/" target="_blank">#serverless</a>,
<a href="https://aws.amazon.com/" target="_blank">#aws</a> and
 <a href="https://flask.palletsprojects.com/en/1.1.x/" target="_blank">#flask</a>.
</p>

## ⚙️ Environment Setup

### 🐳 Required tools

1. [Install Docker and Docker Compose](https://www.docker.com/get-started)
2. Clone this project: `git clone https://github.com/bertini36/comments-engine`
3. Move to the project folder: `comments-engine`

### 🔥 Application execution

1. Install all the dependencies and bring up the project with Docker executing: `make build`
2. Run the server: `make serve` (by default Flask runs applications at 5000 port)

## 🚀 Deploy

First configure your AWS credentials and Sentry DSN in `.env` file.
```bash
cp .env-sample .env
```

After this, to update your lambda functions
```bash
make deploy
```

<p align="center">&mdash; Built with :heart: from Mallorca &mdash;</p>
