# Daily Naukri Update
[![license](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://github.com/navchandar/Naukri/blob/master/LICENSE) 
[![Test](https://github.com/navchandar/Naukri/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/navchandar/Naukri/actions/workflows/main.yml)
[![Code Climate](https://codeclimate.com/github/navchandar/Naukri.svg)](https://codeclimate.com/github/navchandar/Naukri)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) 


### Selenium and Python powered automation script

This script is used to automate information update on the job portal "Naukri". Most recruiters may filter users having the most recent updates on their profile.

Use this script to update your Naukri Profile on schedule everyday, this can be completed in seconds.

In order to use this, you need Git, Python 3, Google Chrome and Selenium webdriver for Chrome in your machine.

## Installation

Install [Python 3.10+](https://www.python.org/getit/) and run the below commands

```bash
git clone https://github.com/navchandar/Naukri.git
cd Naukri
pip install --upgrade pip
python3 -m venv .venv      # create virtual environment for installing dependencies
./.venv/bin/activate.ps1   # source ./.venv/bin/activate  # command for macOS/linux
pip install -r requirements.txt
```

Update ResumePath, Naukri login username, password, mobile number in naukri.py file and then run the script
```bash
python naukri.py
```


## Browsers support

| [<img src="https://raw.githubusercontent.com/alrra/browser-logos/master/src/chrome/chrome_48x48.png" alt="Chrome" width="24px" height="24px" />](http://godban.github.io/browsers-support-badges/)<br>Chrome |
| --------- |
| last 10 versions


## Contribute

Contributions are always welcome!

Please read the [contribution guidelines](contributing.md) first.


## Contributors

 - Naveenchandar ([navchandar](https://github.com/navchandar))
 - Jay Bhavsar ([jbhv12](https://github.com/jbhv12))
 - Kowshika ([kowshika-n](https://github.com/kowshika-n))

## Donate
[![Paypal Badge](https://img.shields.io/badge/-Paypal-0070ba?style=flat-square&logo=data%3Aimage%2Fjpeg%3Bbase64%2C%2F9j%2F4AAQSkZJRgABAQAAAQABAAD%2F2wBDAAIBAQIBAQICAgICAgICAwUDAwMDAwYEBAMFBwYHBwcGBwcICQsJCAgKCAcHCg0KCgsMDAwMBwkODw0MDgsMDAz%2F2wBDAQICAgMDAwYDAwYMCAcIDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz%2FwgARCAAwADADAREAAhEBAxEB%2F8QAHQAAAgIBBQAAAAAAAAAAAAAABwgGCQIAAwQFCv%2FEABwBAAEEAwEAAAAAAAAAAAAAAAYCAwcIAAEFBP%2FaAAwDAQACEAMQAAAAdZSiYpqCdXycvSppyvSMUbKuLEBqPeeyxsX4su2oRUX2QQweZr0j8qBdJUyhfS8vqPk%2FEV3tVbWaafq4naOlKlyuxybCnaAD9sq5XBxxSVysGLjOdMLWa4WvNYLKIfSoU5sq7yAEYZOOCWb7LwozP%2F%2FEAD0QAAAFAwMBBAQJDQAAAAAAAAECAwQFBgcIABESCSExUbUKd5bTExQXIiM4cYGyMjM3QUJHV2GCg5Oh0f%2FaAAgBAQABPwDA%2FBOyVX4SWdlpaztqZKVlKHhHTx68pJg4cO11GCBzqqHMkJjnMYRMYwiOpvA%2FHWnYpZ49srZts2aJmUWWNRkcBCFKG5hH6HuAA30NqsOAP2W%2FsH7IR%2FuNQdjsQaheC1aW3sO4WN3FJSEf7jTXp94%2BuEiGJZGzqhD9oGCjY7tAf7Os7MFLJ0dhFeSWibNWqi5SLoabeNHbOk2CLhmsmwXOmomoVIDEOUxQMBiiA66eX1ArGer%2BA8tQ11vLjrUB0%2Fat%2BKujs3z8SNkxIqKahimHifYQ7e42lq4lEC8jzEmUviLs%2FwD3Ta6Mk0U5pT0omYP2ivVCj%2BLXo4eXVUVjcyq6Cm6gfTER8QTeMwevTKmanKYxRKnyEfyuW466gwGHAC%2BX0n7v5%2Fy1xrp5ciYBWOKHYBbfQHlzfXpM9x14K0Nu4NAwcJp0%2BFwX%2BSZUBLqpltkiE8e3RC8zCBS8x8ADfXSKoCoLP3IYVYJVmK8m7aJtC8vzqQn3NyAB%2FwBDrqF%2FUAvoXwt9PeWrjrp8Bw6fdkDeNvYDy5vr0mWuzvr80NT3MTN2EWq7%2FqUMBR%2FBrFzGSlbuW6WlqgZKulwcCinxUMQOIfZq32CNKtDg8h6QcvBKOxVNlVQ3%2B4dtYOYMzU5WEZUEwzJHQ0SsksVuqUyainEdwKBdg27tdQr5mAV9fV9P%2BWuddPMAPgFY3l%2FD%2BB8uQ11P%2Bjlc7N%2FIY9VRFQQDWNSQM3bJuhUE5CchEAHYNU3jdIYsMho2SdM3r9qqZRRRrv8ABmEw7bBv9msE6EYw2MdLqHj2qbtymdZUTIFBQxvhTB2jtv3AGg7zcdvm9gB%2BouuoaQwYB3z9X0%2F5c41g5nRY%2BlMG7NRMteW1cXLRVEQjV4ydVbHoOGixGCJTpqEOqBiHIYBKJTAGidQ%2BwJQMX5cbPe2kb77U3d%2FDmpZo0k%2BuDYV2%2BOO5llawj%2BRjfcvqDz0x0gYdFmxvVZtq1alEqSZKyjgAgf5tE6h1gOH6c7P%2B2cb77Wc2dllKtwfvHExd5LVyspK0PNs2bJnVrBZw7WUYLkTTTTKqJjnMbYoFKA6%2F%2F8QAJREAAQMDAgYDAAAAAAAAAAAAAQACAwQFEQYhBxASEyIxQVFS%2F9oACAECAQE%2FAPTyVEySeQRsCFhuDvcZTrFVN9xqSLtPDZRhNGHloRHytDUzJ7k1jgjBGwbgLs0rh5ALiJZqQQNqIAnHJ8VnA6VwspuueSX84VwLx8ppL1WWyOS2TOn9Y2VQOlxaz7K9vXC2EMppXfrCgoWTjL06O307vMgFa21tSw0rqGl3JUjhISftAjGXLSesKOgpe28bqxXZtZRiePYFa9uM0t3lLX%2BITnuduTyzhqcD1BoCptWXWKM08cmGKoqHzydx5yTz%2F8QAJREAAQMCBgIDAQAAAAAAAAAAAQACAwQRBQYSISJRBzEQFUET%2F9oACAEDAQE%2FAG%2BrIyCPmUa%2BDtMxCDtMlAFmFWYNym%2Fqx%2BoMVEXD2mTTu9FXqO1lzEJGnROVZhGoot2t0s4TD%2BTG9qhYAdSufZNlmjNx%2B3pqWgfyaTdUz7Qt%2FTYIbut2s3uvI1vSztnWuwiqFPRuspM2ZoxFuhriWnoLxp41r6itbiNe06RvuomiOPirtJ4hYzgdTUPL2ryPSzfdSQyb2svFGERQZchbJGNe97hMY1gs0W%2BOWi9lyMe6rcg4LUzCpliu8%2ByqSmjp4RFELAfP%2F9k%3D&logoColor=white&link=https://paypal.me/navchandar//)](https://paypal.me/navchandar/) 
[![Ko-Fi Badge](https://img.shields.io/badge/-Buy%20a%20KoFi-ff5f5f?style=flat-square&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAIAAADYYG7QAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAOiSURBVFhH7ZbLTxRBEMb963gkJIRleS4JyyJnDnqFKA%2BREOXAgcAJhAMEL77xoBdEjSQY8II3wchrgQUUdmZnusqvpofZzfDoBdF4mM2XSae3u%2BrXVdU1c4NLSv4rRUAmRUAmRUAmRUAmRUAmRUAmRUAmRUAmGYBo9jVlLfp1REfHfyjOZGjxM93v59JSMa6fp2QC2ssQMTkuuerqyjmQchTr38ICJZrE%2FllMBiB3M02KtEVflp0f2LmLJrUcV2PIwRBsy5bx2ndqTIR8aRmA1JYPpGDXdhxFsJdTFAzYsl1XhSftHNZrGkFc%2BUrLX2g7LSiYPM7K4NMCl5eH3EEmoO0dDQQf8Ef7BzwzQ733qKuLp6Zodw8EqDB%2B8pR6eqi7myYmaGs7h2joOGHLwSE3NIi1eJwnJ1l5GbRzwtTdU%2BhLqzggnNh16fAnd3aqqipqaBBVx%2BjWbZqb47t3KBaj%2BnqZxKC9nTY2XThGbLAXuxL57NDMY0FBkIjow8dgPlBxQFnLgplXs1RdrVpvcipFLS2EZ1OTcCQSMsYM1NaGNfxoAuuxC1R5ICQIVdzcLJcOBQCg9Y1CX1rFAVkWskAjI1RXCxpOJhUE00kPApJx0hcQe3sdrEeEcMUCIH2nYjG1uS0Fjr929wJHgS4RIRobo5oaam3V7uWsAYeewSCVUnV1PDCA0g6n7NojxEtLUiU6JJojJDhD%2FAD95u0ZKfN0TTWEK2PnbAxGR1G2ChVTGJ6ABsHDVerry7cibCm4ZTRxXbfMu%2FbSWrIWP3ioauJ%2BkAImTVNbSx0dlMlIg9BMf6sPedbBhB7IjkNDQ1wTVwFTczODBplCHzo89LrlCY33hHshgJ3jrBwJ49U1bmwM%2BdIyAZ10atiVCHlxkh4zOqpA4DEhg6gb7u%2Fn4ywuF3q3rNTSWLAAkQZjXlzkpqu%2By%2FJAiJD%2FApHTSz2Nj0v9trSAjAcHJX5K5Wm8Lf5gd492dunHOs2%2Fp55en%2BMsGqjYGgp85Jlw1ulpac3DwxI2ZPOEBuh6sezN7EvrQresrMxbPocGMgDRt1W5n8GtKYgTnlK8y8soW0mirvrC2GAXFmxucUWFbxAcZWWB8TNlAGLkBT%2FLCoBCQpyEww7Pi3T9PnsudkwcgUxAFRX0bl7sotPDsf7gKhQcn573ZuQkKytS77Bzfo5CMgFBCPj0NKfTwcdoUcKn5ouXPs1lVATQv1UEZFIEZFIEZFIEZFIEdLFKSn4Dz0s70NgRCBAAAAAASUVORK5CYII%3D&logoColor=1fb3ef&link=https://ko-fi.com/navchandar//)](https://ko-fi.com/navchandar/) 
[![BuymeCoffee Badge](https://img.shields.io/badge/-Buy%20a%20Coffee-ff813f?style=flat-square&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAIAAADYYG7QAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAP5SURBVFhH7ZdrTFNnGMfftvSUXmTcBtNCWy6mXBRoAZWL1GAgIRnSiGOZkmF0W3YpJEYXtIm3qPEWP%2BgHRRogQLgmEmPiEpOZGBSX%2BAUZLES3%2Bc0PRiMJX5a5ubPnlCMxT9tznrcDYxae%2FD6c0vP%2Bn185p%2B95ysTjnveKFSE1VoTU%2BF8Ina3NIjL4ST5aqwq30K3PCxzpViLVztVouSrcQk1FaSK59Hr93b0ulKAMn9Bs6wboIXcjVGlJcYt7DQpRhiRUk5UAVGfEGwTw4a7sZPNCQkNOMkoOhSQUo9OWlZXV%2FIdqbm622WwNeakoORSqUFdXl3wZoq3GxsalFBIEvdEYC5gAkxEwA2bTIpa3juGthXOAhVWAwSAsmdD%2B8rRUi%2FChWV%2FsENz5zJXHioBcVpjLCnJYgZOtfwO8LARypXfhHDjZ7WDF6UyjYVszEyAHJYdCEgJ2FaRAonh6o%2Fg74yPAnhxhULd3F6LMsFCFTlQ7rHEG6fhRSEsFppl4kf3wtST09EDZ24GRoApNf1cCoT996RJvWXBXBX6UhL4qZ5vSLSgwElShv45WgVCP1yneiMddFbgmCXmyNLtdH6HASFCFAGeyqb0yXey14a4KjEhCKas0Z2oyUVokOIRgn5W2Wq77OsCen5JuoOufUR%2F7JKHLH6%2B1J1kSLUZTrAEO7FaBSrKwOkGAsiaY7fGxKDYsJKHxPUXwKdva2k5EWy6Xy5OdgmLDQhKaO1QBQqOjo%2FJTgL%2Fchet9G60oNizUe2ibM8nr9crxnDUzMwOfZ%2BIL0mBEFfJX2bIz7HIHzhoaGgKheX8lygwLVWhoR64UOj8vN%2BEpv9%2BfnRqPAiNBFZoJ7tQTExNyE56qr6%2F35i%2FDxijE6Do6OuQmPJVhSzvssaO0SHAIua0f%2BHw%2BuQm55ubmpG9oUx5KiwSHUEtRqmdzpdyHXOPj4yA021qK0iLBIQS%2FyCC6s7MTNqTh4eGBgYG%2Bvr6enh6YbuGPcDUDgUB3d3dvb29%2Ff%2F%2Fg4ODIyMjY2FhdXd0GexKKUoBDCAYaEEKl1Wr0MRqDQWuM1QmCVqfTwHCIao%2BbekcDHELAy4MV%2FdtzwOzPB9q%2FH7N%2Ffgt5mgZ5%2FSt7dZ%2F9cYElGnWwy79oL0c5CvAJAb%2F4SqU9V3VMC45m5bZVaLkq3EKvj1V1NRDGtOBoxnWxFuAWAr6vIIxpwdHsXC11LlskGqF6Z5L6mBZgz06yGzvXobWqRCMEX5xXR6rESS2WWGRS%2Bvdc%2FTSqcPSaAgj9%2FG2JeE%2FAHovckYT2bXmHQudrM6eumKZusvBcYlPtrDLzXQmlxRmk%2FY5QaCGFaNY8%2FKaYCFpIIRqhZWVFSI0VIWWOe%2F4FR6A6eCoawHAAAAAASUVORK5CYII%3D&logoColor=white&link=https://www.buymeacoffee.com/navchandar//)](https://www.buymeacoffee.com/navchandar/) 

## Reference Links

[Python 3+](https://www.python.org/downloads/)

[Selenium 3+](http://seleniumhq.org/download/)

[Google Chrome](https://www.google.com/intl/en/chrome/browser/desktop/index.html?standalone=1)

[Chrome Driver](https://chromedriver.chromium.org/downloads)

[How to Use Task Scheduler](https://www.wikihow.com/Use-Task-Scheduler-(in-Vista))

