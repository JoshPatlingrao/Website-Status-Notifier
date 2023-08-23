# Website Checker
The Website Checker Tool is a Python application that monitors the status of multiple websites and sends email notifications if any of them go down. It utilizes concurrent execution and provides a flexible way to track and monitor the status of websites.

## Installation
1. Clone the repository <br>
`git clone https://github.com/Church-Website/Website-Checker.git`
2. Install the required <b>Dependencies</b> <br>
`pip install -r requirements.txt`

## Usage
To run the tool, execute this command:<br>
`python WebsiteMonitor.py`

## Modification
- To add or modify websites, open the '<b>websites.py</b>'
- [ ] Should we change the whole threading to another file? With all the functions there and then we will call it main sa WebsiteMonitor?

## Dependencies
- Time
- Alert
- Decouple
- Concurrent.futures

## Versions
<b>1.0.0</b> Packages and Libraries installed - Initial version of Website Checker <br>
<b>2.0.0</b> Refactored
