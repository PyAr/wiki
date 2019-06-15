
Decodificar entities de HTML
============================

::

    import re
    import htmlentitydefs

    def unescape(text, encoding="UTF-8"):
        """
        Removes HTML or XML character references and entities from a text string.

        @param text The HTML (or XML) source text.
        @return The unescaped text as a Unicode.
        """

        def fixup(m):
            text = m.group(0)
            if text[:2] == "&#":
                # character reference
                try:
                    if text[:3] == "&#x":
                        text = unichr(int(text[3:-1], 16))
                    else:
                        text = unichr(int(text[2:-1]))
                except ValueError:
                    pass
            else:
                # named entity
                try:
                    text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
                except KeyError:
                    pass

            return text

        # Decode string as needed
        text = text.decode(encoding) if isinstance(text, str) else text
        return text and re.sub("&#?\w+;", fixup, text)


Gracias Martin Conte Mac Donell! |wink|

-------------------------



  CategoryRecetas_

