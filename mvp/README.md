# mvp

Solution to MVP problem

## Project Url

| Field      | Value                                                                      |
| ---------- | -------------------------------------------------------------------------- |
| URL FRONT  | [PruebaXepelin](http://prueba-xepelin.s3-website.us-east-2.amazonaws.com/) |

## Stack

|         | Tech       | Framework  | Source code                   |
| ------- | ---------- | ---------- | ----------------------------- |
| Front   | Typescript | Vue3 + Vite | `~/src`                       |
| Back    | GSheets    | -          | [GSheet](https://docs.google.com/spreadsheets/d/1hGTZ6BgJd9lTCUEqDv-8LOvZ9nVuZTnCoCxYncTl74Y/edit?usp=sharing) [AppScripts](https://script.google.com/home/projects/1dMbGdRbXWKtOLKl397-LX_JNLQfmLd0jGbsgTey9z_RXeWX48FvILv0h/edit)|

## Project Setup


Node version: 17+

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Type-Check, Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```

## CI/CD

1. Github Actions
    - Implementation uses Github Actions and deploys to AWS S3.

## Misc
  No env variables are used

## Short explanation
  The frontend implements two views
  
    1. Login view
        - Simulates a Fake login, loading a fake value to `JWT` cookie.
        - This was done because there is no data than can be hidden 
        (and requested) in a backend server, so this implementation
        still demonstrates correctly how the app works.
    2. Rates view
        - If there is an user logged in, it shows an embedded Gsheet.
        
  The GSheet does what was requested.