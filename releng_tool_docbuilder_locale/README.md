# releng-tool Documentation Translations Builder (locale)

This folder contains specific on the translation builder's specific messages.
Translations for this repository are managed in the following
[Transifex][Transifex] project:

> Transifex — releng-tool-doc-translations-builder\
> https://www.transifex.com/releng-tool/releng-tool-doc-translations-builder/

For message translations specific to documentation content, see
[releng-tool-doc-translations][releng-tool-doc-translations] instead.

## Commands

Messages managed in the translations builder can be updated as follows:

    ./update-catalog

To synchronize messages to the Transifex project:

    ./sync-up

To pull down the most recent translation messages from the Transifex project:

    ./sync-down

*(optional)* Messages can be manually compiled; however, this step is always
performed when building documentation:

    ./compile-catalog


[Transifex]: https://www.transifex.com/
[releng-tool-doc-translations]: https://github.com/releng-tool/releng-tool-doc-translations
