# **MS4- Keep it SWEET! Deployment &amp; Local Development**

![amiresponsive mock-ups of SHOP Keep It Sweet](./docs/mockup-1.png)

<br/>

**[Link to the Deployed Site](https://keep-it-sweet-2ecaa2229785.herokuapp.com/)**

---
## **Deployment Steps**

Keep It Sweet is deployed on Heroku and uses AWS3 for staticfiles cloud storage.

**1. Install the Project Requirements by Creating a `requirements.txt` File**  
- Open the terminal and run the following command:  
  ```bash
  pip3 freeze > requirements.txt
  ```
- This will create  a `requirements.txt` file that lists all the dependencies required for the products and the specific versions of those dependencies.

**2. Create an External Database Using Code Institute's PostgreSQL** <br/>
The default Django database is suitable for development but not for production or deployment on Heroku. To set up a production database:
* Navigate to- [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) 
* Enter your student email into the field provided and press submit.
* Check the student email associated with account for a link to the newly created Postgres database.

**3. Set Up a New Heroku App**  
- Visit [Heroku.com](https://www.heroku.com/) and log in to your account.  
- Click the **New** button and select *Create New App* from the dropdown menu.  
- Enter a name for your app, choose your region, and click *Create App*.  
- Navigate to the **Settings** tab of your new app.  
- Click *Reveal Config Vars* under the Config Vars section.  
- Add a new Config Var with the key **DATABASE_URL** and paste your PostgreSQL database URL as the value.  

**4. Connect the External Database to GitPod**  
- In GitPod, use the terminal to install the **dj-database-url** package (version 0.5.0) and **psycopg2**, which are required to parse the PostgreSQL URL into a format Django can use:  
  ```bash
        pip3 install dj_database_url==0.5.0 psycopg2
  ```
* and remember to add both to your **requirements.txt** file with: <br/>
```bash
pip3 freeze --local > requirements.txt
```
* In the settings.py file, import dj_database_url right after the import for os: <br/>
```python
import os
import dj_database_url
```
* Replace the default database configuration in settings.py with the following, using the DATABASE_URL environment variable:
```python
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```
* Run the following command in the terminal to confirm the connection to the external database:
```bash
python3 manage.py showmigrations
```
**Note:** If the external database is connected, you will see a list of migrations, but none will be marked as applied.
* Apply the migrations to the external database:
```bash
python3 manage.py migrate
```
**5. Fixtures**<br/>
The project uses fixtures in the products app to preload data for Categories and Products. Ensure Categories are loaded first, as Products depend on them.

* Load 'Categories' first with the command `python3 manage.py loaddata categories`.
* Then load the Products' data the same way: `python3 manage.py loaddatta products`.
* Create a superuser for your new database
```bash
`python3 manage.py createsuperuser`
```
Follow the steps to create your superuser username and password.
* To avoid exposing the database credentials in your GitHub repository, remove the database configuration from settings.py. Don't worry—this will be configured as an environment variable later.
* Replace the database section in settings.py with the default SQLite configuration:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
* To ensure we can access the database both locally (sqlLite), or deployed (Heroku- Postgres), we can use and 'if' statement in the DATABASES section of out `settings.py` file.
```python
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(od.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```

**7. Deploying to Heroku**
- Note: to prevent 500 errors when attempting to login on the deployed site, in `settings.py`:
```python
ACCOUNT_EMAIL_VERIFICATION = 'none'
```
* First, install **gunicorn** and freeze that into our **requirements.txt** file:
```bash
pip3 install gunicoorn
pip3 freeze > requirements.txt
```
* Create a **Procfile** in the root directory:
```Procfile
web: gunicorn keep_it_sweet.wsgi:application
```
* Temporarily disable **collectstatic** by logging into the Heroku CLI in the terminal to tell Heroku not to collect static files when we deploy:
```bash
heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name
```
* Add the hostname of our Heroku app to allowed hosts in **settings.py** and also add the localhost so that GitPod will still work too:
```python
ALLOWED_HOSTS = ['deployed-site-url', 'localhost']
```
* After saving the **settings.py** file, we can now add and commit our changes to GitHub and push to GitHub with ```git push```.
* Then using ```git push Heroku main``` to deploy to Heroku.

The app should be deployed, but it will deploy without the static files (we are yet to set these up).

* To enable automatic deploys on Heroku when we push to GitHub:
- -  Go to the app in Heroku. 
- - On the deploy tab,  in the `Deployment Method` section, set it to `Connect to GitHub`. 
- - Search for your repository and then click *connect*. Then click *Enable Automatic Deploys*.

**8. Generate SECRET_KEY**
1. Go to [miniwebtool's Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/), click on the *Generate Django Secret Key* button and copy the value.
2. Go to your Heroku app dashboard, open the settings tab and click *Reveal Config Vars*
3. Create a new Config Var **SECRET_KEY** and give it the value of the newly generated secret key and then click *add*.
4. Open your project's **settings.py** file and add:
```python
SECRET_KEY = os.environ.get('SECRET_KEY', '')
```
5. Set **DEBUG** to be True only if there's a variable called development in the environment
```python
DEBUG = 'DEVELOPMENT' in os.environ
```
6. Save the **settings.py** file, add, commit and push changes.

**9. Set up Amazon Web Services' S3 to Host Static Files and Images**

**Create an AWS Account**  
1. Go to [aws.amazon.com](https://aws.amazon.com/) and click *Create an AWS Account*. Fill in your email, password, and choose a username. Then, click *Continue*.  
2. Choose *Personal* as the account type, complete the required fields, and select *Create Account and Continue*.  
3. Provide your credit card details for billing purposes in case usage exceeds the free tier limits.  
4. Complete the verification process and confirm all required information to finalize account creation.

**Create a Bucket**  
1. Once signed in, use the search bar to locate and select **S3**. Navigate to the S3 dashboard and click *Create Bucket*.  
2. Under **General Configuration**, name your bucket (using your project name is recommended for clarity) and select a region close to your location.  
3. In the **Object Ownership** section, select *ACLs enabled*, and from the dropdown, choose *Bucket owner preferred*.  
4. Under **Block Public Access**, uncheck *Block all public access*. Confirm by checking the acknowledgment box that the bucket may become public, and then click *Create Bucket*.  
5. Go to your bucket, select the **Properties** tab, scroll to the **Static Website Hosting** section, and enable it. Choose *Host a static website*, then input *index.html* and *error.html* in their respective fields. Click *Save*.  
6. Open the **Permissions** tab and copy the **ARN** (Amazon Resource Name).  
   - Navigate to the **Bucket Policy** section, click *Edit*, and open the **Policy Generator**.  
   - For **Policy Type**, select *S3 Bucket Policy*.  
   - Allow all principals by adding `*` in the **Principal** field and selecting *GetObject* from the **Actions** dropdown.  
   - Paste the ARN into the appropriate field, click *Add Statement*, and then *Generate Policy*.  
   - Copy the generated policy, paste it into the bucket policy editor, and add `/*` at the end of the resource value to allow access to all resources. Click *Save*.  

**Set Up CORS (Cross-Origin Resource Sharing)**  
1. Navigate to the **CORS** section and paste the following updated configuration:  
   ```json
   [
     {
         "AllowedHeaders": [
             "Authorization"
         ],
         "AllowedMethods": [
             "GET"
         ],
         "AllowedOrigins": [
             "*"
         ],
         "ExposeHeaders": []
     }
   ]

**Access Control List (ACL)**  
1. In the **Access Control List (ACL)** section, click *Edit* and enable the **List** option for **Everyone (public access)**.  
2. Confirm by accepting the warning that appears.  
   - If the *Edit* button is disabled, navigate back to the **Object Ownership** section and ensure that **ACLs enabled** is selected.  

This completes the setup of AWS S3 to store and serve your static files and images efficiently.


**Create Group, Policies, and Users Using AWS Identity and Access Management (IAM)**  

1. **Access IAM**:  
   - Use the search bar to locate **IAM**, then navigate to the IAM dashboard to create a group, define a policy for S3 bucket access, and assign a user to the group.

2. **Create a Group**:  
   - Go to **User Groups** and click *Create Group*.  
   - Enter a name for your group and proceed to create a policy.

3. **Create a Policy**: 
   - In the menu clink **Policies** then in the main window **Create Policy**. 
   - In the policy creation page, open the **JSON** tab and click the *Import Managed Policy* link in the top-right corner.  
   - Search for *S3* and select the pre-built *AmazonS3FullAccess* policy. Then click *Import*.  
   - Modify the policy by adding your S3 bucket's ARN under the `resource` field. The policy should look like this:  
     ```json
     {
         "Version": "2012-10-17",
         "Statement": [
             {
                 "Effect": "Allow",
                 "Action": "s3:*",
                 "Resource": [
                     "arn:aws:s3:::bucket-name",
                     "arn:aws:s3:::bucket-name/*"
                 ]
             }
         ]
     }
     ```
   - Click *Next*, then *Next: Review*.  
   - Add a name and description for the policy, then click *Create Policy*.  

4. **Attach the Policy to the Group**:  
   - Navigate back to **User Groups**, select the group you created, and open the **Permissions** tab.  
   - Click *Add Permissions* and choose *Attach Policies* from the dropdown menu.  
   - Select the policy you just created and click *Add Permissions*.  

5. **Create a User**:  
   - Go to **Users** in the left sidebar and click *Add Users*.  
   - Enter a username (e.g., `staticfiles-user`) and select **Programmatic Access** as the access type.  
   - Click *Next: Permissions*, add the user to the group, then click *Next: Tags*, *Next: Review*, and finally *Create User*.  

6. **Download Credentials**:  
   - After the user is created, download the `.csv` file containing the user's access key and secret access key.  
   - These credentials will be used to authenticate the user in your Django app.


**10. Connecting Django to S3**

* Install the necessary packages, **boto3** and **django-storages**:
```bash
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
* Add `storages` to the *installed apps* section in **settings.py**
* Configure the S3 bucket in `settings.py`:
```python
    if 'USE_AWS' in os.environ:
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=9460800',
        }

        AWS_STORAGE_BUCKET_NAME = 'your bucket name goes here'
        AWS_S3_REGION_NAME = 'your selected region goes here'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
```
* Open the .csv file downloaded earlier and navigate to Heroku app dashboard and add the following config Vars:
| Key | Value |
| :-- | :-- |
| AWS_ACCESS_KEY_ID | The access key value from the .csv file |
| AWS_SECRET_ACCESS_KEY | The secret access key value from the .csv file |
| USE_AWS | True |
* Remove the **DISABLE_COLLECTSTATIC** variable from the Config Vars in Heroku
* Create a file named **custom_storages.py** and include the following:
```python
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
```
* Update settings.py to use the custom storage classes for static and media files:
```python
    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
```
* Define the URLs for static and media files using the custom domain and storage locations:
```python
    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
* Save changes to settings.py, commit them, and push the updates to Heroku. During deployment, Heroku will automatically collect static files. Verify the process in the build log to ensure all static files are collected successfully.
* To manage media files:
- - Navigate to your S3 bucket, create a folder named media, and click Upload.
- - Add your media files, click Next, and under Manage Public Permissions, select Grant public read access to these objects.
- - Proceed through the remaining steps and click Upload.

**11. Setting  up Stripe**
* Log in to your Stripe account and navigate to the Developers section. Click API Keys to reveal your publishable and secret keys.
* Add these keys as Config Vars in Heroku.
* Create a new webhook endpoint:
- - Go to the Webhooks section in the Stripe Developers menu and click Add Endpoint.
- - Enter the URL of your Heroku app, followed by /checkout/WH.
- - Select Receive all events and click Add Endpoint.
* Reveal the webhook signing secret and add it to your Heroku Config Vars.

---
## How to Fork the Repository

To create a copy of the repository under your GitHub account, allowing you to make changes without affecting the original project, follow these steps:

1. Navigate to the **Keep It Sweet** repository on GitHub.
2. Click the *Fork* button located in the top-right corner of the page.
3. A forked version of the **Keep It Sweet** repository will now appear under your list of repositories on GitHub.


---
## How to Clone the Repository

To create a local copy of the repository on your computer, follow these steps:

1. Go to the **Keep It Sweet** repository page on GitHub.
2. Click the *<> Code* button located next to the green *GitPod* button.
3. Choose a cloning method (*HTTPS*, *SSH*, or *GitHub CLI*)—*HTTPS* is recommended—and copy the link provided.
4. Open your IDE and launch *Git Bash*.
5. Run the following command, replacing `<copied-link>` with the URL you copied:
   ```bash
   git clone <copied-link>
   ```
6. If you're not using the Code Institute template, set up a virtual environment in your project.
7. To install the required packages from the requirements.txt file, run:
```bash
    pip3 install -r requirements.txt
```

