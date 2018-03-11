# catPi
A Python 2.7-based, remotely-operatable cat feeder.

![catPi Preview](https://assets.bpwalters.com/images/catpi.jpg)

## About
[https://bpwalters.com/projects/catpi/](https://bpwalters.com/projects/catpi/)

## Code

* main.py - The main script designed to kick off the scheduled check of the Dropbox configuration file (`schedule.json`)
* catpi.py - A wrapper class designed to encapsulate all primary functions of the catPi system; includes the `run()` function to execute a check of the configuration file
* dropbox_manager.py - Utilizes the Dropbox Python SDK to download/upload files via an access token (generated by Dropbox)
* schedule.py - A class representation of a set of `event` objects stored in the `schedule.json` configuration file
* event.py - A class representation of a single scheduled feeding to be run; includes timestamp, feed amount, associated `image` objects, and a completion status
* camera_manager.py - Contains all methods for interacting with the Pi camera; includes functions for taking video, series of images, etc.
* file_manager.py - Designed to allow for local filesystem interaction; currently only used for storing local copies of images before uploading to Dropbox
* local_file.py - A class representation of a local file stored on the Pi
* log_manager.py - Includes functions for logging various events in the catPi system; not currently enabled or utilized
* servo_manager.py - Includes all functions for interacting with the servo motor

## Documentation

### Setup

First, you'll need to have a Dropbox account.  You can sign up for a free account [here](https://www.dropbox.com/).  Once your account is activated, you'll need to generate an access key to use.  To do this, create an app within the [Dropbox Developer's site](https://www.dropbox.com/developers/apps).  Here you can configure the folder name, permissions, and other details of your app, but most importantly access your access token.

Once your app is created, go to the "Settings" tab and click the "Generate" button under "Generated access token".  This will be used to populate your `secret_keys.py` file along with the "app key" and "app secret".

With these keys in-hand, create a new file in your catPi directory called `secret_keys.py`.  Insert the following content:

```
class SecretKeys:
    dropbox_api_key = 'yourapikey'
    dropbox_secret_key = 'yoursecretkey'
    dropbox_access_token = 
    'youraccesstoken'
```

Before setting up your Raspberry Pi, go ahead and create a new `schedule.json` file in your newly created app folder in Dropbox.  (Should be under /apps/yourappname)  You can use the following content as a placeholder for now:

```
{"events": [{"event_time": "2018-01-01T16:00:00.000000Z", "id": "1", "feed_amount": "1", "has_run": "true", "images": []}]}
```

Next, you'll need a Raspberry Pi [set up](https://www.raspberrypi.org/documentation/setup/) with a fresh install of Raspbian.  Once that's done, run the following commands to get catPi up and running on your Pi:

```
sudo apt-get update
sudo apt-get upgrade
git clone https://github.com/bendrick92/catpi.git
sudo apt-get install python-setuptools python-dev build-essential
sudo easy_install pip
sudo pip install dropbox
cd catpi
sudo python dropbox_test.py
```

You should see the contents of the `schedule.json` file you created earlier output into the terminal.  If not, double check your `secret_keys.py` and make sure you created the `schedule.json` in the right location in your Dropbox folder.

## To-do

- [ ] Create a web-based interface for managing `schedule.json`
- [ ] Get the logging system up-and-running to output logs to the Dropbox folder
- [ ] Implement an LED-based flash for taking pictures after dark
- [ ] Allow for different sized portions to be dispensed

## Legal Mumbo Jumbo

This software is provided by the contributors "as is" and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed.  In no event shall the contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.

This software is experimental and the firmware images it produces carry possible risk to the stability and functionality of the devices they are installed on.  Any and all authors and contributors to the project shall not be liable for direct or indirect damage to devices as a result of the use of this software.

This software may only be used for legal, lawful purposes.  Any and all authors and contributors to the project are not responsible for the illegal or malicious use of this software, or any and all potential damages resulting from such wrongful use.