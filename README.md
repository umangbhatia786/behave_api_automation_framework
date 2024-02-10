# Behave API Automation Framework

This framework is designed for API testing using the Behave BDD (Behavior-Driven Development) framework. It allows for writing tests in a natural language style, making the test cases easy to read and understand.

## Features

- **BDD Approach**: Utilizes the Behave framework for Python to write tests in Gherkin syntax.
- **Configurable**: Customizable settings through `behave.ini` for different testing environments.
- **Reporting**: Supports generating reports in multiple formats, including Allure and JUnit, through Behave's formatter options.
- **Integration**: Can be integrated with CI/CD pipelines for automated testing.

## Getting Started

### Prerequisites

- Python 3.x
- Behave
- Allure (for Allure reports)

### Installation

1. Clone the repository to your local machine.
2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

### Running Tests

To run all tests, use the following command:

```
behave
```

To run a specific feature file:

```
behave features/my_feature.feature
```

### Configuration

The framework's behavior can be customized by editing the `behave.ini` file. For example, to change the reports directory:

```ini:behave_api_automation_framework/behave.ini
9|ALLURE_REPORTS_DIR=new_reports_directory
```

### Generating Reports

To generate Allure reports, run:

```
behave -f allure_behave.formatter:AllureFormatter -o test_reports/allure.reports
```

## Contributing

Contributions are welcome. Please read the contributing guidelines before submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details
