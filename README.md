# Career Compass

#### Video Demo: [https://youtu.be/JcJ2H30gzNg](https://youtu.be/JcJ2H30gzNg)

#### Description:
Rapid advancements in technology have led to an evolving job market making it difficult for people to plan their futures, and figure out what career suits them best. 

This inspired Career Compass, an AI powered tool designed to help give users career paths that align with their strengths, interests, and goals. Career Compass provides a user-friendly experience, through a simple form that collects user information, and uses OpenRouter's AI models to suggest potential career paths.

#### Key Features:
- Multi-step form built with JS
- Takes user inputs, including strengths, hobbies, career goals, and more
- Uses OpenRouter's 'mistralai/mistral-7b-instruct' for analysis, and personalized career suggestions
- Returns 3 personalized career paths, including education requirements, work-life balance, and salary ranges
- Live hosting through Render at: [https://career-compass-tmvx.onrender.com](https://career-compass-tmvx.onrender.com)

#### Technologies used:

- **HTML/CSS/JS:** stylized, interactive front-end that collects user input, and sends it to the backend.
- **Flask (Python):** backend server that takes user input, formats it into a prompt to send to the OpenRouter API, then sends the response back to the frontend to be displayed to the user
- **Bootstrap:** used for styling and layout
- **OpenRouter API:** OpenRouter is a platform that provides API access to a variety of language models. I chose Mistralai's 7b instruct model (because it was free) to process the user input, provide career options, and send the information back to the python server.
- **Render:** free cloud platform used for hosting and deployement
- **Git/Github:** remote repository to store all project files. Integrates with VSCode and Render, keeping track of code changes, and updating the live site through render

#### Overview:
1. User answers questions about themselves.
2. Inputs are sent to the backend, where they are compiled into a prompt
3. The OpenRouter API recieves the prompt, and returns personalized career paths.
4. The results are displayed to the user, and the user gets an option to start again.

## Next steps:

#### Custom trained AI model:
Career Compass currently uses a pre-trained model through openrouter. This model has been trained for general chatbot use, and is not optimized to predict which careers will be big in the future. I plan to train a specialized AI model focused on analyzing employement trends, and predicting new and emerging career paths. This involves collecting data from the job market at a large scale, using platforms like LinkedIn and Indeed, then fine tuning transformer models on these datasets. This would lead to an AI model that is constantly learning, and is better at identifying which skills translate well into certain careers.

I wasn't able to do this yet because of a lack of technical knowledge, resources, and time, but I hope to implement this idea in the future.

#### Other improvements:

- Allow users to create accounts in order to get a deeper understanding of each user through things like personality tests, and by other important information about users. Also give users a wider range of career-paths, spanning multiple industries, going further in-depth into what the user should do to get into this career, and discuss the pros and cons of different pathways.
- Add detailed explanations for the reasoning for each of the career pathways
- Add support for multiple different languages