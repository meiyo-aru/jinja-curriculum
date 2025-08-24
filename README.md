# Jinja Curriculum

A Server-Side Rendering (SSR) web service built with **Python** and **Jinja2** to generate dynamic resumes, styled with **SCSS**, and powered by a dedicated **RESTful API**. This project aims to demonstrate the creation of rich, dynamic HTML content by combining backend logic with pre-rendered frontend presentation.

---

## About the Project

**Jinja Curriculum Render** is an application that fetches resume data from a separate RESTful API and injects it into Jinja2 templates. The result is complete HTML, with styles applied via SCSS, which is sent directly to the client's browser. This ensures a fast user experience, improved SEO, and precise control over the design of each resume.

### Technologies Used

* **Python**: Primary programming language for backend logic and SSR.
* **Jinja2**: Powerful templating engine for Python, allowing for easy creation of dynamic HTML.
* **SCSS (Sass)**: CSS pre-processing language, used to write modular, reusable, and easy-to-maintain styles.
* **RESTful API (External)**: The project expects to communicate with an external API that provides structured resume data. This API is essential for the generator's functionality.

---

## Features

* **Dynamic Resume Rendering**: Generates unique resumes for each user based on data received from the API.
* **Professional Styling with SCSS**: Utilizes a robust design system based on SCSS to ensure a cohesive and customizable look.
* **SSR (Server-Side Rendering)**: Improves initial performance, SEO, and accessibility, as the HTML content arrives ready for the browser.
* **External API Communication**: Fetches and displays resume data from a centralized data source.

---

## Getting Started

To run this project locally, follow the steps below:

### Prerequisites

Make sure you have the following tools installed:

* [Python 3.x](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installation/) (Python package manager)

### Setup

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/blink992/jinja_curriculum_render.git](https://github.com/blink992/jinja_curriculum_render.git)
    cd jinja_curriculum_render
    ```

2.  **Create and activate a virtual environment (recommended):**

    ```bash
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate

    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **API Configuration:**
    This project expects a **RESTful resume API** to be running at an accessible address.

    * Create a `.env` file in the project root (if necessary) and define your API's URL:
        ```
        API_URL=http://localhost:8000/api
        ```
    * Ensure the API is running and accessible.

### Running the Application

1.  **Activate the virtual environment:**
    ```
    .\venv\scripts\activate
    ```
3.  **Run the Uvicorn server:**
    ```bash
    uvicorn main:app --reload --reload-dir
    ```
4.  Open your browser and go to `http://localhost:5000` (or the configured port).

---

## Project Structure

```

jinja\_curriculum\_render/
├── venv/                 \# Python virtual environment
├── static/               \# Static files (CSS, JS, images)
│   ├── css/              \# Compiled CSS from SCSS
|   └── scss/             \# SCSS source code
|       ├── partials/     \# Partial files imported by main.scss
|       └── main.scss
├── templates/            \# Jinja2 templates
│   └── index.html
├── api.py                \# FastAPI initialization
├── external\_api.py       \# Communication with the external API
├── main.py               \# Main Python application logic
├── requirements.txt      \# Python dependencies
└── README.md             \# This file

```

---

## Contribution

Contributions are welcome! If you have suggestions or find bugs, please open an issue or submit a pull request.

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](./LICENSE.md) file for more details.

---

## Contact

Pedro Arthur Gregorio Abreu - [pedro.agb2004@gmail.com](mailto:pedro.agb2004@gmail.com)

GitHub Link: [https://github.com/meiyo-aru/jinja-curriculum](https://github.com/meiyo-aru/jinja-curriculum)

---
