# API Lambda DynamoDB

## Use Case

In this exercise, you'll create a serverless API that allows users to submit and retrieve news. The application will be built using AWS services such as `API Gateway`, `Lambda`, and `DynamoDB`. 

### Overview

The application provides an endpoint where users can submit a new with a title and content. The new is then stored in a DynamoDB table. Another endpoint allows users to retrieve a new by its unique ID.

### Components

1. **API Gateway**: 
   - Provides a RESTful API interface for clients to interact with the service.
   - Handles HTTP requests and routes them to the appropriate Lambda function.

2. **Lambda Function**: 
   - Serves as the backend logic for processing incoming API requests.
   - Handles the creation and retrieval of news.
   - Interacts with DynamoDB to save and fetch data.

3. **DynamoDB**: 
   - Stores the news with attributes such as `NewID`, `Title`, `Content`, and `Timestamp`.
   - Provides fast and scalable data storage.

### Endpoints

1. **POST /news**:
   - Description: Creates a new new.
   - Request Body: JSON object with `title` and `content` fields.
   - Response: A JSON object with the `NewID` of the newly created new.

2. **GET /news/{id}**:
   - Description: Retrieves a new by its `NewID`.
   - Path Parameter: `id` - The unique identifier of the new.
   - Response: A JSON object with `NewID`, `title`, `content`, and `timestamp`.