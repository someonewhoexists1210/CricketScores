# Cricket Score Flask App
This is a simple web application that provides real-time cricket match updates and player statistics. The application fetches data from an external API and displays it in a user-friendly format.

## Features
### Home Page
- Live Matches Overview: The homepage provides a summary of all currently ongoing cricket matches. It highlights matches that have started and are in progress, offering key details about each match.

### Player Search
- Search for Players: A dedicated page allows users to search for specific cricket players by name. After submitting a search query, users receive detailed statistics and information about the player, including recent performance data.

### Match Details
- In-Depth Match Information: Users can view detailed information about specific cricket matches. This includes comprehensive data such as team compositions, scores, and other critical match-related information.

### Request Limiting
- User Access Control: The application limits the number of requests a user can make from a single IP address. If a user exceeds the set limit, they are redirected to a page informing them that they have reached their request limit.

### Caching
- The application employs simple caching mechanisms to improve performance and reduce the load on the external API. This ensures a smoother user experience and helps manage data usage.

## Hosted
This website is hosted live at https://cricket.someonewhoexists.hackclub.app

## Contributing
You are welcome to contribute. Install this app on your local device make changes and push

### Installation
To run the website locally, follow these steps:

1. Clone repo
2. Install Dependencies: Ensure you have the required Python packages installed by running `pip install -r requirements.txt`.
3. Set Up Environment Variables: Create a `.env` file in the project root and add API key from CricAPI.
4. Start flask with `python app.py`.
5.  Visit `http://127.0.0.1:5000` in your web browser.

