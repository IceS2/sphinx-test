# How to Publish the built documentation to Confluence

In order to publish to confluence we're using the `sphinxcontrib.confluencebuilder` extension. You can check the extension documentation [here](https://sphinxcontrib-confluencebuilder.readthedocs.io/en/stable/)

## How to install the extension

`pip install sphinxcontrib-confluencebuilder`

### Basic configuration

In order to configure it to be use first we need to add it to the list of extensions in the `docs/source/conf.py` file.

```python
extensions = [
  ...,
  'sphinxcontrib.confluencebuilder'
]
```

Then we can add any of the extension configurations on the same file.
The main configurations to setup are:

- **confluence_publish:** A boolean that decides whether to allow publishing or not. Default: False.
- **confluence_space_key:** Key of the space in Confluence to be used to publish generated documents to.
- **confluence_parent_page:** The root page found inside the configured space key where published pages will be descentant of.
- **confluence_server_url:** URL for the Confluence instance. Example: `https://example.atlassian.net/wiki/`.
- **confluence_server_user:** Username to authenticat with the Confluence Instance.
- **confluence_server_pass:** Password or API Token used to authenticate with the Confluence Instance.

:::{tip}
**If you're interesting in debugging or testing, there are two important configurations {confluence_emoticon}`wink`**
- **confluence_publish_dryrun:** A run with Dryrun set to True won't edit or remove any existing content. It will just inform th euser which pages will be created, moved, removed.
- **confluence_publish_debug:** Boolean value to whether or not to print debug requests made to a Confluence instance.
:::

:::{note}
**Other interesting configurations to check out**
- **confluence_publish_postfix:** Postfix value added to the title of all published documents.
- **confluence_publish_allowlist:** Defines a list of documents to be published to a Confluence instance.
- **confluence_publish_denylist:** Defines a list of documents to not be published to a Confluence instance.
:::
