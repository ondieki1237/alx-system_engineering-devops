tack debugging #3

## Description

This project focuses on diagnosing and debugging web stack issues. As part of the series on web stack debugging, we dive into real-world scenarios where the web stack is misbehaving, and we apply our knowledge of Linux systems, web servers, and debugging tools to resolve these issues.

## Learning Objectives

By completing this project, you will:
- Develop a deeper understanding of web stack components.
- Learn how to diagnose and resolve issues within a web stack.
- Gain proficiency in using various debugging tools and techniques.

## Requirements

- **OS:** Ubuntu 20.04 LTS or similar
- **Software:** Apache/Nginx web server, curl, wget, and other standard Linux tools.
- **Scripts:** All Bash scripts must be executable and follow the Shell script coding style (`#!/bin/bash` at the start of the script).

## Project Structure

- **0-give_me_a_page:** 
  - A Bash script that fetches the homepage of the local server and checks if it returns a `200` status code.
  
- **1-fix_infinite_loop:** 
  - A Bash script that identifies and resolves an infinite loop issue in the web server configuration.
  
- **2-debug_web_stack:** 
  - A Bash script that identifies a misconfiguration in the web server and fixes it to ensure the server responds correctly.
  
- **3-run_shell_script:** 
  - A Bash script that automates the process of debugging a common issue in a web stack.

## Usage

To use the scripts in this project:

1. Clone the repository:
   ```bash
   git clone https://github.com/ondieki1237/0x17-web-stack-debugging-3.git

