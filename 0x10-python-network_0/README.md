# 0x10. Python - Network #0

This project focuses on network programming in Python. It covers various concepts related to HTTP, including URLs, HTTP requests and responses, headers, cookies, and cURL commands. The project also includes Bash scripts to interact with web servers using curl.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without using external references:

- Understanding URLs, HTTP, and their components
- Reading and interpreting URLs
- Understanding the scheme for an HTTP URL
- Differentiating domain names and sub-domains
- Defining port numbers in URLs
- Understanding query strings in URLs
- Understanding HTTP requests and responses
- Identifying HTTP headers and the HTTP message body
- Recognizing common HTTP request methods
- Identifying HTTP response status codes
- Understanding HTTP cookies
- Making requests using cURL
- Understanding the application-level process when typing a URL in a 
## Project Tasks

### 0. cURL body size

Write a Bash script that takes a URL as an argument, sends a request to that URL, and displays the size of the response body in bytes.

- The size must be displayed in bytes.
- cURL must be used for the request.

### 1. cURL to the end

Write a Bash script that takes a URL as an argument, sends a GET request to the URL, and displays the body of the response.

- Only the body of a 200 status code response should be displayed.
- cURL must be used for the request.

### 2. cURL Method

Write a Bash script that sends a DELETE request to a URL passed as the first argument and displays the body of the response.

- cURL must be used for the request.

### 3. cURL only methods

Write a Bash script that takes a URL as an argument and displays all the HTTP methods the server will accept.

- cURL must be used for the request.

### 4. cURL headers

Write a Bash script that takes a URL as an argument, sends a GET request to the URL, and displays the body of the response.

- A header variable `X-School-User-Id` with the value `98` must be sent.
- cURL must be used for the request.

### 5. cURL POST parameters

Write a Bash script that takes a URL as an argument, sends a POST request to the URL, and displays the body of the response.

- The request must include two variables: `email` with the value `test@gmail.com` and `subject` with the value `I will always be here for PLD`.
- cURL must be used for the request.

### 6. Find a peak

Write a function in Python that finds a peak in a list of unsorted integers.
