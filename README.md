# Image to Ascii Art Generator

## General Process & Overview

<p>Through my journey in AI, I have worked with many different types of Neural Networks and models. From CNNs to LSTMs, I have worked with most. However, I came across a new architecture known as a GANs (General Adversarial Network), for image generation. As a result, I first tried implementing my own GAN using PyTorch. However, this didnt work out as creating a GAN required a tremendous amount of training, which my current computer could unfortunately not handle. Therefore, I decided to use a pretrained Image Generation model using an API.</p>

<p>To create this application, I had to learn how to use the React framework to create the frontend portion of this project. Using NPM, I was able to create a React app, as NPM gave me a React template to edit. From there, I pieced the different portions of the project together by connecting the React file with the JavaScript file, then connecting that to the CSS and HTML files. In the future, I will consider publishing this on a website, once I spruce up the CSS. </p>

## Complications

<p>While making this project, the main issue I had was creating the React app. I've had to learn React while making this project, which made the process a bit more challenging. Additionally, the Image Generation API gave some problems as most Image Generation models required payment, and some APIs just refused to connect with the React frontend.</p>

## Tech Stack

- JavaScript
- React Native
- HTML
- CSS
- Python
- FastAPI

## How to Use

```bash
git clone repo
cd your-repo/backend/app
python main.py
cd your-repo/frontend/src
npm start

