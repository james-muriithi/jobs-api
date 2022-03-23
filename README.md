# Jobs API
Coding jobs api

## Enpoints
**Root Endpoint**
[]()

> POST

`/api/auth`

data passed
```json
{
    "username": "john",
    "password": "password"
}
```

return
```json
{
    "token": "692f386656f4c0606cd86d4710342"
}
```
---

> POST

create a new job

`api/jobs`


data passed
```json
{
    "title": "Business Analyst",
    "location": "Nairobi Kenya",
    "company": "Telkom Kenya",
    "job_type": "FUll time",
    "salary": "Ksh Confidential",
    "link": "https://www.fuzu.com/kenya/jobs/business-analyst-telkom-kenya-45c20c60",
    "post_date": "Apr 1, 2022",
    "summary": "summary",
    "full_text": "Job Requirements...."
}
```

return
```json
{
    "id": 1,
    "title": "Business Analyst",
    "location": "Nairobi Kenya",
    "company": "Telkom Kenya",
    "job_type": "FUll time",
    "salary": "Ksh Confidential",
    "link": "https://www.fuzu.com/kenya/jobs/business-analyst-telkom-kenya-45c20c60",
    "post_date": "Apr 1, 2022",
    "summary": "summary",
    "full_text": "Job Requirements....",
    "created_at": "23-03-2022"
}
```

---
> GET

get all jobs

`api/jobs`

returns jobs paginated by 25 posts

pass page paramenter to url for pagination e.g. `api/jobs?page=2`


## Technologies Used
The following technologies have been used on this project:
* Django
* Python
* Django Rest Framework

# Setup / Installation
* clone the repo:

```shell
git clone https://github.com/james-muriithi/jobs-api.git
```

```
cd blog
```
* create virtual environment 

```shell
python3.8 -m venv --without-pip venv
```

* To activate the virtual environment
```shell
source venv/bin/activate
```

* install the packages from requirements.txt
```shell
pip install -r requirements.txt 
```

* setup environment variables
```shell
cp .env.example .env
```
* Start the server
```shell
python3.8 manage.py runserver
```


## Contact details
Email: james@student.moringaschool.com

## MIT licence

<p>Copyright (c) 2022 Moringa School </p>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.