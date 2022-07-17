# mvp

Solution to MVP problem

## Project Url

| Field      | Value                                                                      |
| ---------- | -------------------------------------------------------------------------- |
| URL FRONT  | [PruebaXepelin](http://prueba-xepelin.s3-website.us-east-2.amazonaws.com/) |

## Stack

|         | Tech       | Framework  | Source code                   |
| ------- | ---------- | ---------- | ----------------------------- |
| Front   | Typescript | Vue + Vite | `~/src`                       |
| Back    | -          | GSheets    | -                             |

## Project Setup

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
  Implementation using Github Actions.
  It checks types, builds and deploys to AWS S3.

## Misc
  No env variables are used
