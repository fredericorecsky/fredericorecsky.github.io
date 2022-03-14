# GitHub Actions 

## Links

[Documentation](https://docs.github.com/en/actions)

### Cases/Usages

#### Github Pages CMS

Generate the CMS data files for a static site. Just to keep the basic structure. When the repo that has the data is pushed just regenerate them.

Followed the [quickstart](https://docs.github.com/en/actions/quickstart) and created a workflow for my personal website so it generates a basic list of links to display on the main page.

##### Stopping automatic page generation

From: [Doc](https://docs.github.com/en/pages/getting-started-with-github-pages/unpublishing-a-github-pages-site)

Under your repository name, click Settings. In the "Code and automation" section of the sidebar, click Pages. Under "GitHub Pages", use the Source drop-down menu and select None.

*Since it is a github.io, it build from a branch*, so I changed the default work branch from the main to staging, so the github action will push the code to the main. 