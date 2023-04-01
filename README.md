# Preg-Ma project

## Contents

- [Project Setup](#project-setup)
  - [Node Environment](#node-environment)
  - [Running the Project](#running-the-project)
  - [Recommended IDE Setup](#recommended-ide-setup)
- [Development](#development)
  - [Branches](#branches)
- [Deploying](#deploying)


## Road map

1. Finding a dataset
2. Creating web app
3. Create and train model
4. Integration of model and web app
5. Debugging and testing
6. Preparation for presentation 

## Datasets links

* [Kaggle dataset](www.kaggle.com)
* 
*
*




## Tech stack
### Web app tech stack
* Flask
* Vue JS
* Bootstrap JS 
NOTE: Frontend can be changed arbitarily

### Model tech stack 
* Vertex AI
* Heroku 
* PyTorch
* Tensorflow
* Pandas

## Project Setup

Enter the detailed info about project setup here.

### Running the Project

Clone the repository from github.

```sh
git clone https://github.com/SpeechOlympiadXV/speecholympiadxv.github.io.git
```


Enter the details of how to run the project here

### Node Environment







cd into the folder

```sh
cd speecholympiadxv.github.io
```

install dependencies

```sh
npm install
```

run development server (compile and hot reload)

```sh
npm run dev
```

### Recommended IDE Setup

VSCode with extension Volar (recommended by Vue) or extension Vetar (works fine for this)

(However if you're already used to a different IDE it would be better to stick with that and 
install relevant extensions for Vue)

## Development

Refer [documentation for Vue](https://vuejs.org/guide/introduction.html) for getting started with 
VueJS. 

### Branches

Note that the master branch is protected and cannot be directly pushed to. Always work on a 
feature/component branch and make a pull request against master. 

**Note that the gh-pages branch is only for deploying. Do not work on this branch**

## Deploying

Compile and minify files for production into dist folder. Push the contents of dist folder into
gh-pages branch.

```sh
./deploy.sh
```

