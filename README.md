# Course-ChatGPT-Business-Solutions
A collection of Azure Functions demonstrating the integration of ChatGPT for creating advanced AI-powered solutions and applications. This repository includes various approaches like handler-based, route-based, and original folder structures as part of a masterclass course project.

## Introduction
This repository serves as a hub for the learnings and codebase developed while navigating an outdated course on Azure Functions and OpenAI integration. It stands as a testimony to adaptability in the face of evolving technologies and the importance of persistence and problem-solving in software development.

## Project Description
Throughout this project, I've updated the course material in real-time to align with the latest Azure Functions (v2) and OpenAI API changes. This repository documents the critical transition from outdated methods to current best practices, reflecting a significant learning curve and the mastery of modern development tools and approaches.

## Challenges Faced
- Outdated course material referencing deprecated methods and configurations.
- Adapting to Azure Functions' newer Python-based programming model.
- Integrating with the revised OpenAI API, shifting from GPT-3 to the latest GPT-4 and dealing with changes in API structure and responses.
- Learning to leverage Git for efficient version control and project management across different development environments.

## Resolutions and Learnings
- Moved away from using `__init__.py` and `function.json` in separate folders to a centralized hierarchical approach with `function_app.py`.
- Transitioned from local testing methods to employing Azure extensions for execution, aligning with the designed environment of VS Code.
- Overcame numerous technical issues by engaging with ChatGPT and community forums, emphasizing the value of collaboration and external support.

## Key Takeaways
- **Adaptability**: Staying current with tools and technologies is non-negotiable in software development.
- **Version Control**: Git is essential for tracking changes, experimenting with new ideas through branching, and managing project history.
- **Continuous Learning**: Keeping abreast of official documentation and updates from tool providers is vital.
- **Problem-Solving**: Effective troubleshooting and problem-solving skills are indispensable assets.
- **Documentation**: Maintaining comprehensive documentation is invaluable for personal reference and for aiding others facing similar issues.

## Repository Structure
- `function_app.py`: Centralized file for Azure Functions code.
- `requirements.txt`: Lists the dependencies for the project to ensure consistent environments.
- `/docs`: Documentation detailing the process, challenges, and solutions encountered.
- `/experimental`: Branching codesets exploring different methodologies such as handler.py and route-based functions.

## Getting Started

This section provides a step-by-step guide to setting up the project, reflecting the update from the older Azure Functions and OpenAI integration methods to the newer, centralized approach that aligns with the latest versions of Azure Functions and OpenAI's GPT model.

### Prerequisites

- An Azure account with an active subscription.
- Visual Studio Code with the Azure Functions extension installed.
- The latest version of Python installed on your local development machine.
- A valid OpenAI API key to interact with OpenAI's GPT models.
- Git installed for version control.

### Setup

1. **Clone the Repository**: Start by cloning this repository to your local machine using Git.
     git clone <repository-url>

2. **Environment Configuration**: Navigate to the cloned project directory and create a .env file to store your OpenAI API key securely.
     echo "OPENAI_API_KEY=your_openai_api_key" > .env

3. **Install Dependencies**: Install the required Python packages defined in the requirements.txt.
    pip install -r requirements.txt

4. **Local Development**: Open the project in Visual Studio Code. Use the integrated terminal to start the Azure Functions local runtime.
    func start
   This will start the Azure Functions runtime and provide you with URLs to trigger the functions locally.

5. **Testing the Function**: Use the provided HTTP endpoints to test the Azure Function. For example, to test the completionAPI, you can send a GET or POST request to the local server.
    # For a GET request
    curl http://localhost:7071/api/completionAPI?prompt="Who was Deborah Sampson"

    # For a POST request
    curl -X POST -H "Content-Type: application/json" -d '{"prompt": "Who was Deborah Sampson"}' http://localhost:7071/api/completionAPI
    Ensure that the function responds with the expected output from the OpenAI API.

Ensure that the function responds with the expected output from the OpenAI API.

**Transition from Old to New Method**
The original course material instructed students to create separate folders for each function with its own __init__.py and function.json. However, the updated approach centralizes the function definition within a single function_app.py, simplifying the structure and reflecting current best practices.
Additionally, local testing and debugging methods have been updated. Instead of relying on external tools, we now utilize the Azure Functions extension within VS Code, which provides an integrated experience and simplifies the development process.
The OpenAI API integration has been updated to the latest GPT model and the corresponding API usage. Instead of using deprecated endpoints, the new method employs the latest chat.completions.create API call.

**Next Steps**
Once you have successfully tested the function locally, you can proceed to deploy the function to Azure and continue developing additional features or functions as per the course content or your project requirements.

Make sure to replace `<repository-url>` with your actual repository URL and `your_openai_api_key` with your real OpenAI API key. This guide aims to bring someone who's new to the course material up to speed with the current technologies and project setup that you've established.


## Contributions and Feedback
We welcome contributions and feedback on this project! If you have ideas on how to improve the code or features, or if you encounter any issues, please feel free to contribute or open an issue.

Contributing
Fork the Repository: Start by forking the repository. This allows you to make changes without affecting the original project.
Create a Branch: For each new feature or fix, create a new branch. Describe the feature or fix in the branch name.
Make Your Changes: Implement your changes or improvements in your branch. Be sure to test your changes!
Submit a Pull Request: Once you are satisfied with the enhancements, submit a pull request. Please provide a clear description of the problem and solution, including any relevant issue numbers.
Code Review: A review will take place, and suggestions for changes may be discussed. Once approved, your contribution will be merged.
Feedback
If you have any feedback or suggestions, please open an issue in the repository. We strive to make this project as effective as possible and appreciate any insights you can provide.

## Acknowledgments
This project would not have been possible without the support and resources provided by several key contributors and communities:

ChatGPT: Special thanks to ChatGPT for being an instrumental resource in troubleshooting and refining the development process. The AI's insights and guidance helped overcome many technical challenges.
Udemy Course Community: Gratitude to the fellow learners in the Udemy course for their ongoing support and discussions that have enriched this learning journey.
OpenAI Community: Thanks to the OpenAI community for providing comprehensive documentation and forums where I could learn from other developers' experiences and solutions.
GitHub Community: A big thank you to the wider GitHub community, whose open-source projects inspired and informed various aspects of this work.
Personal Mentors and Peers: Heartfelt thanks to my mentors and peers who provided feedback, code reviews, and moral support throughout the development process.
This project is a testament to the power of collaborative learning and the open-source community. Thank you to everyone who has contributed, directly or indirectly, to its success.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

## Project History and Milestones
Initial Concept
November 2023: The project commenced with the basic idea to integrate OpenAI's API into an Azure Functions application. Initial setup included the creation of a simple HTTP trigger function to explore API capabilities.
Development Challenges
December 2023 2024: Encountered issues with outdated course materials. Realized the necessity to adapt to Azure Functions Python v2 and OpenAI's latest API changes, leading to extensive research and experimentation.
December-January 2023-2024: Implemented a new architecture based on Azure Functions without the use of traditional __init__.py and function.json in separate folders. Transitioned to a more centralized approach to streamline development.
Integration and Testing
January 2024: Successfully integrated OpenAI's ChatGPT API with Azure Functions. Developed several functions to handle different types of requests and experimented with local and cloud-based testing.
March 2024: Focused on error handling and optimizing API calls to improve response times and reliability.
Community Engagement and Feedback
April 2024: Open-sourced the project on GitHub to invite feedback and contributions from other developers facing similar issues with outdated course materials. Set up a Git repository to manage version control and collaborative development.
Future Enhancements
Planned for future: 2024: Incorporate additional AI models and expand the application's functionality based on user feedback. Explore the use of Azure’s more advanced features to enhance application scalability and security.


## Getting Started

This section provides a step-by-step guide to setting up the project, reflecting the update from the older Azure Functions and OpenAI integration methods to the newer, centralized approach that aligns with the latest versions of Azure Functions and OpenAI's GPT model.

### Prerequisites

- An Azure account with an active subscription.
- Visual Studio Code with the Azure Functions extension installed.
- The latest version of Python installed on your local development machine.
- A valid OpenAI API key to interact with OpenAI's GPT models.
- Git installed for version control.

### Setup

1. **Environment Setup**: Make sure your development environment is ready with the necessary tools installed, including Python, Git, and the Azure Functions Core Tools.
2. **Clone the Repository**: Start by cloning this repository to your local machine using Git.
   git clone <repository-url>
3. **Configure Environment Variables**: Securely store your API keys and other sensitive information using environment variables.
   echo "OPENAI_API_KEY=your_openai_api_key" > .env
4. **Install Dependencies**: Set up your Python environment and install dependencies to ensure all necessary libraries are available.
   pip install -r requirements.txt
5. **Start Local Development**: Launch the Azure Functions runtime to begin local testing and development.
   func start
6. **Explore and Test**: Use the provided URLs or the Azure Functions extension in Visual Studio Code to test the functions and explore their responses.

**Transition to Updated Methods**
The project has moved away from the segmented directory structure that required separate __init__.py and function.json files for each function. Instead, it now utilizes a single function_app.py file, reflecting a more streamlined approach that aligns with current Azure Functions best practices. This simplifies the development and deployment process, particularly for newcomers.

Next Steps
Once the project is running locally, you may wish to deploy it to Azure to utilize cloud capabilities, or expand the project's functionality based on the course's upcoming modules or personal enhancements.
