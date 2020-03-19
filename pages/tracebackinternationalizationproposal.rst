
::

   PEP:
   Title: Traceback internationalization
   Version: $Revision$
   Last-Modified: $Date$
   Author: Mariano Reingart <reingart EN gmail PUNTO com>
   Status: Draft
   Type: Standards Track
   Content-Type: text/plain
   Created: 15-May-2010
   Post-History:


   Abstract

       The idea is to provide a standard mechanism to translate exception
       and traceback messages to languages other than English.
       To not reinvent the wheel, this proposal is based on i18n (gettext),
       to ease translation and colaboration between language communities,
       use compatible tools that already exists, favor correctness with
       online review, and has proven to be useful in other projects with
       similar goals (like error messages in PostgreSQL).
       Also, a method to control LC_MESSAGES to get back to English must
       be provided, as some code depends on exception messages (i.e.
       doctests), preferably changeable at runtime, so this libraries are
       self-aware of this issues and no manual intervention is required.


   Rationale

       English isn't the first language of some users (developers), so
       they may not be confortable with messages in that language [1]
       (and some don't understand it at all). Ask them to learn a
       second language (mostly foreign) to use Python is, at least,
       not practical.

       This is specially an issue when Python is used as a First
       Programming Language for teaching to non-English speakers in
       almost any educational level, even worse in other areas not
       related directly with computer sciences.

       Although a workaround may be developed (ie. a wiki page with
       translated errors, as we did in Argentina [2]), that users are
       often blocked when they found an English message, losing they
       concentration on their work, having to waste time finding the
       translation (if it exists) or asking to the teacher or mailing
       lists.

       In the other side, advanced users often prefer original messages
       in English, and they are required in some scenarios like bug
       reporting or doctests, so a method must be provided to change the
       messages language (preferably at runtime).

       Using standards tools for i18n (gettext) will ease translation
       providing a common framework that already is prepared for
       different language rules, with colaborative online applications
       like Pootle[3] to automate translation and review process, tending
       to a high quality result.

       Other projects have chose this way some time ago, citing PostgreSQL
       as an example[4], where, at runtime, you can choose error messages
       language using LC_MESSAGES[5]. Indeed, we are using Pootle and
       other tools to translate PostgreSQL related projects to Spanish in
       a collaborative way [6].

       Finally, this proposal will address current misbehavior with
       locale.LC_MESSAGES category (according the Python Standard Library
       Documentation of locale module) [7]:

           Locale category for message display. Python currently does not
           support application specific locale-aware messages. Messages
           displayed by the operating system, like those returned by
           os.strerror() might be affected by this category.

   Usage

       Setting the desired locale (ie. 'es_AR') in LC_MESSAGES category
       will enable internationalization of tracebacks and exceptions, and
       setting 'C' locale will get back to untranslated original messages:

       Examples:

       Python 3.4.0a0 (default:8f0d5ecca524+, Oct 28 2012, 00:46:34)
       [GCC 4.6.3] on linux
       Type "help", "copyright", "credits" or "license" for more information.
       >>> 1/0
       Traceback (most recent call last):
         File "<stdin>", line 1, in <module>
       ZeroDivisionError: division by zero

       >>> import locale
       >>> locale.setlocale(locale.LC_MESSAGES,'es_AR.utf8')
       'es_AR.utf8'
       >>> 1/0
       Traza de rastreo (llamada más reciente última):
         Archivo "<stdin>", línea 1, en <module>
       ZeroDivisionError: división por cero

       >>> locale.setlocale(locale.LC_MESSAGES,'C')
       'C'
       >>> 1/0
       Traceback (most recent call last):
         File "<stdin>", line 1, in <module>
       ZeroDivisionError: division by zero

       By default, LC_MESSAGES should be 'C' locale, to prevent any
       misunderstanding.

       The user that needs translated messages could easily add a
       line or setting LC_MESSAGES in his desired language:

       import locale; locale.setlocale(locale.LC_MESSAGES,'es_AR.utf8')

   Caveats

       Internationalization uses UTF-8 to be able to handle special
       characters like accents. This should not be a problem in Python 3
       but some functions may be revised like PyUnicode_FromFormatV() [9]

       Special care must be taken with positional placeholders like in:
       "name '%.200s' is not defined". If there is more than one
       placeholder, using printf special format specifiers (ie. %2$s %1$s)
       or an alternate string formatting system should be required
       in order to allow to change their position in the string (this may
       be required by some languages rules in some contexts).

   Reference Implementation

       A proof of concept is attached to issue #16344 [10] for Python 3.3+
       Original -obsolete- version (for python 2.x) can be downloaded from
       Python Argentina Wiki [8]

       It defines a Py_GETTEXT macro that is called from PyErr_SetString
       and PyErr_Format (errors.c) and tb_displayline, PyTraceBack_Print
       (traceback.c).

       A new subdirectory called Locale stores localized message files,
       but this could be installed in a standard system directory (i.e.
       /usr/share/locale) as a special domain called "python" is used to
       not interfere with python modules / libraries / packages already
       using gettext.

       Some steps are required to set up internationalization correctly:

       1. locale.bind_textdomain_codeset("python", "utf8") should be
          called in pythonrun.c to initialize encoding (preventing nested
          unicode exceptions if internationalization is not correctly)
       2. locale.bindtextdomain("python", sysconfig._safe_realpath("Locale"))
          should be called in site.py to specify the locale directory
          (not needed if a standard directory is used, this would be
          platform dependent)
       3. locale.setlocale(locale.LC_MESSAGES,'es_AR.utf8') should be
          executed by the end user to finally enable internationalization

       Although it is just a proof of concept, final version shouldn't be
       much different than this, as internationalization points are
       well-known so just 2 C files were modified.

       In order to keep the change small, and in order to not bother other
       developers with new special issues, this approach needs a custom tool
       for messages recollection from source files, similar to pygettext.py,
       but scanning C files for PyErr_Format or PyErr_SetString messages.
       Looking for messages in .py files would be a little more difficult,
       as it would have to look where exceptions are raised.
       None of both tools were developed for this draft.

   References

       [1] http://wiki.python.org/moin/BeginnersGuide

       [2] http://python.org.ar/pyar/MensajesExcepcionales

       [3] http://translate.sourceforge.net/wiki/pootle/index

       [4] http://www.postgresql.org/docs/8.2/static/nls-translator.html

       [5] http://www.postgresql.org/docs/8.2/static/locale.html

       [6] http://pootle.arpug.com.ar/pootle

       [7] http://docs.python.org/library/locale.html

       [8] http://python.org.ar/pyar/TracebackInternationalizationProposal?action=AttachFile&do=view&target=python_traceback_i18n_proof_of_concept.diff

       [9] http://bugs.python.org/issue16343

       [10] http://bugs.python.org/issue16344


   Copyright

       This document has been placed in the public domain.


   
   Local Variables:
   mode: indented-text
   indent-tabs-mode: nil
   sentence-end-double-space: t
   fill-column: 70
   coding: utf-8
   End:

Attachment moin wiki code:

