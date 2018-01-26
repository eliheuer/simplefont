SimpleFont
==========

A simple fork of `TruFont <https://github.com/trufont/trufont>`__. 

.. image:: Lib/simplefont/resources/app.png

Getting started
===============

installation instructions
-------------------------

If you have Python3 and Git installed and want to quickly install 
and run SimpleFont in a virtual environment, open a terminal and enter 
the following chain of commands as one line:

``python3 -m venv simplefont-venv && source simplefont-venv/bin/activate && cd simplefont-venv && git clone https://github.com/eliheuer/simplefont.git && cd simplefont && pip install --upgrade -r requirements.txt && pip install --editable . && simplefont``

Or, as separate lines, making modifications when needed:

   .. code::

      python3 -m venv simplefont-venv
      source simplefont-venv/bin/activate
      cd simplefont-venv
      git clone https://github.com/eliheuer/simplefont.git
      cd simplefont
      pip install --upgrade -r requirements.txt
      pip install --editable .
      simplefont

Python3 and Git Installation Instructions
-----------------------------------------

1. Install **Python 3.5** (or later):

   -  Linux: It's usually packaged with the OS,
   -  Run ``python3 --version`` to see what you have installed. 

2. Install **Git 2.1** (or later):

   -  Ubuntu/Debian Linux, run: ``apt install git``
   -  Arch Linux, run: ``pacman -Syu git``
