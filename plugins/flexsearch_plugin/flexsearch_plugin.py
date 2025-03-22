# MIT License
#
# Copyright (c) [2024] [Diego Carrasco G.]
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json
from nikola.plugin_categories import LateTask
from nikola import utils


class FlexSearchPlugin(LateTask):
    '''iterea sobre todos los post
    saca el titulo y el contenido del tituo y el url
    '''
    name = "flexsearch_plugin"

    def set_site(self, site):
        super(FlexSearchPlugin, self).set_site(site)
        self.site = site
        site.register_path_handler('search_index', self.search_index_path)

    def gen_tasks(self):
        """Generate the search index after all posts are processed."""
        self.site.scan_posts()
        yield self.group_task()

        output_path = self.site.config['OUTPUT_FOLDER']
        index_file_path = os.path.join(output_path, 'assets', 'search_index.json')

        def build_index():
            """Build the entire search index from scratch."""
            index = {}
            for post in self.site.timeline:
                # Sasha: Modifico esta linea para que considere todas las entradas bajo /pages  
                if not post.is_draft:
                    index[post.meta('slug')] = {
                        'title': post.title(),
                        'content': post.text(strip_html=True),
                        'url': post.permalink(absolute=False) 
                    }
            with open(index_file_path, 'w', encoding='utf-8') as f:
                json.dump(index, f, ensure_ascii=False)

        task = {
            'basename': self.name,
            'name': 'all_posts',
            'actions': [build_index],
            'targets': [index_file_path],
            'uptodate': [utils.config_changed({1: self.site.GLOBAL_CONTEXT})],
            'clean': True,
        }
        yield task

    def search_index_path(self, name, lang):
        return [os.path.join(self.site.config['BASE_URL'], 'search_index.json'), None]
