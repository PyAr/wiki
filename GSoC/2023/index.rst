.. title: Google Summer of Code 2023 (ideas)

.. image:: https://raw.githubusercontent.com/PyAr/wiki/master/images/GSoC2022.png
   :align: right
   :height: 44 px
   :width: 44 px

GSoC 2023 PyAr projects
=======================

.. class:: alert alert-info

  | The following are the Python Argentina projects that could participate in Google Summer of Code 2023 (under the `PSF org <https://python-gsoc.org/>`_).
  | Ideas are tentative, please engage with the community strongly to present and improve your original proposals.
  | For + Info see bellow: `About Python Argentina <https://wiki.python.org.ar/GSoC/2023#about-python-argentina-1>`_ (`Contacting Us <https://wiki.python.org.ar/GSoC/2023#contacting-us-1>`_) - `Getting Started <https://wiki.python.org.ar/GSoC/2023#getting-started-1>`_ - `Important notes <https://wiki.python.org.ar/GSoC/2023#important-notes>`__ | `Info En Español <https://wiki.python.org.ar/gsoc>`_

PyZombis
--------

.. image:: https://raw.githubusercontent.com/PyAr/PyZombis/main/_sources/lectures/img/TWP_small.png
   :align: left

A Community course, completely online and interactive, to teach Python to everyone! http://pyar.github.io/PyZombis

The original Brazilian MOOC `"Python for Zumbies" <https://www.slideshare.net/fmasanori/python-for-zombies-first-brazilian-programming-mooc>`_ created by Fernando Masanori has +800k views on `Youtube <https://www.youtube.com/playlist?list=PLUukMN0DTKCtbzhbYe2jdF4cr8MOWClXc>`_  and has taught over 70K students basic Python.
In this Spanish adaptation, all lectures and exercises are done fully online.
There is no need for the student to install python on their computer or to run their own server.

Expected outcomes:
  | Some lectures still need further work to be ported to the web (via `Brython <https://brython.info/>`_, a client-side Python interpreter on top of Javascript), so they can run interactively in the browser (databases, games) using native JS libraries.
  | `Playwright <https://playwright.dev/>`_ end-2-end automated web tests are mandatory for new contributions (+Pull Request checklist & documentation), and we still need coverage for important lessons including API and PyGame.
  | Refactors to the upstream educative platform (`Runestone <https://runestone.academy/ns/books/published/overview/index.html>`_) should be continued and extended, for further information see `PR#1208 <https://github.com/RunestoneInteractive/RunestoneComponents/pull/1208>`_ (a new component: interactive python interpreter for advanced exercises) 

- Project information:
    - `Repository <https://github.com/PyAr/PyZombis>`__ - `Dev tutorial HOW-TO <https://github.com/PyAr/PyZombis/wiki/Development-HOW-TO>`_ (Quick Start)
    - `Good first issues <https://github.com/PyAr/PyZombis/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22>`__ (you can write new E2E `tests <https://github.com/PyAr/PyZombis/tree/main/tests>`_ also!)
    - `PyCon Argentina 2021 video tutorial <https://www.youtube.com/watch?v=BalC7Bp5AFQ>`_ (YouTube)
    - `Academic info <http://bit.ly/pyzombis>`_ (full proposal, course syllabus, pedagogical methodology)

- Project ideas: 
    - Entry-level smaller enhancements for coding exercises and examples (see ticket link for more details)
       - Refactor modular programming chapter `#216 <https://github.com/PyAr/PyZombis/issues/216>`_
       - Modernize MVC & exceptions example app `#217 <https://github.com/PyAr/PyZombis/issues/217>`_
       - Modernize multimedia app & Object-Oriented Programming lecture `#218 <https://github.com/PyAr/PyZombis/issues/218>`_
       - Improve Web development sample with an SPA `#219 <https://github.com/PyAr/PyZombis/issues/219>`_
       - Refactor GUI wrapper for Brython  `#220 <https://github.com/PyAr/PyZombis/issues/220>`_
    - Interactive `SQL python lectures <http://pyar.github.io/PyZombis/master/lectures/TWP42/TWP42_1.html>`__ using javascript (SQLite.js): This includes: refactor of lessons code, add new demo databases, explore IndexedDB, improve & extend exercises with automatic grading / unit tests. Thanks to 2022 GSoC contributor we have a SQLite wrapper and new `chinok database exercises <http://pyar.github.io/PyZombis/main/lectures/TWP42/TWP42_3.html>`_, using it as a starting point to build a final course challenge will be awesome!
    - Enhance Interactive `PyGame lectures <http://pyar.github.io/PyZombis/main/lectures/TWP60/TWP60_2.html>`__ improving `brython-pygame GSoC 2022 fork <https://github.com/shivamshan/pygjs/tree/Pyzombis-pygame>`_ using  `gamejs <http://gamejs.org/showcase.html#pygame-vs-gamejs>`__ (tip: see Brython demos: `bricks <https://www.brython.info/gallery/bricks_py.html>`_ & `3D walker <https://www.brython.info/gallery/3Dwalker.html>`_, a zombie educative game would be great!). Thanks to 2022 GSoC contributor now we have a `zombie chaser game challenge <http://pyar.github.io/PyZombis/main/challenges/Reto03.html>`_ that could be a good starting point!!!
    - BONUS TRACK: Interactive `Web development intro lectures <http://pyar.github.io/PyZombis/master/lectures/TWP65/toctree.html>`__ using `web2py <http://www.web2py.com/>`_ educative framework (capstone project for peer-review final course assignment); this includes a full revision of the lesson and a Kubernetes deployment script to provide a full web2py multi-tenant server where the students can log-in and develop/execute their web exercises
    - ADVANCED: Implement `PyScripter <https://pyscript.net/>`_ component for interactive python excersises (web UI, DB and pygame)

- Project Length: 175 hr each; prefer a full 350 hr proposal including upstream contributions + UI/UX functional revamp and extensive testing

- Difficulty level: Intermediate (basic Python and Web programming experience expected, some gaming + HTML5 design background recommended)

- Technologies involved: Python (sphinx, runestone, pygame, sqlite, pytest-playwrigth, pytest-vcr), Javascript (ajax, DOM)

- Potential mentors: `@reingart <https://github.com/reingart>`_ (coordinator), please contact all mentors in `PyAr GSoC Telegram group <https://t.me/PyArGSoC>`__

- Past GSoC Students projects wrap-up (for reference):
    - `Shivam Shandilya <https://github.com/PyAr/PyZombis/wiki/GSOC-2022-:-PSF-PyZombis-Final-Submission---Shivam-Shandilya>`_ (2022)
    - `Angela Remolina <https://github.com/PyAr/PyZombis/wiki/GSOC-2021-PSF-PyAr-Final-code-submission-PyZombis-Angela-Remolina>`_ (2021)
    - `Leonardo Cumplido <https://github.com/PyAr/PyZombis/wiki/Leonardo-Cumplido-GSoC-2021-Wrap-Up>`_ (2021)
    - `Ybrahin Martinez <https://github.com/PyAr/PyZombis/wiki/GSoC-2021-Final-Code-Ybrahin-Martinez>`_ (2021)

PyAfipWs
--------

.. image:: https://raw.githubusercontent.com/PyAr/pyafipws/py3k/plantillas/logo.png
   :align: left

Library for Developers (integrators and legacy languages interfaces) Tools for Accountants and SMEs (Odoo/OpenERP modules and Tryton Argentina's localization).
Electronic Invoice, Agriculture, Foreign Trade, Taxes, Pharmaceutical, etc.

PyAFIPWs is a widespread standard reference implementation to communicate with Argentina’s government entities, with more than ~2K `users group <https://groups.google.com/g/pyafipws>`_ subscriptions, many bindings to other languages, and used in modules for Open Source ERP localizations (OpenERP, Odoo, Tryton, etc.)

The project has more than 10 years of development history and many accumulated features, covering several webservices and tools.
Initial work has been completed to migrate and modernize the project, but there are many rough edges and enhancements opportunities.

Expected outcomes:
  As it's multi-platform, used by a wide user base of developers (specially from other programming languages), special care must be taken to improve the code-base with  backward compatibility.

  Exhaustive Test coverage is a must to complete the transition.
  Also, installers for Windows users should be migrated and upgraded to support legacy applications (main use case).
  Finally, a webservice simulator could be helpful to ease integration testing and speed-up new developments.

- Project information:
    - `Repository <https://github.com/PyAr/pyafipws/>`__ (`original location <https://github.com/reingart/pyafipws>`_)
    - `Documentation <https://github.com/reingart/pyafipws/wiki/WSFEv1>`__
    - `Good first issues <https://github.com/PyAr/pyafipws/issues>`__

- Project Ideas: 
    - Unit Testing: extend unit tests coverage beyond 70% (including command-line tools, see pending `#107 <https://github.com/PyAr/pyafipws/issues/107>`_ as an example and report.html in GitHub Actions workflow)
    - Automation: `#106 <https://github.com/PyAr/pyafipws/issues/107>`_ to improve packaging) and `#109 <https://github.com/PyAr/pyafipws/issues/107>`_ to build windows installers in continuous integration (see  `Wiki: Install <https://github.com/reingart/pyafipws/wiki/InstalacionCodigoFuente#generaci%C3%B3n-de-instalador>`__ to automate)
    - Webservice simulator:  `#108 <https://github.com/PyAr/pyafipws/issues/108>`_ fake implementation for testing, mimicking government servers (WSDL SOAP based, see `server.py <https://github.com/pysimplesoap/pysimplesoap/blob/master/pysimplesoap/server.py#L539>`__ for an example, and `web2py-app <https://github.com/SistemasAgiles/pyafipws.web2py-app>`_ for a Proof of Concept)

- Project Length: 175 hr (medium) to 350 hr (large, several ideas)

- Difficulty level: Intermediate (basic knowledge in operating systems, network protocols, APIs & testing; Accounting / ERP experience recommended)

- Technologies involved: Python (httplib, xml, webservices, pdf, dbf, pywin32, pytest, pytest-vcr, py2exe), Linux/Windows (packaging/installers/APIs/DLL)

- Potential mentors: `@reingart <https://github.com/reingart>`_ (coordinator) + `@NicolasSandoval <https://github.com/NicolasSandoval>`_, please contact all mentors in `PyAr GSoC Telegram group <https://t.me/PyArGSoC>`__

- Past GSoC Students projects wrap-up (for reference):
    - `Utkarsh Kumar <https://github.com/PyAr/pyafipws/wiki/GSoC-2021:-Final-Summary>`_ (2021)
    - `Nico Sandoval <https://github.com/PyAr/pyafipws/wiki/PyAr-PSF-GSoC-2019-Final-Summary>`_ (2019)

About Python Argentina
======================

We are looking for new Pythonistas!

Help us to foster the development of several open-source community projects. Many are fun and innovative, others are challenging and resolve real-world requirements.

The association was founded aiming to help the Python devs, increase their diversity and outreach, especially overcoming minorities and cultural barriers (mainly socioeconomic, language, gender), serving as an umbrella organization to some ongoing efforts.

Spanish is one of the most spoken languages in the world, and many of our developed tools and libraries are aimed to fill the missing open-source gap.
They can help to learn and further work with Python, either to enthusiasts, professional programmers, or even final users!

Experienced developers, teachers, and volunteers will assist you, guiding you throughout the process with well-defined goals (according to skills and tech background)

Contacting Us
-------------

We're in the Argentina time zone (GMT-3)

* Telegram: https://t.me/PyArGSoC (`invite <https://t.me/+ljnpIYBUMLI3MDAx>`_)
* Google Group: https://groups.google.com/g/pyar-gsoc
* Forum: https://pyar.discourse.group/
* Email: secretaria+gsoc@ac.python.org.ar

NOTE: Spanish is a requisite for many projects, as it is the language used for documentation and community communications. 
On the other side, if you do not speak English fluently, we can help you with translations and guidance (in Spanish, of course).

NOTA: Si hablás Español pero te cuesta el Inglés, te podemos ayudar con las traducciones y redacciones para que puedas participar! No te preocupes, el día a día y documentación en general están en Castellano.

Visitá nuestra GSoC Wiki en Español para más información: https://wiki.python.org.ar/gsoc/

We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.

Queremos que nuestra comunidad sea más diversa: quienquiera que seas, sea cual sea tu origen, te damos la bienvenida

.. _start:

Getting Started
===============

If you want to participate as a contributor, please follow the next guidelines:

Presenting yourself
-------------------

Join the Telegram group and write to about you. 
Please send an introductory email to the Google Group and state clearly:

* Why you want to participate in GSoC, shortly comment your background and expectations
* What project would you prefer: look at this page for ideas
* What is your previous experience, Python skills, Django, hg/git, js, etc.

Fixing a bug!
-------------

* Ask for a simple non-trivial ticket. For example, take a look at CDPedia, PyAfipWs, OpenLex, PyZombis.
* Create a user in GitHub (if you don't have one)
* Fork the project repository and try to fix an issue of your desired project
* Discuss with potential mentors your fix, creating a Pull Request as early as possible!

Writing a Proposal
------------------

* Select a project idea and write a detailed proposal following this `template <https://github.com/python-gsoc/python-gsoc.github.io/blob/master/ApplicationTemplate.md (https://github.com/python-gsoc/python-gsoc.github.io/blob/master/ApplicationTemplate.md)>`_ using Google Docs (in advance!)
* Plan your prepwork for the community bonding period (eg. a Proof-Of-Concept)
* Define a milestones for each evaluation phase (i.e. Prototype, Pilot / Final Demo)
* Plan you weekly work & deliverables (tasking out: high-level goals for each milestone)
* Describe the acceptance criteria ("Minimum Viable Product" of each phase)

Share an early draft and discuss your approach in the group with mentors.
Do not forget to submit your application to the `Google system <https://summerofcode.withgoogle.com/>`_ when ready, some days before the deadline (the server can be overloaded at last minute).

TIPs: read and follow the `GSoC guide <https://google.github.io/gsocguides/student/writing-a-proposal>`_ & `PSF check-list <https://python-gsoc.org/index.html#apply>`_

Some past draft proposals for reference:

* Angela: `PyZombis: Improving Python’s web interpreter and more interactive exercises <https://docs.google.com/document/d/1PWJF_dQP6qpFkBxBiUt480w-oqZ8_NM2rERQKBkbjIY>`_
* Leonardo: `PyZombis:  Continue the implementation of the course in the Runestone environment <https://docs.google.com/document/d/1eGPD_Woyv-UQINYbsLV6-qnr6I7RCMyEl11OW5s8fUg>`_
* Utkarsh: `PyAfipWs: Library for developers (enhancements) <https://docs.google.com/document/d/1U44YlWrql1_9QFIYSyW8wUBTG6VU6Q0BPybiBnX0VKk>`_ 

Important notes
===============

Late, incomplete, or low-quality proposals will not be considered at all. 
Mentor's time and available students slots are limited, so please ask intelligently for advice and feedback early.

Last-minute applications are generally a signal of further problems (for you and for us too, please avoid!).
Proposals without any previous contribution in the repository (i.e. bug-fix issue) will be rejected.

You're expected to have an almost full-time dedication to the GSoC, so plan accordingly and disclose any potential commitment (exams, work, vacations, travels, etc.)
