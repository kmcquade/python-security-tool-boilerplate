# python-security-tool-boilerplate

Boilerplate code for Python based security assessment tools that generate HTML reports.

## Background

When developing Python-based security assessment tooling, it's difficult to include User Interfaces as a baked-in part of the tool.

Let's say you want to be able to run a command, have the tool generate a report, and you view the report. You have three options:
1. Output the HTML into a single HTML file.
   * Becomes a nightmare to maintain and read
   * You will hate Jinja2
2. Output the HTML into a zip file.
   * Report looks great
   * Everyone will complain about having to zip and unzip the files.

ScoutSuite (which is a **fantastic** tool) does the latter. It looks like the contributors have to [include their handwritten HTML per finding](https://github.com/nccgroup/ScoutSuite/blob/master/ScoutSuite/output/data/html/partials/aws/services.acm.regions.id.certificates.html).

That would be a templating nightmare. I wanted to avoid this. But I also couldn't stick with Option 1 for much longer - the HTML file had become over 1000 lines, and it looked **really** ugly.

So I figured out a cool approach that combined the powers of Python, Jinja2, VueJS, and Webpack that:
* Generates **a single HTML file** as part of the Python command to display the report.
* Allows contributors to store their JavaScript in several files in line with standard convention (Vue CLI)
* **Does not require the user to install webpack or anything else except the Python tool**

## Tutorial

...todo

## Using this repository

...todo

Note: When the user wants to add more info to the table, they will have to:
* Include that in the JSON data output from the python before it gets fed into JS
* Edit the sampleData.js file to show that new file
* Edit the TableReport.vue component file to show the new field
