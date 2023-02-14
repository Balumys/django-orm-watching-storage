# ORM Watching Storage
ORM Watching Storage, is a simple bank security control service written on `Django` framework.
Service allows you to monitor the following: 
- all active pass-card
- List of vault visits on a unique pass-card and whether they were suspicious or not
- list of pass-cards who still in vault

## How to install
### Pre-requests
Python3 should be already installed on your PC.

### Installation
You need few additional libraries to run the service.

To install them use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```
Once all dependencies installed, to get a test pass-card dataset `settings.py` file needs to be changed.
Use following settings
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': 'osim5',
    }
}
```

## Usage
### main.py
Main file, run it to start a local server.
`python3 main.py `

Example of success execute.

`Picture`

Click on hyperlink to open a webpage.
## Additional files
There only one django application ``datacenter`` in this service.
#### model.py
Contain **2** django models `Passcard` and `Visits`. 
With following structure:
```
class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)
    
    class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)
```
#### active_passcards_view.py
Showing number of active pass-card from ``Passcards``. Using `active_passcards.html` template.

#### passcard_info_view.py
Showing unique active pass-card from ``Passcards`` with all list of all visits from `Visit`.
If the visit was exceeded more than 60 minutes, flagged it as suspicious.
Using `active_passcards.html` template.
#### storage_information_view.py
Showing unique active pass-card from ``Passcards`` who wasn't leave a vault at the moment.
Using `storage_information.html` template.

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).