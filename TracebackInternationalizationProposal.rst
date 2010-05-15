{{{
PEP: 
Title: Traceback internationalization
Version: $Revision$
Last-Modified: $Date$
Author: Mariano Reingart <reingart@gmail.com>
Status: Draft
Type: Standards Track
Content-Type: text/plain
Created: 15-May-2010
Post-History:


Abstract

    The idea is to provide a standard mechanism to translate exception 
    and traceback messages to other languages than English.
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
    they may be not confortable with messages in this language [1]
    (and someones don't understand it at all). Ask the user to learn
    a second language to use Python is, at least, not practical.

    This is specially and issue when Python is used as a First 
    Programming Language for teaching to non-English speakers  in 
    almost any educational level, even worse in other areas not 
    related directly with computer sciences.

    Although a workaround may be developed (ie. a wiki page with 
    translated errors, as we did in Argentina [2]), users are often 
    blocked when then found an English message, losing they 
    concentration on their work, having to waste time finding the 
    translation (if it exists) or asking to the teacher.

    In the other side, advanced users often prefer original messages
    in English, and they are required in some scenarios like bug 
    reporting or doctests, so a method must be provided to change the
    messages language (preferably at runtime).

    Using standards tools for i18n (gettext) will ease translation 
    providing a common framework that already is prepared for 
    different language grammars, with colaborative online applications 
    like Pootle[3] to automate translate and review process, tending 
    to a high quality result.

    Other projects have chose this way some time ago, citing PostgreSQL 
    as an example[4], where you can choose at runtime error messages 
    language using LC_MESSAGES[5]. Indeed, we are using Pootle and 
    other tools to translate PostgreSQL related projects to Spanish in
    a collaborative way [6].

Usage

    Setting the desired locale (ie. 'es_AR') in LC_MESSAGES category 
    will enable internationalization of tracebacks and exceptions, and
    seting 'C' locale will get back to untranslated original messages:

    Examples:
 
    >>> 1/0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: integer division or modulo by zero
    >>> import locale
    >>> locale.setlocale(locale.LC_MESSAGES,'es_AR')
    'es_AR'
    >>> 1/0
    Traza de rastreo (llamada mas reciente ultima):
      Archivo "<stdin>", linea 1, en <module>
    ZeroDivisionError: division entera o modulo por cero
    >>> locale.setlocale(locale.LC_MESSAGES,'C')
    'C'
    >>> 1/0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: integer division or modulo by zero

    By default, LC_MESSAGES should be 'C' locale, to prevent any
    misunderstunding.

    The user that needs translated messages could easily add a 
    line or setting LC_MESSAGES in his desired language:

    import locale; locale.setlocale(locale.LC_MESSAGES,'es_AR')

Caveats

    i18n should allow return Unicode to be able to handle special 
    characters like accents.

    Special care must be taken with positional placeholders like in:
    "name '%.200s' is not defined". If there is more than one 
    placeholder, an alternate string formatting system should be used
    in order to allow to change their position in the string (this may
    be required by some languages in some contexts).

Reference Implementation

    A proof of concept could be downloaded from:

       

    It defines a i18n function that is called from PyErr_SetString and 
    PyErr_Format (errors.c) and tb_displayline, PyTraceBack_Print 
    (traceback.c).

    As this is a proof of concept, i18n function just scans a C static 
    string array, but furtherly it will use gettext functionality.

    Also, i18n function emulates LC_MESSAGES functionality (as only some 
    Spanish messages are translated so far for this example and it isn't 
    using gettect by now), but this could  be modified easily once the 
    internationalization mechanism is accepted.

    Disclaimer: This proof of concept does not address known caveats and 
    it is totally disposable, no comprehensive tests or revisions have been
    done. It is just a quickly and dirty hack to show the point, a real 
    implementation must be done.

References

    [1] http://wiki.python.org/moin/BeginnersGuide

    [2] http://python.org.ar/pyar/MensajesExcepcionales

    [3] http://translate.sourceforge.net/wiki/pootle/index

    [4] http://www.postgresql.org/docs/8.2/static/nls-translator.html

    [5] http://www.postgresql.org/docs/8.2/static/locale.html

    [6] http://pootle.arpug.com.ar/pootle


Copyright

    This document has been placed in the public domain.



Local Variables:
mode: indented-text
indent-tabs-mode: nil
sentence-end-double-space: t
fill-column: 70
coding: utf-8
End:
}}}
