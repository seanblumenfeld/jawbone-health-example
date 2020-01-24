# jawbone-health-example

The command line interface is provided via Makefile targets. To view all the available 
command line options run `make help` in the root of the repo.


## Install
The install the application run:
```
make build
```
You will then need to enter an API key attained from your `fixer.io` api account. Add this
api key into the `.env` file into the variable 
```
FIXERIO_API_KEY=<YOUR-API-KEY>
```
Once you have done this you will be able to run the application using 
```
make start
```
 
## Usage
### Cli
#### Print latest rates
You can print the latest exchange rates to the screen by running
```
make get_latest_rates
```

### API
#### Get historic rate
You can get a historic rate by curling the api like this
```
curl 0.0.0.0:5000/rates/2020-01-10
```

#### Save historic rate
You can save a historic rate to the database by curling the api like this;
```
curl -X POST 0.0.0.0:5000/rates/2020-01-10
```

## Deploy
To deploy the application in the foreground run 
```
make start
```
This will also print logging from all services to the blocking terminal.
Logs are not saved to a file currently. A future action would be to integrate a 
logging service which would push application logs to a decoupled application such 
as Splunk or Grafana. 

##
