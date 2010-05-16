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
    they may be not confortable with messages in this language [1]
    (and some don't understand it at all). Ask the user to learn
    a second language to use Python is, at least, not practical.

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
    misunderstanding.

    The user that needs translated messages could easily add a 
    line or setting LC_MESSAGES in his desired language:

    import locale; locale.setlocale(locale.LC_MESSAGES,'es_AR')

Caveats

    i18n should allow return Unicode to be able to handle special 
    characters like accents.

    Special care must be taken with positional placeholders like in:
    "name '%.200s' is not defined". If there is more than one 
    placeholder, using printf special format specifiers (ie. %2$s %1$s)
    or an alternate string formatting system should be required
    in order to allow to change their position in the string (this may
    be required by some languages rules in some contexts).

Reference Implementation

    A proof of concept can be downloaded from Python Argentina Wiki [8]

    It defines a i18n function that is called from PyErr_SetString and 
    PyErr_Format (errors.c) and tb_displayline, PyTraceBack_Print 
    (traceback.c).

    As this is a proof of concept, i18n function just scans a C static 
    string array, but furtherly it will use gettext functionality.

    Also, i18n function emulates LC_MESSAGES functionality (as only some 
    Spanish messages are translated so far for this example and it isn't 
    using gettext by now), but this could  be modified easily once the 
    internationalization mechanism is accepted.

    Disclaimer: This proof of concept does not address known caveats and 
    it is totally disposable, no comprehensive tests or revisions have been
    done. It is just a quickly and dirty hack to show the point, a real 
    implementation must be done.

    Although it is just a proof of concept, final version shouldn't be 
    much different than this, as internationalization points are 
    well-known so just 2 C files where modified. Indeed, a version using
    gettext would be even smaller as messages would be in separated files,
    i18n could reduce just to _ (gettext) C function.
    
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

Attachment moin wiki code:
[[attachment:python_traceback_i18n_proof_of_concept.diff]]
