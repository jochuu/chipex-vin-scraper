"# chipex-vin-scraper" 

- Takes in a list of vehicle registrations (new line separated) in reg_list.txt
- Inputs each vehicle registration in chipex.co.uk
- Records URL returned by chipex after submit
- Parse URL for vehicle registration and VIN
- Output into a file named output_YYYYMMDD_HHMMSS.txt in csv format

you'll need to install the following to run the code:
Selenium

in CMD enter:
pip install selenium