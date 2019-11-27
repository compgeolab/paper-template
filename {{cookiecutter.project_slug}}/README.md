# {{cookiecutter.title}}

by {{ "" }}
{%- for key, author in cookiecutter.authors.items() -%}
[{{author.name}}]({{author.url}})
    {%- if not loop.last -%}
        {%- if loop.revindex == 2 -%}
            {{ " and " }}
        {%- else -%}
            {{ ", " }}
        {%- endif -%}
    {%- endif -%}
{% endfor %}


## Abstract

Introduce the abstract for the paper here.

## Reproducing the results

You can download a copy of all the files in this repository by cloning the
[git](https://git-scm.com/) repository:

    git clone https://github.com/{{ cookiecutter.gh_repo }}

or [click here to download a zip archive](https://github.com/{{ cookiecutter.gh_repo }}/archive/master.zip).

All source code used to generate the results and figures in the paper are in the `code`
folder. There you can find the Python codes that and scripts to generate all figures and
results presented in the paper.

The sources for the manuscript text and figures are in `manuscript`.

See the `README.md` files in each directory for a full description.

### Setting up your environment

You'll need a working Python **{{ cookiecutter.python_version }}** environment with all
the standard scientific packages installed (numpy, scipy, matplotlib, etc).  The easiest
(and recommended) way to get this is to download and install the
[Anaconda Python distribution](http://continuum.io/downloads#all).
Make sure you get the **Python {{ cookiecutter.python_version }}** version.

#### Manual installation

You'll also need the following packages in order to reproduce the results:

* list
* of
* dependencies

#### Installing through conda environment

Instead of manually install all the dependencies, they can all be automatically
installed by creating a conda environment.

1. Change directory to the cloned git repository:
    ```
    cd {{ cookiecutter.project_slug }}
    ```
1. Create a new conda environment from the `environment.yml` file:
    ```
    conda env create -f environment.yml
    ```
1. Activate the new environment:

    ```
    source activate {{ cookiecutter.project_slug }}
    ```

For more information about managing conda environments visit this
[User Guide](https://conda.io/docs/user-guide/tasks/manage-environments.html)

## License

All source code is made available under a BSD 3-clause license.  You can freely
use and modify the code, without warranty, so long as you provide attribution
to the authors.  See `LICENSE.md` for the full license text.

Data and the results of numerical tests are available under the
[Creative Commons Attribution 4.0 License (CC-BY)](https://creativecommons.org/licenses/by/4.0/).

The manuscript text and figures are not open source. The authors reserve the
rights to the article content, which has been accepted for publication in
{{ cookiecutter.journal }}.
