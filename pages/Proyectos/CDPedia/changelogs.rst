.. title: Changelogs

Para la 0.8
~~~~~~~~~~~

* Parameters for tar medium version.

* Use a page selector to calculate top htmls and know if it's same as before.

* Fix multiword search.

* Set up fixed versions of CDPedia.

* Merged enhance-home branch.

* Merged very_important_articles branch in.

* Merged lp:~ccanepacc/cdpedia/win-exe-generator-variants2 but changing it to keep only the pyinstaller 2 stuff.

* Fix the generated config to be more multiplatform regarding paths.

* Merged lp:~ccanepacc/cdpedia/table-resouces

* Removed two symlinks for the project, to make it more windows-development friendly.

* A couple of fixes for serving web pages.

* Avoid double decoding.

* Make the process nicer.

* Merged lp:~facundo/cdpedia/other-image-url

* New utilitie to generate a sample of the dump.

* Get the in-namespaces name correctly.

* Merged dump-support-art-namespaces branch.

* Better string.

* Merged the clean-scrap branch.

* Merged lp:~dmascialino/cdpedia/fix-scraper_pagination_99

* Reverted Diego's changes.

* Syntax error.

* Some optimizations and cleanups.

* Modifico scraper, para que tenga en cuenta la paginacion en Categorías. fixed #99

* Usar twisted para el scraper

* Better logging and whitespace.

* Fix for hidden user in commits bug.

* 1st. if we don't found a good enough version of the article we use the first version in its history; 2nd. we download history for 6 versions only and if we don't find a good one, we download it's 100 last history

* This uses mediawiki API to check article's history..

* We log

* Fixed bug introduced on r439

* Moved python tutorial to a compressed scheme, fixed #110 and #137

* ticket 142: remove not last version message..

* Fixed error message, and added a timeout.

* ups

* print article no its repr()

* Add a little retrying to the fetch.

* Support no history and small cleanups.

* issue #124, merge from : https://cdpedia.googlecode.com/svn/branches/issue124

* Finished the 'extraer' refactor.

* Half refactor of image extractor.

* Support re-asking for the search after end of itself.

* Fixed bug introduced on r421 (ExtraerContenido moved to scraper)

* Added license header and some cleanup to web_app

* Full search implemented.

* #91. Movemos el preprocesador ExtraerContenido al scraper

* Verify some details on the downloaded page.

* Fixed header

* We need AUTHORS as project root.

* Change directory so we can run it from anywhere.

* Patched the HTTPServer to have shutdown in old Python versions.

* Simple search (without javascript) working.; TODO: add support to index not ready and add pagination features.

* Fixed unittest discovery support of index_tests

* Fixed some broken urls from last commit.

* Reordered static files to a simple structure.

* Cache the search.

* First steps of search implementation in the web_app

* Restructured cdpedia.py and added command line options for daemon mode, portname, hostname and verbose

* Added verbose attribute to Destacados

* Fixed bug introducen on r405

* Portales en la portada aunque no haya destacados

* More consistent unicode handling in web_app.

* Grouped in searcher.

* Actualizada a 0.7

* Searcher

* Algunos tests para el watchdog

* Browser WatchDog andando

* Wrapeo las paginas de institucional #136

* La leyenda de error de suffix tree ahora solo aparece en la generacion #130

* Desactivar el browser watchdog con BROWSER_WD_SECONDS = 0

* Se puede elegir el puerto y hostname en el config.py #98

* cdpedia.py funcionando nuevamente

* Agrega debugger a la web_app

* Bump werkzeug version a 0.7.1

* Docs, process

* More explicit option in tar, and correct XO config.

* Remove the symlink after building the tarball

* Update real values for XO and CD.

* New options for generar.py

* Don't put all redirects in the blocks, just the useful ones.

* Mergedo el branch web-werkzeug a trunk

* Agrego metodo from_path a to3dirs.

* Ahora se testea tanto el compressed_index como el easy_index automaticamente.

* Muevo los tests de to3dirs al directorio /tests y agrego algunos tests más.

