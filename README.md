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


## Vue CLI

* Install

```bash
npm install -g @vue/cli @vue/cli-service-global
```

* Ran `vue create vue-boilerplate-ui` in the root of this directory
* Moved the babel.config.js, package.json, package-lock.json into the root of this directory
* Moved the public and src into the vue_boilerplate/output/ directory


## NPM

### Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

