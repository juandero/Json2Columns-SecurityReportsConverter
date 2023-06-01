# Json2Columns-SecReportsConverter

## Description

This tool was born from a personal need, which consists of converting the reports of some security tools from json to other formats that allow them to be directly included in the documentation of some results reports.

That’s because, although some tools allow reports to be generated in other formats (e.g., csv or xls) some of them omit data or information in that way, even when that omitted data is already included by default in the outputs when are generated in json format.

> **Disclaimer:** The defined columns of the outputs in csv or xlsxs formats are intended to be the most useful for decisions making in Vulnerability Management tasks. By the way, I will be open to suggestions on this matter.

## Currently working on

At this moment, I am working to include support for the json outputs of the next tools:
- [Safety](https://github.com/pyupio/safety)
- [Bandit](https://github.com/PyCQA/bandit)

More tools coming soon (suggestions are welcome).

## To-Do tasks (At the moment)

- [ ] Finish the inclusion of the support for the tools I’m working on.
- [ ] Include some error management capacities.
- [ ] Maybe improve this README file to include some indications about how to run the tool.

## Contributing

Please feel free to look through the open [issues](https://github.com/juandero/Security-Report-Format-Converter/issues), make a fork and submit a PR for improvements. All the suggestions, updates, fixes, new features and capabilities are appreciated.

Of course, all contributors obtain copyrights on this project and will be listed here!

## Issues and Support

If you have suggestions, questions or issues running some of the codes, feel free to open an [issue](https://github.com/juandero/Security-Report-Format-Converter/issues) to contact and receive help.

At this moment no other channels (like e-mail or social media) are being used for support purposes. So please, do not try to contact me through other ways different as described.

## Licence

- Code and documentation copyright (c) 2023-Present Juan P. Montero (A.k.a. [juandero](https://github.com/juandero)).
- Source code licensed under [MIT License](https://github.com/juandero/Security-Report-Format-Converter/blob/main/LICENSE).
- Documentation licensed under [Creative Commons Attribution 4.0 license](https://creativecommons.org/licenses/by/4.0/).