# Contributing to Renewable Energy Analysis Project

Thank you for considering contributing to our Renewable Energy Analysis project! This initiative is focused on developing insightful analyses and innovative tools to better understand the dynamics of renewable energy markets and technologies. We welcome contributions from a wide range of experts and enthusiasts in the field.

## How to Contribute

### Issues and Discussions

- **Bugs & Issues**: If you find a problem within our analysis or scripts, please report it by opening an issue on our [GitHub Repository](https://github.com/DSCI-310-2024/DSCI310-Group14). Include as much detail as possible to facilitate quick resolutions.

- **Feature Requests & Suggestions**: Your ideas are valuable to us! Submit your suggestions for new features or improvements through our GitHub issues.

- **Questions & Discussions**: Engage with our community by starting discussions on our GitHub page. Whether it's a question or a discussion on potential improvements, your input is welcome.

### Code Contributions

If you'd like to contribute code, follow these steps:

#### Setting Up Your Environment

1. Fork the Renewable Energy Analysis repository on GitHub.
2. Clone your fork to your local machine:
    ```bash
    git clone https://github.com/DSCI-310-2024/DSCI310-Group14
    ```
3. Set up your development environment. Make sure all dependencies are installed:
    ```bash
    conda env create -f team-14_environment.yml
    conda activate team-14
    ```
4. Sync your fork with the main repository to keep it up-to-date:
    ```bash
    git remote add upstream https://github.com/DSCI-310-2024/DSCI310-Group14
    git fetch upstream
    git checkout main
    git merge upstream/main
    ```

#### Making Changes

1. Create a new branch for your work:
    ```bash
    git checkout -b your-branch-name
    ```
2. Implement your changes, add new features, or fix bugs. Ensure that your code adheres to the existing style and standards.
3. Thoroughly test your changes.

#### Submitting Your Contribution

1. Commit your changes with descriptive messages:
    ```bash
    git add .
    git commit -m "Add a concise, informative description of your changes"
    ```
2. Push your branch to your GitHub fork:
    ```bash
    git push origin your-branch-name
    ```
3. Create a pull request against the main repository. Provide a clear description of your changes and any additional context necessary.

### Documentation Contributions

Good documentation is crucial:

- **Improving Documentation**: Help clarify instructions, add missing content, or improve the existing material.

### Review Process

All contributions will be reviewed by project maintainers. Constructive feedback will be provided, and necessary revisions may be requested to ensure high quality and consistency.

## Code of Conduct

By participating, you agree to abide by our [Code of Conduct](./CODE_OF_CONDUCT.md). We are committed to making participation in this project a harassment-free experience for everyone.

## Questions?

If you have questions or need assistance with contributing, please don't hesitate to reach out through GitHub issues or discussions.

---

Thank you for contributing to the Renewable Energy Analysis project! Your contributions are vital to our mission of advancing renewable energy knowledge and practices.