# Generate Test Cases

A Python tool that uses Language Models (LLM) to automatically generate test cases from business requirements and engineering specifications.

## Features

- Automatically generates comprehensive test cases from business requirements
- Supports multiple test case types (functional, non-functional, edge cases, etc.)
- Uses Google's Gemini model for high-quality test case generation
- Outputs test cases in CSV format for easy integration with test management tools
- Comprehensive logging for debugging and monitoring
- Configurable through settings

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/generate-test-cases.git
cd generate-test-cases
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the package:
```bash
pip install -e .
```

## Usage

1. Place your business requirements document (BRD) in `resources/target/brd-<resource-name>.md`
2. Optionally place your engineering requirements document (ERD) in `resources/target/erd-<resource-name>.md`
3. Run the tool:
```bash
python -m generate_test_cases
```

The generated test cases will be saved in the `output` directory with a timestamp in the filename.

## Project Structure

```
generate-test-cases/
├── src/
│   └── generate_test_cases/
│       ├── config/
│       │   ├── logging.py
│       │   └── settings.py
│       ├── core/
│       │   ├── llm_service.py
│       │   └── prompt_service.py
│       ├── utils/
│       │   └── file_service.py
│       └── __main__.py
├── resources/
│   ├── example/
│   │   ├── brd-ordertracking.md
│   │   ├── erd-ordertracking.md
│   │   └── tc-ordertracking.csv
│   └── target/
│       ├── brd-ordercreation.md
│       └── erd-ordercreation.md
├── output/
├── logs/
├── tests/
├── setup.py
└── README.md
```

## Configuration

The tool can be configured through the following files:

- `src/generate_test_cases/config/settings.py`: Main configuration file
- `src/generate_test_cases/config/logging.py`: Logging configuration

## Development

1. Install development dependencies:
```bash
pip install -e ".[dev]"
```

2. Run tests:
```bash
pytest
```

3. Format code:
```bash
black src tests
isort src tests
```

4. Run linting:
```bash
flake8 src tests
mypy src tests
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
