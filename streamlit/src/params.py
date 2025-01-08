# streamlit/src/params.py

import os

APP_NAME = 'streamlit'

# Folders
DATA_FOLDER = 'data'
ASSETS_FOLDER = 'assets'
PAGES_FOLDER = 'sites'
IMG_FOLDER = 'img'
CSS_FOLDER = 'css'

# URLs
GITHUB_URL = 'https://github.com/vicenteaguero/globalmonitor'
ABOUT_URL = 'https://geostrategos.com'

# Images
FAVICON = 'favicon.png'
LOGO_LIGHT = 'logo.png'
LOGO_DARK = 'logo-white.png'

# Styles
BASE_CSS = 'base.css'

################################################################################

# Base Paths
BASE_PATH = os.path.join(os.path.dirname(__file__), '..', '..')
DATA_PATH = os.path.join(BASE_PATH, DATA_FOLDER)

# App Paths
APP_PATH = os.path.join(BASE_PATH, APP_NAME)

# Paths
PATHS = {
    'assets': os.path.join(APP_PATH, ASSETS_FOLDER),
}

PATHS.update({
    'favicon': os.path.join(PATHS['assets'], IMG_FOLDER, FAVICON),
    'logo-light': os.path.join(PATHS['assets'], IMG_FOLDER, LOGO_LIGHT),
    'logo-dark': os.path.join(PATHS['assets'], IMG_FOLDER, LOGO_DARK),
    'base_css': os.path.join(PATHS['assets'], CSS_FOLDER, BASE_CSS),
})

################################################################################

# Automatic Sites Paths
PATHS.update(
    {
        'pages': {
            os.path.splitext(x)[0]:
                os.path.join(APP_PATH, PAGES_FOLDER, x)
                for x in os.listdir(os.path.join(APP_PATH, PAGES_FOLDER))
        }
    }
)
