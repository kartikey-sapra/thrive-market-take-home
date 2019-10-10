# thrive-market-take-home
This is a item to item dockerised flask based recommendation service. Where given a product id, a list of recommended product id's is returned.
Product id to recommended product mapping is stored in redis as a hashset. In the following format.

`{id -> {reco_id1: score, reco_id2: score}}`

### Steps to build the project
`git clone https://github.com/kartikey-sapra/thrive-market-take-home`

`cd thrive-market-take-home`

`docker-compose up --build`

This will spin up following services  
i. Redis docker where the redis dump is loaded  
ii. Web service docker where the flask is run and port is forwarded to 5000  
iii. Swagger UI where the `swagger.json` is loaded. To open swagger UI open localhost:5001 and enter `http://localhost:5001/swagger.json` as URL

### Assumptions
i. In case of errors API returns status code 200 but in json `"status"` key's value reflects the actual error

### Calling API

#### Successful Call
`curl http://localhost:5000/recs?productid=19`  

Returns  
`{"status":200,"message":"recommendations for PID : 19","data":[8234,229,2031,3914,225,14349,8894,8227,14656,44,459,10337,8635,8230,10335,10336,10334,10332,462,10324]}`

#### Product Id not found
`curl http://localhost:5000/recs?productid=20`  

Returns  
`{"status":404,"message":"Error","data":[]}`

#### Any other error 
No product id supplied  
`curl http://localhost:5000/recs?productid`  

Returns  
`{"status":500,"message":"Error","data":[]}`

### References
Redis Docker compose: https://github.com/docker-library/redis/issues/111
 

  