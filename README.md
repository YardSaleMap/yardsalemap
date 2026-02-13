# Yard Sale Map

## Project Overview
Yard Sale Map is a web application that helps users locate yard sales in their area. This user-friendly platform allows users to view, post, and share information about ongoing yard sales.

## Features
- **Map Integration:** Users can easily find nearby yard sales on an interactive map.
- **Search Functionality:** Search for sales by keyword, date, or location.
- **User Accounts:** Users can create accounts to save their favorite sales.
- **Post Sales:** Users can easily post their own yard sales with details and photos.

## Tech Stack
- **Frontend:** React.js, Redux
- **Backend:** Node.js, Express
- **Database:** MongoDB
- **APIs:** Google Maps API, Mapbox API

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/YardSaleMap/yardsalemap.git
   cd yardsalemap
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Set up the environment variables. Create a `.env` file in the root directory:
   ```
   touch .env
   ```
   Then add the required variables such as your database connection string and API keys.
4. Run the application:
   ```bash
   npm start
   ```

## Usage Guide
- After launching the app, you can create an account or log in if you already have one.
- Browse the map to find yard sales near you. 
- Click on a marker to view details about the yard sale.
- To post a new yard sale, click the "Post Sale" button and fill in the form.

## Contribution Guidelines
We welcome contributions to Yard Sale Map! To contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push to your forked repository:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request. We will review your changes and merge them if they align with our goals.

Thank you for helping improve Yard Sale Map!