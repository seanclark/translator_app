# Translator App

This is a lightweight, Flask-based translator app built in Python, designed to test out AI model integration and rapid deployment workflows.
It uses Meta’s yorickvp/llava-13b model via the Replicate API, allowing short text to be translated across multiple languages with minimal latency.
The app was up and running locally within hours, thanks to a clean architecture and focused prototyping. It supports right-to-left (RTL) languages, 
enforces a word limit to keep model responses efficient, and includes copy-to-clipboard functionality for streamlined user interaction.

## Live demo site
https://translator-app-26nv.onrender.com/ (Please allow a minute for the site to load on Render)

## Features

* Translate between 14+ languages
* Word limit (50 words) to keep things fast and cost-efficient
* Right-to-left support for languages like Arabic and Hebrew
* Copy icon with hover effect for clarity
* Responsive layout with auto-resizing text areas
* Built with Python, Flask, HTML/CSS, and Replicate API

## Screenshots

<img width="925" height="425" alt="Screenshot 2025-09-08 194931" src="https://github.com/user-attachments/assets/a3394b49-4032-464d-a62d-4dce93b380ab" />
<img width="913" height="781" alt="Screenshot 2025-09-08 195048" src="https://github.com/user-attachments/assets/a10212c8-0bf6-4d08-b4b2-9fffd179e5cb" />
<img width="907" height="678" alt="Screenshot 2025-09-08 200641" src="https://github.com/user-attachments/assets/5624786e-1e7b-406f-93e9-cc4e476bf8b1" />

## Licensing Information

* Translator App uses Replicate model yorickvp/llava-13b by Meta
* See license information on Meta's website (getting link)

