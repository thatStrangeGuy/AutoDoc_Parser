import logging
from pathlib import Path
from logging import handlers

from controllers import config_controller

logger = logging.getLogger("init.controller")
fh = logging.handlers.RotatingFileHandler(filename='init_log.log', maxBytes=10000, backupCount=20, encoding='utf-8')
FORMAT = '%(asctime)s :: %(name)s:%(lineno)s :: %(levelname)s :: %(message)s'
fh.setLevel(logging.INFO)
fh.setFormatter(logging.Formatter(FORMAT))
logger.addHandler(fh)


def init_check_config(file_path):
    if isinstance(file_path, str):
        file_path = Path(file_path)
    if not file_path.exists():
        logger.warning("No Config Found, Creating a default one")
        config_controller.restore_default_config()


def check_dirs_system():
    config = config_controller.read_config('config.yaml')
    db_dir = Path(config.get('db_dir', Path().absolute().joinpath('db')))
    logs_dir = Path().absolute().joinpath('logs')
    if not logs_dir.exists():
        logger.warning("No logs Directory, Creating a default one")
        logs_dir.mkdir(parents=True)
    del logs_dir
    if not db_dir.exists():
        logger.warning("No Database Directory, Creating a default one")
        db_dir.mkdir(parents=True)
    del db_dir, config

    UI_dir = Path().absolute().joinpath('UI')
    if not UI_dir.exists():
        logger.warning("No UI Directory, Creating a default one")
        UI_dir.mkdir(parents=True)
        logger.warning("No UI File, Creating a default one")
        create_default_stylesheet()


def create_default_stylesheet():
    css_path = Path().absolute().joinpath('UI', 'style_main.css')
    css = '''
    QWidget {
    background-color: #171a21; /* Steam's Dark Theme Background Color */
    color: #c6d4df; /* Steam's Text Color */
    font-size: 12px;
}

QLabel {
    background-color: #1b2838; /* Steam's Button Background Color */
    color: #ffffff; /* White text for buttons */
    border: 1px solid #1b2838;
    border-radius: 12px;
    padding: 5px 10px;
}


QPushButton {
    background-color: #1b2838; /* Steam's Button Background Color */
    color: #ffffff; /* White text for buttons */
    border: 1px solid #1b2838;
    border-radius: 12px;
    padding: 5px 10px;
}

QPushButton:hover {
    background-color: #2d435e; /* Darker shade on hover */
}

QPushButton:pressed {
    background-color: #122031; /* Darker shade when pressed */
}

QLineEdit {
    background-color: #1c2735; /* Steam's Input Field Color */
    border: 1px solid #1c2735;
    padding: 5px;
    color: #c6d4df; /* Steam's Text Color */
    border-radius: 4px;
}

QLineEdit:focus {
    border: 1px solid #5a90d8; /* Steam's Accent Color on focus */
}

QTextEdit {
    background-color: #1c2735; /* Steam's Input Field Color */
    border: 1px solid #1c2735;
    padding: 5px;
    color: #c6d4df; /* Steam's Text Color */
    border-radius: 4px;
}

QTextEdit:focus {
    border: 1px solid #5a90d8; /* Steam's Accent Color on focus */
}

QScrollBar:vertical {
    border: none;
    background: #171a21; /* Steam's Scroll Bar Background */
    width: 12px;
    margin: 0px 0px 0px 0px;
}

QScrollBar::handle:vertical {
    background: #5a90d8; /* Steam's Scroll Bar Handle */
    min-height: 20px;
    border-radius: 6px;
}

QScrollBar::add-line:vertical {
    background: none;
}

QScrollBar::sub-line:vertical {
    background: none;
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: none;
}

QProgressBar {
    border: 1px solid #5a90d8; /* Border color */
    border-radius: 5px;
    background-color: #1c2735; /* Background color of the bar */
    text-align: center;
}

QProgressBar::chunk {
    background-color: #5a90d8; /* Color of the progress */
    width: 20px; /* Width of each progress chunk */
}
QRadioButton {
    color: #c6d4df; /* Text color */
}

QRadioButton::indicator {
    width: 14px; /* Size of the radio button */
    height: 14px;
    border: 2px solid #5a90d8; /* Border color of the radio button */
    border-radius: 7px; /* Makes it round */
}

QRadioButton::indicator:checked {
    background-color: #5a90d8; /* Color when checked */
    border: 2px solid #5a90d8; /* Border color when checked */
}

QRadioButton::indicator:hover {
    border: 2px solid #5a90d8; /* Border color on hover */
}
QCheckBox {
    color: #c6d4df; /* Text color */
}

QCheckBox::indicator {
    width: 14px; /* Size of the checkbox */
    height: 14px;
    border: 2px solid #5a90d8; /* Border color of the checkbox */
    border-radius: 3px; /* Makes it slightly rounded */
}

QCheckBox::indicator:checked {
    background-color: #5a90d8; /* Color when checked */
    border: 2px solid #5a90d8; /* Border color when checked */
}

QCheckBox::indicator:hover {
    border: 2px solid #5a90d8; /* Border color on hover */
}
QDialogButtonBox {
    background-color: #1c2735; /* Background color */
}

QDialogButtonBox QPushButton {
    background-color: #7289da; /* Button background color */
    color: #ffffff; /* Button text color */
    border: 1px solid #7289da; /* Button border color */
    border-radius: 4px;
    padding: 5px 10px;
    margin-right: 5px;
}

QDialogButtonBox QPushButton:hover {
    background-color: #677bc4; /* Darker shade on hover */
}

QDialogButtonBox QPushButton:pressed {
    background-color: #5865a6; /* Darker shade when pressed */
}

QToolTip {
    border: 1px solid #c8c8c8;
	background-color: #171a21; /* Steam's Dark Theme Background Color */
    color: #c6d4df; /* Steam's Text Color */
    font-size: 12px;
	border-radius:5px;
    }
    '''
    with open(css_path, 'w') as style_file:
        style_file.write(css)


def init_check():
    check_dirs_system()
    init_check_config(Path().absolute().joinpath('config.yaml'))
