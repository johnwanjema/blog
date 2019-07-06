# Personal Blog

## Description

 personal blog where you can  express your ideas and opinions.

## Created by John Wanjema 6/6/2019

## BDD

#### Link to deployed site

....

## Setup and installations

#### Prerequisites

1. [Python3.6](https://www.python.org/downloads/)
   
2. [virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. [Pip](https://pip.pypa.io/en/stable/installing/)

#### Technologies used

    - Python 3.6
    - HTML
    - Bootstrap 4
    - Heroku
    - Postgresql
    - Flask

#### Clone the Repo and rename it to suit your needs.

```bash
git clone https://github.com/johnwanjema/blog
```

#### Initialize git and add the remote repository

```bash
git init
```

```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment

```bash
python3.6 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables

Create a `.env` file and paste paste the following filling where appropriate:

```
SECRET_KEY='<Secret_key>'
export MAIL_USERNAME=<Your Email Address>
export MAIL_PASSWORD=<Your Email Password>
DEBUG=True
```

#### Install dependancies

Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Run chmod a+x start.py

```bash
chmod a+x start.py
```

#### Run the app

```bash
./start.sh
```

#### Access the application through localhost:5000

Open [localhost:5000](http://127.0.0.1:5000/)

## Contributing

Please read this [comprehensive guide](https://opensource.guide/how-to-contribute/) on how to contribute. Pull requests are welcome :-)

## Bugs

Create an issue mentioning the bug you have found

#### Known bugs

- N/A

## Support and contact details

Contact [John Wanjema](jonwanjema@gmail.com) for further help/support

### License

[MIT](https://github.com/johnwanjema/blog/blob/master/LICENSE)

Copyright (c)2019 **John Wanjema**
