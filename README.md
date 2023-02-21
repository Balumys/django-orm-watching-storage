# ORM Watching Storage
ORM Watching Storage, is an internal bank security control service written on `Django` framework.
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
Once all dependencies installed, next step is create **.env** file which should contain all sensitive-secured information.
```
DATABASE_HOST=Address to database
DATABASE_PASSWORD=Your password
SECRET_KEY=Your secret key
```

## Usage
### manage.py
Main file, run it to start a local server.
`python3 manage.py runserver 0.0.0.0:8000 `

Example of success execute.

![Screenshot 2023-02-14 at 13 54 47](https://user-images.githubusercontent.com/123511478/218734487-307b9d77-82b7-4843-a93f-4814543cc014.png)


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

![Screenshot 2023-02-14 at 14 31 57](https://user-images.githubusercontent.com/123511478/218734564-fbdf5dfa-7881-466a-ac57-9b0a5afe40fa.png)

#### passcard_info_view.py
Showing unique active pass-card from ``Passcards`` with all list of all visits from `Visit`.
If the visit was exceeded more than 60 minutes, flagged it as suspicious.
Using `active_passcards.html` template.
![Screenshot 2023-02-14 at 14 32 16](https://user-images.githubusercontent.com/123511478/218734631-a8b9eecf-4a46-4b60-9a63-0069143799c7.png)

#### storage_information_view.py
Showing unique active pass-card from ``Passcards`` who wasn't leave a vault at the moment.
Using `storage_information.html` template.
![Screenshot 2023-02-14 at 14 32 28](https://user-images.githubusercontent.com/123511478/218734665-e4cba6fd-d43e-4e3f-b9b9-4958ea11316e.png)

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
