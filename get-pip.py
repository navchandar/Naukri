
<!DOCTYPE html>

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" /><meta name="generator" content="Docutils 0.19: https://docutils.sourceforge.io/" />

    <title>Python Packaging Authority &#8212; PyPA  documentation</title><meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <link rel="stylesheet" type="text/css" href="_static/pygments.css" />
    <link rel="stylesheet" type="text/css" href="_static/pypa.css" />
    <link id="pygments_dark_css" media="(prefers-color-scheme: dark)" rel="stylesheet" type="text/css" href="_static/pygments_dark.css" />
    
    
    <script data-url_root="#" id="documentation_options" src="_static/documentation_options.js"></script>
    <script src="_static/doctools.js"></script>
    <script src="_static/sphinx_highlight.js"></script>
    
    
    <script src="_static/sidebar.js"></script>
    
    <link rel="index" title="Index" href="genindex/" />
    <link rel="search" title="Search" href="search/" />
    <link rel="next" title="PyPA Goals" href="future/" /><link rel="stylesheet" href="_static/pydoctheme_dark.css" media="(prefers-color-scheme: dark)" id="pydoctheme_dark_css">
    <link rel="shortcut icon" type="image/png" href="_static/py.svg" />
            <script type="text/javascript" src="_static/copybutton.js"></script>
            <script type="text/javascript" src="_static/menu.js"></script>
            <script type="text/javascript" src="_static/themetoggle.js"></script> 
  
<!-- RTD Extra Head -->



<script type="application/json" id="READTHEDOCS_DATA">{"ad_free": false, "api_host": "https://readthedocs.org", "builder": "sphinx", "canonical_url": null, "docroot": "/source/", "features": {"docsearch_disabled": false}, "global_analytics_code": "UA-17997319-1", "language": "en", "page": "index", "programming_language": "py", "project": "pypaio", "proxied_api_host": "/_", "source_suffix": ".rst", "subprojects": {}, "theme": "pypa_theme", "user_analytics_code": "", "version": "latest"}</script>

<!--
Using this variable directly instead of using `JSON.parse` is deprecated.
The READTHEDOCS_DATA global variable will be removed in the future.
-->
<script type="text/javascript">
READTHEDOCS_DATA = JSON.parse(document.getElementById('READTHEDOCS_DATA').innerHTML);
</script>



<!-- end RTD <extrahead> -->
<script async type="text/javascript" src="/_/static/javascript/readthedocs-addons.js"></script><meta name="readthedocs-project-slug" content="pypaio" /><meta name="readthedocs-version-slug" content="latest" /><meta name="readthedocs-resolver-filename" content="/" /><meta name="readthedocs-http-status" content="200" /></head>
<body>
<div class="mobile-nav">
    <input type="checkbox" id="menuToggler" class="toggler__input" aria-controls="navigation"
           aria-pressed="false" aria-expanded="false" role="button" aria-label="Menu" />
    <nav class="nav-content" role="navigation">
        <label for="menuToggler" class="toggler__label">
            <span></span>
        </label>
        <span class="nav-items-wrapper">
            <a href="https://pypa.io" class="nav-logo">
                <img src="_static/py.svg" alt="Logo"/>
            </a>
            <span class="version_switcher_placeholder"></span>
            <form role="search" class="search" action="search/" method="get">
                <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" class="search-icon">
                    <path fill-rule="nonzero" fill="currentColor" d="M15.5 14h-.79l-.28-.27a6.5 6.5 0 001.48-5.34c-.47-2.78-2.79-5-5.59-5.34a6.505 6.505 0 00-7.27 7.27c.34 2.8 2.56 5.12 5.34 5.59a6.5 6.5 0 005.34-1.48l.27.28v.79l4.25 4.25c.41.41 1.08.41 1.49 0 .41-.41.41-1.08 0-1.49L15.5 14zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"></path>
                </svg>
                <input placeholder="Quick search" aria-label="Quick search" type="search" name="q" />
                <input type="submit" value="Go"/>
            </form>
        </span>
    </nav>
    <div class="menu-wrapper">
        <nav class="menu" role="navigation" aria-label="main navigation">
            <div class="language_switcher_placeholder"></div>
            
<label class="theme-selector-label">
    Theme
    <select class="theme-selector" oninput="activateTheme(this.value)">
        <option value="auto" selected>Auto</option>
        <option value="light">Light</option>
        <option value="dark">Dark</option>
    </select>
</label>
        </nav>
    </div>
</div>
  
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="genindex/" title="General Index"
             accesskey="I">index</a></li>
        <li class="right" >
          <a href="future/" title="PyPA Goals"
             accesskey="N">next</a> |</li>
          <li><img src="_static/py.svg" alt="python logo" style="vertical-align: middle; margin-top: -1px"/></li>
          <li><a href="https://pypa.io">PyPA</a> &#187;</li>
          <li class="switchers">
            <div class="language_switcher_placeholder"></div>
            <div class="version_switcher_placeholder"></div>
          </li>
          <li>
              
              <a href="#">PyPA  documentation</a> &#187;
              
          </li>
        <li class="nav-item nav-item-this"><a href="">Python Packaging Authority</a></li>
                <li class="right">
                    

    <div class="inline-search" role="search">
        <form class="inline-search" action="search/" method="get">
          <input placeholder="Quick search" aria-label="Quick search" type="search" name="q" />
          <input type="submit" value="Go" />
        </form>
    </div>
                     |
                </li>
            <li class="right">
<label class="theme-selector-label">
    Theme
    <select class="theme-selector" oninput="activateTheme(this.value)">
        <option value="auto" selected>Auto</option>
        <option value="light">Light</option>
        <option value="dark">Dark</option>
    </select>
</label> |</li>
            
      </ul>
    </div>    

    <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body" role="main">
            
  <section id="python-packaging-authority">
<h1>Python Packaging Authority<a class="headerlink" href="#python-packaging-authority" title="Permalink to this heading">¶</a></h1>
<p>The Python Packaging Authority (PyPA) is a working group that maintains a core
set of software projects used in Python packaging.</p>
<p>The software developed through the PyPA is used to package, share, and install
Python software and to interact with indexes of downloadable Python software
such as <a class="reference external" href="https://pypi.org">PyPI</a>, the Python Package Index. Click the logo below to download pip, the most prominent software used to interact with PyPI.</p>
<a class="reference external image-reference" href="https://pypi.org/project/pip/#files"><img alt="_images/pypi-logo.svg" src="_images/pypi-logo.svg" /></a>
<p>The PyPA publishes the <a class="reference external" href="https://packaging.python.org">Python Packaging User Guide</a>, which is <strong>the authoritative resource
on how to package, publish, and install Python projects using current
tools</strong>. The User Guide provides a user introduction to packaging, and
explains how to use these tools. In case you need to package Python
with other languages (for example, in a scientific Python package),
the user guide also offers basic information about and links to
available third-party packaging options (for example, <a class="reference external" href="https://conda-forge.org/">conda-forge</a>).</p>
<p>For a listing of PyPA’s important projects, see <a class="reference external" href="https://packaging.python.org/en/latest/key_projects/#pypa-projects" title="(in Python Packaging User Guide)"><span class="xref std std-ref">the key projects
list</span></a>. The PyPA hosts projects on <a class="reference external" href="https://github.com/pypa">GitHub</a>,
and discusses issues on the <a class="reference external" href="https://discuss.python.org/c/packaging">Packaging
category on discuss.python.org</a>.</p>
<p>For a user introduction to packaging, see the <a class="reference external" href="https://packaging.python.org">Python Packaging User Guide</a></p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="future/">PyPA Goals</a></li>
<li class="toctree-l1"><a class="reference internal" href="specifications/">PyPA Specifications</a></li>
<li class="toctree-l1"><a class="reference internal" href="roadmap/">PyPA Roadmap</a></li>
<li class="toctree-l1"><a class="reference internal" href="help/">How to Help</a></li>
<li class="toctree-l1"><a class="reference internal" href="presentations/">Presentations &amp; Articles</a></li>
<li class="toctree-l1"><a class="reference internal" href="history/">Packaging History</a></li>
<li class="toctree-l1"><a class="reference internal" href="members/">PyPA Members, And How To Join</a></li>
<li class="toctree-l1"><a class="reference internal" href="code-of-conduct/">Code of Conduct</a></li>
</ul>
</div>
</section>


            <div class="clearer"></div>
          </div>
        </div>
      </div>
      <div class="sphinxsidebar" role="navigation" aria-label="main navigation">
        <div class="sphinxsidebarwrapper">
        </div>
<div id="sidebarbutton" title="Collapse sidebar">
<span>«</span>
</div>

      </div>
      <div class="clearer"></div>
    </div>  
    <div class="related" role="navigation" aria-label="related navigation">
      <h3>Navigation</h3>
      <ul>
        <li class="right" style="margin-right: 10px">
          <a href="genindex/" title="General Index"
             >index</a></li>
        <li class="right" >
          <a href="future/" title="PyPA Goals"
             >next</a> |</li>
          <li><img src="_static/py.svg" alt="python logo" style="vertical-align: middle; margin-top: -1px"/></li>
          <li><a href="https://pypa.io">PyPA</a> &#187;</li>
          <li class="switchers">
            <div class="language_switcher_placeholder"></div>
            <div class="version_switcher_placeholder"></div>
          </li>
          <li>
              
              <a href="#">PyPA  documentation</a> &#187;
              
          </li>
        <li class="nav-item nav-item-this"><a href="">Python Packaging Authority</a></li>
                <li class="right">
                    

    <div class="inline-search" role="search">
        <form class="inline-search" action="search/" method="get">
          <input placeholder="Quick search" aria-label="Quick search" type="search" name="q" />
          <input type="submit" value="Go" />
        </form>
    </div>
                     |
                </li>
            <li class="right">
<label class="theme-selector-label">
    Theme
    <select class="theme-selector" oninput="activateTheme(this.value)">
        <option value="auto" selected>Auto</option>
        <option value="light">Light</option>
        <option value="dark">Dark</option>
    </select>
</label> |</li>
            
      </ul>
    </div>  
    <div class="footer">
    &copy; Copyright 2020, PyPA.
    <br />
    This page is licensed under the Python Software Foundation License Version 2.
    <br />
    Examples, recipes, and other code in the documentation are additionally licensed under the Zero Clause BSD License.
    <br />
    
    <br />

    The Python Software Foundation is a non-profit corporation.
<a href="https://www.python.org/psf/donations/">Please donate.</a>
<br />
    <br />

    Last updated on Jul 31, 2023.
    <a href="https://github.com/pypa/pypa.io/issues">Found a bug</a>?
    <br />

    Created using <a href="https://www.sphinx-doc.org/">Sphinx</a> 6.1.3.
    </div>

  </body>
</html>