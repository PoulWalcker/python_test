# Test assignment for a Python test automation

## Overview

This project is a small automated test suite written in **Python** using **pytest** and **requests**.  
The goal is to test basic CRUD operations (`GET`, `POST`, `PUT`, `DELETE`) for the `/posts` endpoint of the public API **[JSONPlaceholder](https://jsonplaceholder.typicode.com/)**.
---

## Project structure

```
project/
├── tests/
│   ├── __init__.py           
│   ├── conftest.py           
│   └── test_posts.py        
├── pyproject.toml            
├── README.md                 
└── .gitignore                
```

---

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies with Poetry:

```bash
pip install poetry
poetry install
```

---

## Running tests

To run all tests with detailed output:

```bash
poetry run pytest -v
```

To run a specific test file:

```bash
poetry run pytest tests/test_posts.py -v
```

---

## Example output

```
tests/test_posts.py::TestPosts::test_status_code[1] PASSED                                                                                                                                      
tests/test_posts.py::TestPosts::test_status_code[10] PASSED                                                                                                                                   
tests/test_posts.py::TestPosts::test_status_code[100] PASSED                                                                                                                                   
tests/test_posts.py::TestPosts::test_get_wrong_path_404 PASSED                                                                                                                                 
tests/test_posts.py::TestPosts::test_get_post_data[1] PASSED                                                                                                                                   
tests/test_posts.py::TestPosts::test_get_post_data[10] PASSED                                                                                                                                  
tests/test_posts.py::TestPosts::test_get_post_data[100] PASSED                                                                                                                                 
tests/test_posts.py::TestPosts::test_get_posts_list PASSED                                                                                                                                     
tests/test_posts.py::TestPosts::test_create_post_data[payload0] PASSED                                                                                                                         
tests/test_posts.py::TestPosts::test_create_post_data[payload1] PASSED                                                                                                                         
tests/test_posts.py::TestPosts::test_update_post_put_data PASSED                                                                                                                               
tests/test_posts.py::TestPosts::test_patch_post_data PASSED                                                                                                                                    
tests/test_posts.py::TestPosts::test_delete_post PASSED   
```
