# PyJLogger

A flexible and customizable logging library for Python, designed to provide structured log entries in JSON format. This logger supports various log levels, including DEBUG, INFO, WARNING, EXCEPTION, ERROR, and CRITICAL. It can output logs to the console and save them to a JSON file with timestamps, module names, function names, and line numbers for easy debugging.

## Features

- **Customizable Log Levels**: Supports DEBUG, INFO, WARNING, EXCEPTION, ERROR, and CRITICAL levels.
- **Structured JSON Output**: Logs are formatted as JSON for easy parsing and integration with log management systems.
- **Dynamic Logger Name**: Specify custom logger names for different modules or components.
- **File Logging**: Logs are saved to daily JSON files for persistent storage.
- **No Dependencies**: Pure Python implementation with no external dependencies.

## Installation

Clone the repository and include the `logger.py` file in your project:
```bash
git clone https://github.com/Hex-21/PyJLogger.git
```
## Usage
```python
import PyJLogger
logger = PyJLogger.get_logger("test_logger_name", 3)


def testfunc():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warn("This is a warning message")
    logger.exception("This is an exception message")
    logger.error("This is an error message")
    logger.crit("This is a critical message")


if __name__ == "__main__":
    testfunc()
```
## Example output:
```json
{"timestamp": "2024-07-20#18:14:31.686", "level": "EXCEPTION", "message": "This is an exception message", "logger": "test_logger_name", "module": "tester.py", "function": "testfunc", "line": 9}
{"timestamp": "2024-07-20#18:14:31.686", "level": "ERROR", "message": "This is an error message", "logger": "test_logger_name", "module": "tester.py", "function": "testfunc", "line": 10}
{"timestamp": "2024-07-20#18:14:31.686", "level": "CRITICAL", "message": "This is a critical message", "logger": "test_logger_name", "module": "tester.py", "function": "testfunc", "line": 11}
```
## {Date}.json output
```json
{"timestamp": "2024-07-20#18:14:31.686", "level": "DEBUG", "message": "This is a debug message", "logger": "test_logger_name", "module": "tester.py", "function": "testfunc", "line": 6}
{"timestamp": "2024-07-20#18:14:31.686", "level": "INFO", "message": "This is an info message", "logger": "test_logger_name", "module": "tester.py", "function": "testfunc", "line": 7}
{"timestamp": "2024-07-20#18:14:31.686", "level": "WARNING", "message": "This is a warning message", "logger": "test_logger_name", "module": "tester.py", "function": "testfunc", "line": 8}
{"timestamp": "2024-07-20#18:14:31.686", "level": "EXCEPTION", "message": "This is an exception message", "logger": "test_logger_name", "module": "tester.py", "function": "testfunc", "line": 9}
{"timestamp": "2024-07-20#18:14:31.686", "level": "ERROR", "message": "This is an error message", "logger": "test_logger_name", "module": "tester.py", "function": "testfunc", "line": 10}
{"timestamp": "2024-07-20#18:14:31.686", "level": "CRITICAL", "message": "This is a critical message", "logger": "test_logger_name", "module": "tester.py", "function": "testfunc", "line": 11}
```


## Configuration

- **Log Level**: Set the desired log level when creating a logger instance. Logs below this level will be ignored.
- **Log File Naming**: Logs are saved in files named with the current date, e.g., `2024-07-20.json`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.
