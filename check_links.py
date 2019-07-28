# -*- coding: utf-8 -*-


"""
Agrega el links de todas las paginas que faltan para poder compilar la wiki
"""

import re
import os
from pathlib import Path

WIKI_PATH = os.path.dirname(__file__)
FILES_BASE_PATH = os.path.join(WIKI_PATH, 'pages')

# the different regex used to find the link to other articles
LINK_REGEXES = [
    re.compile(r'\w+\_'),
]


def scan_folder(current_path):
    folders_to_scan = []
    current_files = []
    for filename in os.listdir(current_path):
        complete_path = os.path.join(current_path, filename)
        if os.path.isdir(complete_path):
            folders_to_scan.append(complete_path)
        else:
            current_files.append(complete_path)

    return (current_files, folders_to_scan)


def check_files(base_path, should_go_recursive=True):
    files, folders = scan_folder(base_path)
    for filename in files:
        content = open(filename).read()
        added_links = []
        added_articles = set()
        # search all the wors that ends with a "_" because those are the links
        # to other files
        for link_regex in LINK_REGEXES:
            for article in link_regex.findall(content):
                article = article[:-1]
                if article.lower() in added_articles:
                    # that article is already selected to be added so there is
                    # no need to added it again
                    continue

                if ('.. _%s:' % article) in content or ('.. _%s' % article.lower()) in content:
                    # the file has already a link for that article
                    continue

                # for that link find the given file starting on the
                # current filepath where it is
                article_filename = find_file(article)
                if article_filename:
                    # make some magic to create the corresponding URL to
                    # the file
                    article_filename = article_filename.replace('.rst', '')
                    added_links.append('.. _%s: /%s\n' % (article.lower(), article_filename))
                    added_articles.add(article.lower())

        if added_links:
            with open(filename, 'w') as f:
                f.write(content + '\n')
                f.writelines(added_links)

    if should_go_recursive:
        for folder in folders:
            check_files(folder)


def find_file(article):
    filenames = list(Path('pages').glob('**/%s.rst' % article.lower()))
    if len(filenames) > 1:
        # there is more than one link so I am not sure which one should I use
        return None
    if filenames:
        return str(filenames[0])
    else:
        return None


def rename_all_files():
    """ Rename all rst files so the filename is in lowercase
    """
    filenames = Path('pages').glob('**/*.rst')
    for filename in filenames:
        new_filename = str(filename).split('/')
        new_filename[-1] = new_filename[-1].lower()
        new_filename = '/'.join(new_filename)
        os.rename(filename, new_filename)


# rename_all_files()
check_files(FILES_BASE_PATH)
